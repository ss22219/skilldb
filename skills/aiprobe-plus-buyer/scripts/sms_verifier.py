#!/usr/bin/env python3
"""
SMS Verification Channel Client
Supports SMS-Activate protocol, 5SIM API, and generic SMS OTP providers
for receiving verification codes during OpenAI / ChatGPT account registration and verification.
"""

import json
import os
import ssl
import time
import urllib.parse
import urllib.request
from typing import Dict, Optional, Tuple, Union


class SMSClient:
    """Unified SMS Verification Client for OpenAI/ChatGPT SMS OTP verification."""

    def __init__(
        self,
        provider: str = "sms-activate",
        api_key: Optional[str] = None,
        api_url: Optional[str] = None,
        timeout: int = 10,
    ):
        self.provider = provider.lower()
        self.api_key = api_key or os.getenv("SMS_API_KEY", "")
        self.api_url = api_url or self._default_api_url()
        self.timeout = timeout
        self._ctx = ssl.create_default_context()
        self._ctx.check_hostname = False
        self._ctx.verify_mode = ssl.CERT_NONE

    def _default_api_url(self) -> str:
        if self.provider == "5sim":
            return "https://5sim.net/v1"
        # Default to SMS-Activate standard endpoint
        return "https://api.sms-activate.org/stubs/handler_api.php"

    def _request_get(self, params: Dict, headers: Optional[Dict] = None) -> str:
        """Helper for GET HTTP requests."""
        headers = headers or {"User-Agent": "Mozilla/5.0"}
        query = urllib.parse.urlencode(params)
        url = f"{self.api_url}?{query}" if "?" not in self.api_url else f"{self.api_url}&{query}"
        
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=self.timeout, context=self._ctx) as r:
            return r.read().decode("utf-8")

    def get_balance(self) -> str:
        """Get current balance from SMS provider."""
        if not self.api_key:
            return "Error: SMS_API_KEY is not set."

        try:
            if self.provider == "5sim":
                headers = {"Authorization": f"Bearer {self.api_key}", "Accept": "application/json"}
                req = urllib.request.Request(f"{self.api_url}/user/profile", headers=headers)
                with urllib.request.urlopen(req, timeout=self.timeout, context=self._ctx) as r:
                    res = json.loads(r.read().decode("utf-8"))
                    return f"Balance: {res.get('balance', 0)} {res.get('currency', 'RUB')}"
            else:
                # SMS-Activate protocol
                res = self._request_get({"api_key": self.api_key, "action": "getBalance"})
                if "ACCESS_BALANCE" in res:
                    balance = res.split(":")[1]
                    return f"Balance: {balance} RUB/USD"
                return f"SMS Provider response: {res}"
        except Exception as e:
            return f"Failed to check balance: {e}"

    def get_number(
        self,
        service: str = "dr",  # 'dr' is OpenAI code in SMS-Activate, 'openai' in 5sim
        country: Union[str, int] = "0",  # Country code or 'any'
        operator: str = "any",
    ) -> Tuple[bool, str, str]:
        """
        Request a phone number.
        Returns: (success: bool, activation_id: str, phone_number: str)
        """
        if not self.api_key:
            return False, "", "API Key required. Set SMS_API_KEY environment variable."

        # Map common service names
        svc_code = "dr" if service.lower() in ["openai", "chatgpt", "gpt"] and self.provider != "5sim" else service

        try:
            if self.provider == "5sim":
                headers = {"Authorization": f"Bearer {self.api_key}", "Accept": "application/json"}
                url = f"{self.api_url}/user/buy/activation/{country}/{operator}/{service}"
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=self.timeout, context=self._ctx) as r:
                    res = json.loads(r.read().decode("utf-8"))
                    act_id = str(res.get("id"))
                    phone = str(res.get("phone"))
                    return True, act_id, phone
            else:
                # SMS-Activate protocol
                params = {
                    "api_key": self.api_key,
                    "action": "getNumber",
                    "service": svc_code,
                    "country": str(country),
                }
                res = self._request_get(params)
                if "ACCESS_NUMBER" in res:
                    parts = res.split(":")
                    # ACCESS_NUMBER:ID:NUMBER
                    return True, parts[1], parts[2]
                return False, "", f"Failed to get number: {res}"
        except Exception as e:
            return False, "", f"Exception during get_number: {e}"

    def get_code(
        self,
        activation_id: str,
        wait_seconds: int = 120,
        interval: int = 5,
    ) -> Tuple[bool, str]:
        """
        Poll for SMS OTP verification code.
        Returns: (success: bool, code_or_message: str)
        """
        if not self.api_key:
            return False, "API Key required."

        start_time = time.time()
        print(f"Waiting for SMS OTP code (ID: {activation_id})... Max wait: {wait_seconds}s")

        while time.time() - start_time < wait_seconds:
            try:
                if self.provider == "5sim":
                    headers = {"Authorization": f"Bearer {self.api_key}", "Accept": "application/json"}
                    req = urllib.request.Request(f"{self.api_url}/user/check/{activation_id}", headers=headers)
                    with urllib.request.urlopen(req, timeout=self.timeout, context=self._ctx) as r:
                        res = json.loads(r.read().decode("utf-8"))
                        sms_list = res.get("sms") or []
                        if sms_list:
                            code = sms_list[0].get("code") or sms_list[0].get("text")
                            return True, str(code)
                else:
                    # SMS-Activate protocol
                    params = {
                        "api_key": self.api_key,
                        "action": "getStatus",
                        "id": activation_id,
                    }
                    res = self._request_get(params)
                    if "STATUS_OK" in res:
                        # STATUS_OK:CODE
                        code = res.split(":")[1]
                        return True, code
                    elif "STATUS_WAIT_CODE" in res:
                        pass
                    elif "STATUS_CANCEL" in res:
                        return False, "Activation cancelled."
            except Exception:
                pass

            time.sleep(interval)

        return False, "Timeout waiting for SMS verification code."

    def cancel_activation(self, activation_id: str) -> str:
        """Cancel an ongoing number rental."""
        if not self.api_key:
            return "API Key required."

        try:
            if self.provider == "5sim":
                headers = {"Authorization": f"Bearer {self.api_key}", "Accept": "application/json"}
                req = urllib.request.Request(f"{self.api_url}/user/cancel/{activation_id}", headers=headers)
                with urllib.request.urlopen(req, timeout=self.timeout, context=self._ctx) as r:
                    return f"Cancelled ID {activation_id}"
            else:
                # SMS-Activate status 8 = cancel
                res = self._request_get({"api_key": self.api_key, "action": "setStatus", "status": "8", "id": activation_id})
                return f"Cancel response: {res}"
        except Exception as e:
            return f"Failed to cancel activation: {e}"


if __name__ == "__main__":
    client = SMSClient(provider="sms-activate")
    print(client.get_balance())
