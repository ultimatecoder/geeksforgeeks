Feature: Solution for Count the zeros
  Scenario: The program should work against inputs given in the example
    When I run `count_the_zeros.py` interactively
    # Number of test cases
    And I type "3"
    # Case 1
    # ======
    # Length of elements
    And I type "12"
    # Elements
    And I type "1 1 1 1 1 1 1 1 1 0 0 0"
    # Case 2
    # ======
    # Length of elements
    And I type "5"
    # Elements
    And I type "0 0 0 0 0"
    # Case 3
    # ======
    And I type "6"
    # Elements
    And I type "1 1 1 1 1"
    Then the output should contain:
    """
    3
    5
    0
    """

  Scenario: The program should give when number of test cases are below 1.
    When I run `count_the_zeros.py` interactively
    # Number of test cases
    And I type "0"
    Then the exit status should be 1

  Scenario: The program should give when number of test cases are above 100.
    When I run `count_the_zeros.py` interactively
    # Number of test cases
    And I type "101"
    Then the exit status should be 1

  Scenario: The program should give when length of elements is below 1.
    When I run `count_the_zeros.py` interactively
    # Number of test cases
    And I type "1"
    # Length of elements
    And I type "0"
    Then the exit status should be 1

  Scenario: The program should give when length of elements is below 1.
    When I run `count_the_zeros.py` interactively
    # Number of test cases
    And I type "1"
    # Length of elements
    And I type "0"
    Then the exit status should be 1

  Scenario: The program should give when length of elements is above 30.
    When I run `count_the_zeros.py` interactively
    # Number of test cases
    And I type "1"
    # Length of elements
    And I type "31"
    Then the exit status should be 1

  Scenario: The program should give when elements of the array is not zero(0) or one(1).
    When I run `count_the_zeros.py` interactively
    # Number of test cases
    And I type "1"
    # Length of elements
    And I type "12"
    # Elements
    And I type "1 1 2 1 1 1 1 1 0 0"
    Then the exit status should be 1
