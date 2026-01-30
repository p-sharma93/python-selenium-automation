# Created by priyankasharma at 1/29/26
Feature: Target - Cart and Sign In

  Scenario: Cart is empty for logged out user
    Given open target main page
    When Click on cart icon
    Then Should see "Your cart is empty"


  Scenario: Logged out user can navigate to Sign In
    When Click Sign In
    Then From the right side navigation menu click Sign In
    Then I should see the Sign In form
