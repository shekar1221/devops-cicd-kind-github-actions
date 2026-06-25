#evOps CI/CD Kind GitHub Actions Lab

This project is built for the HSBC-style JD topics:

- Linux, Ansible, Python, DevOps tooling
- REST API integration with third-party tools
- CI/CD with GitHub Actions, not Jenkins
- JVM application
- JUnit and Cucumber tests
- Kubernetes on Kind with 2 worker nodes
- ConfigMap, Secret, probes, resources, Service, Deployment
- Kyverno policy-as-code
- Prometheus/Grafana readiness through metrics endpoint and scrape annotations
- ServiceNow, Ansible Tower, Argo CD, Prometheus, and notification REST API examples
- SOX/compliance style gates and audit-friendly workflow

## Architecture

```text
GitHub
  |
  | push / pull request
  v
GitHub Actions
  |
  |-- Maven build
  |-- JUnit tests
  |-- Cucumber BDD tests
  |-- ServiceNow REST API change gate
  |-- Ansible Tower REST API optional pre-check
  |-- Kyverno policy-as-code check
  |-- Docker image build
  |-- Kind cluster deployment
  |-- Kubernetes rollout validation
  |-- REST API smoke test
  |-- Argo CD REST API optional sync
  |-- Prometheus REST API optional metric validation
  |-- Teams/Slack webhook optional notification
```

## Folder structure

```text
app/                         JVM Spring Boot payment API
app/src/test/                JUnit and Cucumber tests
kind/cluster-2-workers.yaml  Kind cluster with 1 control-plane and 2 workers
k8s/base/                    Kubernetes manifests
policies/kyverno/            Kyverno ClusterPolicy examples
scripts/rest_api/            Python REST API integration scripts
ansible/playbooks/           Ansible pre-check and patching workflow samples
.github/workflows/           GitHub Actions CI/CD pipeline
docs/                        Detailed interview and runbook documentation
```

## Prerequisites on your laptop

Install:

- Git
- Docker Desktop and keep it running
- Kind
- kubectl
- Java 17
- Maven
- Python 3

Check:

```bash
docker version
kind version
kubectl version --client
java -version
mvn -version
python3 --version
```

## Local step-by-step execution

### Step 1: Create Kind cluster with 2 worker nodes

```bash
kind create cluster --config kind/cluster-2-workers.yaml
```

Validate:

```bash
kubectl get nodes -o wide
```

Expected:

```text
hsbc-devops-lab-control-plane   Ready
hsbc-devops-lab-worker          Ready
hsbc-devops-lab-worker2         Ready
```

### Step 2: Run JVM tests locally

```bash
cd app
mvn clean test
cd ..
```

This runs:

- JUnit tests
- Cucumber BDD tests

### Step 3: Build Docker image

```bash
docker build -t payment-api:local app
```

### Step 4: Load image into Kind

```bash
kind load docker-image payment-api:local --name hsbc-devops-lab
```

### Step 5: Deploy to Kubernetes

```bash
kubectl apply -k k8s/base
```

### Step 6: Verify deployment

```bash
kubectl rollout status deployment/payment-api -n hsbc-demo
kubectl get pods -n hsbc-demo -o wide
kubectl get svc -n hsbc-demo
kubectl get endpoints payment-api -n hsbc-demo
```

### Step 7: Test API from laptop

Because the Kind config maps NodePort 30080 to your laptop port 8080:

```bash
curl http://localhost:8080/health
curl http://localhost:8080/api/payments/status
curl http://localhost:8080/api/payments/demo-payment-001
curl http://localhost:8080/actuator/prometheus
```

### Step 8: Run Python REST API smoke test

```bash
pip install -r scripts/rest_api/requirements.txt
APP_BASE_URL=http://localhost:8080 python3 scripts/rest_api/smoke_test.py
```

## GitHub Actions setup

Push this project to GitHub. The pipeline is in:

```text
.github/workflows/ci-cd-kind.yml
```

The pipeline does:

1. Build JVM app.
2. Run JUnit tests.
3. Run Cucumber tests.
4. Run optional ServiceNow REST API change gate.
5. Trigger optional Ansible Tower job through REST API.
6. Validate Kyverno policies.
7. Create Kind cluster with 2 worker nodes.
8. Build and load Docker image.
9. Deploy Kubernetes manifests.
10. Validate rollout.
11. Run REST API smoke test.
12. Optionally call Argo CD, Prometheus, and webhook APIs.

## Optional GitHub repository secrets

For local demo, these are optional. For real enterprise use, add them in:

```text
GitHub repository -> Settings -> Secrets and variables -> Actions
```

Secrets:

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

## Interview summary

You can explain this project like this:

> I built a GitHub Actions based CI/CD workflow without Jenkins. It builds a JVM Spring Boot API, runs JUnit and Cucumber tests, validates policy-as-code using Kyverno, creates a Kind Kubernetes cluster with two worker nodes, deploys the application, validates rollout, and runs REST API smoke tests. The pipeline also includes REST API integration examples for ServiceNow change gate, Ansible Tower job launch, Argo CD sync, Prometheus metric validation, and Teams/Slack notification. This matches DevSecOps, SOX control, and third-party tool integration expectations.

