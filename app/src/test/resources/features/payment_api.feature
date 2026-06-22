Feature: Payment API smoke validation

  Scenario: Payment API status should be available
    Given the payment API is deployed
    When I check the payment status API
    Then the API should return available
