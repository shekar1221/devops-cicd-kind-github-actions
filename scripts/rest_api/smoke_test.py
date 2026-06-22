#!/usr/bin/env python3
import os
import sys
import time
import requests


BASE_URL = os.getenv("APP_BASE_URL", "http://localhost:8080").rstrip("/")
TIMEOUT = int(os.getenv("API_TIMEOUT_SECONDS", "5"))
RETRIES = int(os.getenv("API_RETRIES", "10"))

ENDPOINTS = [
    "/health",
    "/api/payments/status",
    "/api/payments/demo-payment-001",
    "/actuator/health",
]


def call_endpoint(path: str) -> bool:
    url = f"{BASE_URL}{path}"
    response = requests.get(url, timeout=TIMEOUT)
    print(f"{response.status_code} GET {url}")
    if response.status_code < 200 or response.status_code >= 300:
        print(response.text[:500])
        return False
    return True


def main() -> int:
    print(f"Running smoke test against {BASE_URL}")
    for attempt in range(1, RETRIES + 1):
        try:
            failures = [path for path in ENDPOINTS if not call_endpoint(path)]
            if not failures:
                print("Smoke test passed")
                return 0
            print(f"Attempt {attempt}: failed endpoints: {failures}")
        except requests.RequestException as exc:
            print(f"Attempt {attempt}: API not ready: {exc}")
        time.sleep(5)
    print("Smoke test failed after retries")
    return 1


if __name__ == "__main__":
    sys.exit(main())
