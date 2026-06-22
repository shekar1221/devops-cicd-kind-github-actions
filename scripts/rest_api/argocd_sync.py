#!/usr/bin/env python3
"""
Trigger Argo CD application sync using REST API.

Interview use:
In GitOps, Git is the source of truth. CI updates Git/manifests and Argo CD
syncs the desired state into Kubernetes.

Required environment variables for real use:
- ARGOCD_URL
- ARGOCD_TOKEN
- ARGOCD_APP
"""

import os
import sys
import requests


def main() -> int:
    url = os.getenv("ARGOCD_URL")
    token = os.getenv("ARGOCD_TOKEN")
    app = os.getenv("ARGOCD_APP", "payment-api")

    if not url or not token:
        print("Argo CD variables are not configured. Skipping Argo CD sync for local Kind lab.")
        return 0

    api = f"{url.rstrip('/')}/api/v1/applications/{app}/sync"
    response = requests.post(api, headers={"Authorization": f"Bearer {token}"}, json={}, timeout=30)
    print(f"Argo CD sync status: {response.status_code}")
    print(response.text[:1000])
    response.raise_for_status()
    return 0


if __name__ == "__main__":
    sys.exit(main())
