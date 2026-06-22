package com.hsbc.demo;

import static org.assertj.core.api.Assertions.assertThat;

import java.util.Map;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.http.ResponseEntity;

public class PaymentStepDefinitions {

    @Autowired
    private TestRestTemplate restTemplate;

    private ResponseEntity<Map> response;

    @Given("the payment API is deployed")
    public void thePaymentApiIsDeployed() {
        response = restTemplate.getForEntity("/health", Map.class);
        assertThat(response.getStatusCode().is2xxSuccessful()).isTrue();
    }

    @When("I check the payment status API")
    public void iCheckThePaymentStatusApi() {
        response = restTemplate.getForEntity("/api/payments/status", Map.class);
    }

    @Then("the API should return available")
    public void theApiShouldReturnAvailable() {
        assertThat(response.getStatusCode().is2xxSuccessful()).isTrue();
        assertThat(response.getBody()).containsEntry("status", "AVAILABLE");
    }
}
