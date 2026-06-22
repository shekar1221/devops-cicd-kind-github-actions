# Troubleshooting Scenarios

## Scenario 1: Pod CrashLoopBackOff

Commands:

```bash
kubectl get pods -n hsbc-demo
kubectl describe pod <pod> -n hsbc-demo
kubectl logs <pod> -n hsbc-demo
kubectl logs <pod> -n hsbc-demo --previous
kubectl get events -n hsbc-demo --sort-by=.lastTimestamp
```

Possible causes:

- Wrong ConfigMap
- Missing Secret
- JVM OutOfMemory
- Application startup failure

## Scenario 2: Service endpoint empty

Commands:

```bash
kubectl describe svc payment-api -n hsbc-demo
kubectl get endpoints payment-api -n hsbc-demo
kubectl get pods -n hsbc-demo --show-labels
```

Root cause:

```text
Service selector does not match pod labels, or pods are not ready.
```

Interview answer:

> Service endpoint empty usually means the Service cannot find ready pods. I check selector, pod labels, namespace, and readiness probe.

## Scenario 3: API not reachable from laptop

Check:

```bash
kubectl get svc -n hsbc-demo
kubectl get nodes
docker ps
curl http://localhost:8080/health
```

Root cause:

```text
Kind port mapping or NodePort not configured correctly.
```

## Scenario 4: JVM pod OOMKilled

Commands:

```bash
kubectl describe pod <pod> -n hsbc-demo
kubectl top pod -n hsbc-demo
kubectl logs <pod> -n hsbc-demo --previous
```

Root cause examples:

- Memory limit too low
- Heap too high
- Memory leak

Fix:

- Tune `JAVA_TOOL_OPTIONS`
- Increase memory limit after approval
- Ask development team to check memory leak

## Scenario 5: Policy failure

If Kyverno is enforcing instead of auditing, deployment can fail when:

- Labels are missing
- Probes are missing
- Resources are missing
- Image uses `latest`

Interview answer:

> Policy failure is good in DevSecOps because it catches risky manifests before production.

