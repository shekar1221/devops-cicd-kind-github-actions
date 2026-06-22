package com.hsbc.demo;

import java.time.Instant;
import java.util.Map;
import java.util.UUID;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PaymentController {

    @Value("${app.environment:local}")
    private String environment;

    @Value("${app.release:dev}")
    private String release;

    @Value("${db.host:payments-db}")
    private String dbHost;

    @GetMapping("/health")
    public Map<String, Object> health() {
        return Map.of(
                "status", "UP",
                "service", "payment-api",
                "environment", environment,
                "release", release,
                "timestamp", Instant.now().toString()
        );
    }

    @GetMapping("/api/payments/status")
    public Map<String, Object> paymentStatus() {
        return Map.of(
                "status", "AVAILABLE",
                "message", "Payment service is ready",
                "environment", environment
        );
    }

    @GetMapping("/api/payments/{paymentId}")
    public Map<String, Object> getPayment(@PathVariable String paymentId) {
        return Map.of(
                "paymentId", paymentId,
                "state", "AUTHORIZED",
                "currency", "INR",
                "amount", 1000,
                "traceId", UUID.randomUUID().toString()
        );
    }

    @PostMapping("/api/payments")
    @ResponseStatus(HttpStatus.CREATED)
    public Map<String, Object> createPayment(@RequestBody Map<String, Object> request) {
        return Map.of(
                "paymentId", UUID.randomUUID().toString(),
                "state", "CREATED",
                "received", request,
                "traceId", UUID.randomUUID().toString()
        );
    }

    @GetMapping("/api/admin/config")
    public Map<String, Object> config() {
        return Map.of(
                "environment", environment,
                "release", release,
                "dbHost", dbHost,
                "password", "****"
        );
    }
}
