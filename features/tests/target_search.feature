
Feature: Tests for search

  Scenario: User can search for a tea on Target
    Given Open Target main page
    When Search for tea
    Then Search results for tea are shown

  Scenario: User can search for a book on Target
    Given Open Target main page
#    When Search for tea
#    Then Search results for tea are shown

  Scenario Outline: User can search for a product
    Given Open Target main page
    When Search for <product>
    Then Search results for <product_result> are shown

    Examples:
    |product  |product_result|
    |tea      |tea           |
    |mug      |mug           |
    |coffee   |coffee        |