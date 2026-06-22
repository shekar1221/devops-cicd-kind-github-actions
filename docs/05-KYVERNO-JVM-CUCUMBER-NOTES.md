# Kyverno, JVM, Cucumber, JUnit, and Selenium Awareness

## Kyverno

Kyverno is policy-as-code for Kubernetes.

In this project:

```text
policies/kyverno/require-labels.yaml
policies/kyverno/disallow-latest-image-tag.yaml
policies/kyverno/require-probes-and-resources.yaml
```

These policies check:

- Required labels
- No `latest` image tag
- Readiness probe
- Liveness probe
- CPU/memory requests and limits

Interview answer:

> Kyverno helps enforce Kubernetes governance. In a controlled BFSI environment, we can audit or block deployments that do not meet standards.

## JVM

The app is Java 17 Spring Boot.

Kubernetes JVM settings:

```yaml
JAVA_TOOL_OPTIONS: "-XX:MaxRAMPercentage=70 -XX:+ExitOnOutOfMemoryError"
```

Why important:

- JVM apps need memory tuning.
- Kubernetes memory limit should align with JVM heap behavior.
- `ExitOnOutOfMemoryError` lets Kubernetes restart unhealthy JVM pods.

Interview answer:

> For JVM apps on Kubernetes, I check memory limits, heap settings, garbage collection behavior, pod restarts, and OOMKilled events.

## JUnit

JUnit is used for technical unit/integration tests.

In this project:

```text
app/src/test/java/com/hsbc/demo/PaymentControllerTest.java
```

## Cucumber

Cucumber is used for business-readable tests.

Feature file:

```text
app/src/test/resources/features/payment_api.feature
```

Example:

```gherkin
Given the payment API is deployed
When I check the payment status API
Then the API should return available
```

Interview answer:

> JUnit validates technical behavior and Cucumber validates business-readable scenarios in Given-When-Then format.

## Selenium awareness

This project is API-only, so Selenium is not required.

How to explain:

> Selenium is mainly for browser/UI automation. If this payment API had a web UI, Selenium tests could run after deployment to validate login, payment screen, and confirmation page. Since this lab is API-only, I used REST API smoke tests and Cucumber API scenarios instead.

