# REST API Integrations in the CI/CD Pipeline

## Why REST APIs are important

CI/CD does not work alone. It communicates with other systems:

```text
GitHub Actions -> ServiceNow
GitHub Actions -> Ansible Tower
GitHub Actions -> Argo CD
GitHub Actions -> Prometheus
GitHub Actions -> Slack/Teams webhook
GitHub Actions -> Application APIs
```

## Integration 1: ServiceNow change gate

Script:

```text
scripts/rest_api/servicenow_change_gate.py
```

Purpose:

```text
Before production deployment, validate whether the change ticket is approved.
```

Interview answer:

> We can call ServiceNow REST API from GitHub Actions before production deployment. If the change is not approved, the pipeline stops. This supports compliance and SOX control.

## Integration 2: Ansible Tower job launch

Script:

```text
scripts/rest_api/ansible_tower_launch.py
```

Purpose:

```text
Trigger Tower job template for Linux pre-check, post-check, patching, or operational automation.
```

Interview answer:

> We can trigger Ansible Tower using REST API from GitHub Actions. Tower gives RBAC, credentials, workflow control, job history, and audit logs.

## Integration 3: Argo CD sync

Script:

```text
scripts/rest_api/argocd_sync.py
```

Purpose:

```text
Trigger GitOps sync or check application health.
```

Interview answer:

> In GitOps, Git is the source of truth. GitHub Actions can update manifests and call Argo CD API to sync or verify the application.

## Integration 4: Prometheus validation

Script:

```text
scripts/rest_api/prometheus_validate.py
```

Purpose:

```text
Validate post-deployment metrics like HTTP 5xx rate, latency, and restarts.
```

Interview answer:

> Deployment success should not mean only pod running. We should validate error rate, latency, and business API health using Prometheus and smoke tests.

## Integration 5: Webhook notification

Script:

```text
scripts/rest_api/notify_webhook.py
```

Purpose:

```text
Notify Teams, Slack, or another webhook endpoint after deployment.
```

Interview answer:

> Webhook notification improves communication with support, development, and management teams.

