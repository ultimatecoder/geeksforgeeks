Feature: Solution for Maximum Sum Problem
  Scenario: The program should work against inputs given as an example
    When I run `maximum_sum_problem.py` interactively
    # Number of Test cases
    And I type "2"
    # Case 1
    # ======
    # Number
    And I type "12"
    # Case 2
    # =======
    # Number
    And I type "24"
    Then the output should contain:
    """
    13
    27
    """

  Scenario: The program should give error when number of test cases are below 1
    When I run `maximum_sum_problem.py` interactively
    # Number of test cases
    And I type "0"
    Then the exit status should be 1

  Scenario: The program should give error when number of test cases are above 100
    When I run `maximum_sum_problem.py` interactively
    # Number of test cases
    And I type "101"
    Then the exit status should be 1

  Scenario: The program should give error when number entered is below 1
    When I run `maximum_sum_problem.py` interactively
    # Number of test cases
    And I type "1"
    # Number
    And I type "0"
    Then the exit status should be 1

  Scenario: The program should give error when Number entered is greater than 1000000
    When I run `maximum_sum_problem.py` interactively
    # Number of test cases
    And I type "1"
    # Number
    And I type "1000001"
    Then the exit status should be 1
