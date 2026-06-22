# Local Runbook

## 1. Start Docker Desktop

On Windows, open Docker Desktop and wait until it shows running.

Validate:

```powershell
docker version
```

If you see:

```text
failed to connect to the docker API
```

Docker Desktop is not running.

## 2. Create Kind cluster

```bash
kind create cluster --config kind/cluster-2-workers.yaml
```

Validate:

```bash
kubectl get nodes -o wide
```

## 3. Build app

```bash
cd app
mvn clean test
cd ..
docker build -t payment-api:local app
```

## 4. Load image

```bash
kind load docker-image payment-api:local --name hsbc-devops-lab
```

## 5. Deploy

```bash
kubectl apply -k k8s/base
```

## 6. Validate

```bash
kubectl rollout status deployment/payment-api -n hsbc-demo
kubectl get pods -n hsbc-demo -o wide
kubectl get svc -n hsbc-demo
kubectl get endpoints payment-api -n hsbc-demo
```

## 7. Test from laptop

```bash
curl http://localhost:8080/health
curl http://localhost:8080/api/payments/status
curl http://localhost:8080/actuator/prometheus
```

## 8. Troubleshooting commands

```bash
kubectl describe pod -n hsbc-demo -l app.kubernetes.io/name=payment-api
kubectl logs -n hsbc-demo -l app.kubernetes.io/name=payment-api
kubectl get events -n hsbc-demo --sort-by=.lastTimestamp
kubectl describe svc payment-api -n hsbc-demo
kubectl get endpoints payment-api -n hsbc-demo
```

## 9. Delete lab

```bash
kind delete cluster --name hsbc-devops-lab
```

