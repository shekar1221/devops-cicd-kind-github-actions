# GitHub Actions Setup

## 1. Create GitHub repository

Example:

```bash
git init
git add .
git commit -m "Initial HSBC DevOps CI/CD Kind lab"
git branch -M main
git remote add origin https://github.com/<your-user>/hsbc-devops-cicd-kind-github-actions.git
git push -u origin main
```

## 2. Pipeline location

```text
.github/workflows/ci-cd-kind.yml
```

## 3. What the pipeline does

```text
Build JVM app
Run JUnit
Run Cucumber
Run REST API gates
Validate Kyverno policies
Create Kind cluster with 2 workers
Build Docker image
Load image into Kind
Deploy Kubernetes manifests
Validate rollout
Run REST API smoke test
Optionally call Argo CD
Optionally call Prometheus
Optionally send webhook notification
```

## 4. Optional GitHub secrets

For demo, these can be empty.

For enterprise simulation, configure:

```text
SNOW_INSTANCE_URL
SNOW_USER
SNOW_PASS
TOWER_URL
TOWER_TOKEN
TOWER_TEMPLATE_ID
ARGOCD_URL
ARGOCD_TOKEN
PROMETHEUS_URL
WEBHOOK_URL
```

## 5. Why no Jenkins?

This project uses GitHub Actions only. That is enough to explain CI/CD pipeline automation for this JD.

Interview answer:

> I used GitHub Actions instead of Jenkins. GitHub Actions handles build, test, scan, API gates, Kind deployment, Kubernetes validation, and post-deployment smoke testing.

