Feature: Adding a solution for Maximum difference problem
  Problem link: https://practice.geeksforgeeks.org/problems/maximum-difference/0

  Scenario: Program should give an error when number of test cases are less than 1
    When I run `maximum_difference.py` interactively
    # Number of test cases
    And I type "0"
    Then the exit status should be 1

  Scenario: Program should give an error when number of test cases are above 100
    When I run `maximum_difference.py` interactively
    # Number of test cases
    And I type "101"
    Then the exit status should be 1

  Scenario: Program should give error when number of elements in array are less than 1
    When I run `maximum_difference.py` interactively
    # Number of test cases
    And I type "1"
    # Test case 1
    # ==============
    # Elements in array
    And I type "0"
    Then the exit status should be 1

  Scenario: Program should give error when number of elements in array are greater than 10, 000, 000
    When I run `maximum_difference.py` interactively
    # Number of test cases
    And I type "1"
    # Test case 1
    # ===========
    # Elements in array
    And I type "10000001"
    Then the exit status should be 1

  Scenario: Program should give error when element in array is less than -1000000
    When I run `maximum_difference.py` interactively
    # Number of test cases
    And I type "1"
    # Test case 1
    # ===========
    # Elements in array
    And I type "3"
    # Elements
    And I type "2 -10000001 1"
    Then the exit status should be 1

  Scenario: Program should give error when element in array is greater than 1000000
    When I run `maximum_difference.py` interactively
    # Number of test cases
    And I type "1"
    # Test case 1
    # =============
    # Elements in array
    And I type "4"
    # Elements
    And I type "2 -10000001 1 0"
    Then the exit status should be 1

  Scenario: Program should work against example 1
    When I run `maximum_difference.py` interactively
    # Number of test cases
    And I type "2"
    # Test case -1
    # ============
    # Elements in first array
    And I type "7"
    # Elements
    And I type "2 3 10 6 4 8 1"
    # Test case -2
    # ============
    # Elements in second array
    And I type "6"
    # Elements
    And I type "7 9 5 6 3 2"
    Then the output should contain:
    """
    8
    2
    """
