#!/usr/bin/env python3
"""
Launch Ansible Tower / Automation Controller job template using REST API.

Interview use:
GitHub Actions can call Tower API to run pre-checks, post-checks, patching,
or controlled operational automation. Tower provides RBAC and audit history.

Required environment variables for real use:
- TOWER_URL, example: https://tower.company.com
- TOWER_TOKEN
- TOWER_TEMPLATE_ID

Optional:
- TOWER_EXTRA_VARS as JSON string
"""

import json
import os
import sys
import requests


def main() -> int:
    tower_url = os.getenv("TOWER_URL")
    token = os.getenv("TOWER_TOKEN")
    template_id = os.getenv("TOWER_TEMPLATE_ID")

    if not all([tower_url, token, template_id]):
        print("Tower variables are not configured. Skipping Tower launch for local lab.")
        return 0

    extra_vars_raw = os.getenv("TOWER_EXTRA_VARS", "{}")
    extra_vars = json.loads(extra_vars_raw)

    url = f"{tower_url.rstrip('/')}/api/v2/job_templates/{template_id}/launch/"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    payload = {"extra_vars": extra_vars}

    response = requests.post(url, headers=headers, json=payload, timeout=30)
    print(f"Tower launch status: {response.status_code}")
    print(response.text[:1000])
    response.raise_for_status()
    return 0


if __name__ == "__main__":
    sys.exit(main())
