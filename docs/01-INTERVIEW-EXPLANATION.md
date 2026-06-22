# Interview Explanation - HSBC JD Mapping

## 1. How this project maps to the JD

| JD requirement | Project implementation |
|---|---|
| Linux | Ansible pre-check and patching workflow samples |
| Ansible Automation | `ansible/playbooks/` and Ansible Tower REST API script |
| Python | REST API integration scripts |
| REST APIs | ServiceNow, Tower, Argo CD, Prometheus, webhook, app smoke tests |
| CI/CD | GitHub Actions workflow |
| DevSecOps | Tests, policy-as-code, change gate, validation |
| GitHub | Branch/PR based workflow |
| JUnit | `PaymentControllerTest.java` |
| Cucumber | `payment_api.feature` and step definitions |
| Kubernetes | Kind cluster, Deployment, Service, ConfigMap, Secret |
| Prometheus/Grafana | Actuator Prometheus endpoint and scrape annotations |
| SOX controls | Change gate, audit-friendly pipeline, evidence artifacts |
| RDBMS awareness | ConfigMap/Secret DB values and docs |
| Hadoop awareness | Documented separately as operational awareness |

## 2. Best interview answer

Say:

> I created a GitHub Actions CI/CD pipeline for a JVM-based payment API. The pipeline builds the code, runs JUnit and Cucumber tests, validates Kubernetes manifests, checks Kyverno policies, creates a Kind cluster with two worker nodes, deploys the application, verifies Kubernetes rollout, and runs REST API smoke tests. I also added REST API integrations for ServiceNow change approval, Ansible Tower job launch, Argo CD sync, Prometheus metric validation, and webhook notifications. This demonstrates end-to-end DevOps automation without Jenkins.

## 3. How to explain REST API integration

Say:

> REST APIs are used in the pipeline to connect third-party tools. For example, GitHub Actions can call ServiceNow API to validate whether a production change is approved, Ansible Tower API to trigger pre-check or post-check automation, Argo CD API to sync Kubernetes applications, Prometheus API to validate post-deployment metrics, and webhook API to notify support teams. For simple calls we can use curl, and for advanced logic we can use Python requests.

## 4. How to explain SOX/compliance

Say:

> In a BFSI environment, production deployment should not happen directly. The pipeline should check change approval, run quality gates, validate security/policy controls, deploy in a controlled way, verify health, and produce evidence. This supports SOX-style controls such as approval, audit trail, segregation of duties, rollback plan, and validation evidence.

## 5. How to explain JVM part

Say:

> The application is a Java Spring Boot service running on Java 17. In Kubernetes, I configured JVM options using `JAVA_TOOL_OPTIONS`, memory requests and limits, readiness and liveness probes, and actuator endpoints for health and Prometheus metrics. This is important because JVM apps can face memory pressure, garbage collection issues, or OutOfMemory errors if resources are not tuned.

## 6. How to explain Cucumber and JUnit

Say:

> JUnit validates technical unit or integration behavior. Cucumber validates business-readable scenarios using Given-When-Then format. In this project, JUnit checks API endpoints and Cucumber validates that the payment API is deployed and returns available status. In real CI/CD, these tests become quality gates before deployment.

## 7. How to explain Kyverno

Say:

> Kyverno is Kubernetes policy-as-code. It helps enforce standards like required labels, no latest image tag, probes, and resource limits. In BFSI, this supports security and governance because risky manifests can be blocked or audited before reaching production.

