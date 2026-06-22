#!/usr/bin/env python3
"""
Validate post-deployment metrics using Prometheus REST API.

Interview use:
Deployment success should not mean only "pod is running". It should include
business/API health, 5xx error rate, latency, and restart checks.
"""

import os
import sys
import requests


PROMETHEUS_URL = os.getenv("PROMETHEUS_URL")
QUERY = os.getenv(
    "PROMETHEUS_QUERY",
    'sum(rate(http_server_requests_seconds_count{application="payment-api",status=~"5.."}[5m]))',
)
THRESHOLD = float(os.getenv("PROMETHEUS_THRESHOLD", "1"))


def main() -> int:
    if not PROMETHEUS_URL:
        print("PROMETHEUS_URL is not configured. Skipping Prometheus validation for local lab.")
        return 0

    response = requests.get(
        f"{PROMETHEUS_URL.rstrip('/')}/api/v1/query",
        params={"query": QUERY},
        timeout=20,
    )
    print(f"Prometheus API status: {response.status_code}")
    response.raise_for_status()

    data = response.json()
    print(data)
    results = data.get("data", {}).get("result", [])
    if not results:
        print("No metric result returned. Treating as pass for demo; adjust for production.")
        return 0

    value = float(results[0]["value"][1])
    print(f"Metric value: {value}, threshold: {THRESHOLD}")
    if value > THRESHOLD:
        print("Prometheus validation failed")
        return 1

    print("Prometheus validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
