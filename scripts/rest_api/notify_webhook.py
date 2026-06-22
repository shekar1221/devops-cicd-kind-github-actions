#!/usr/bin/env python3
"""
Send deployment notification to Slack/Teams-compatible webhook.
"""

import os
import sys
import requests


def main() -> int:
    webhook_url = os.getenv("WEBHOOK_URL")
    status = os.getenv("DEPLOYMENT_STATUS", "UNKNOWN")
    environment = os.getenv("DEPLOYMENT_ENV", "kind")
    version = os.getenv("DEPLOYMENT_VERSION", "local")

    if not webhook_url:
        print("WEBHOOK_URL is not configured. Skipping notification.")
        return 0

    message = {
        "text": f"payment-api deployment status: {status}, environment: {environment}, version: {version}"
    }
    response = requests.post(webhook_url, json=message, timeout=15)
    print(f"Notification status: {response.status_code}")
    response.raise_for_status()
    return 0


if __name__ == "__main__":
    sys.exit(main())
