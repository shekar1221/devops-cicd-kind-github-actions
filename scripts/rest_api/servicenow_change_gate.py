#!/usr/bin/env python3
"""
ServiceNow change gate for CI/CD.

Interview use:
Before production deployment, the pipeline validates that the ServiceNow change
ticket is approved. If the change is not approved, deployment is blocked.

Required environment variables for real use:
- SNOW_INSTANCE_URL, example: https://company.service-now.com
- SNOW_USER
- SNOW_PASS
- CHANGE_NUMBER, example: CHG0045678

Optional:
- REQUIRE_CHANGE_GATE=true means fail if variables are missing.
"""

import os
import sys
import requests


def main() -> int:
    instance = os.getenv("SNOW_INSTANCE_URL")
    user = os.getenv("SNOW_USER")
    password = os.getenv("SNOW_PASS")
    change_number = os.getenv("CHANGE_NUMBER")
    required = os.getenv("REQUIRE_CHANGE_GATE", "false").lower() == "true"

    if not all([instance, user, password, change_number]):
        msg = "ServiceNow variables are not configured. Skipping change gate for local/non-prod lab."
        print(msg)
        return 1 if required else 0

    url = f"{instance.rstrip('/')}/api/now/table/change_request"
    params = {
        "sysparm_query": f"number={change_number}",
        "sysparm_fields": "number,state,approval,start_date,end_date,short_description",
        "sysparm_limit": "1",
    }
    response = requests.get(url, params=params, auth=(user, password), timeout=20)
    print(f"ServiceNow API status: {response.status_code}")
    response.raise_for_status()

    result = response.json().get("result", [])
    if not result:
        print(f"Change ticket not found: {change_number}")
        return 1

    change = result[0]
    print(f"Change found: {change}")
    approval = str(change.get("approval", "")).lower()
    state = str(change.get("state", "")).lower()

    if approval == "approved" or state in {"scheduled", "implement", "approved"}:
        print("Change gate passed")
        return 0

    print("Change gate failed: change is not approved")
    return 1


if __name__ == "__main__":
    sys.exit(main())
