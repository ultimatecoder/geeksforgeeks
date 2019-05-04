Feature: Add a solution of Nearly Sorted Algorithm problem
  Scenario: The program should work against input given in the example
    When I run `nearly_sorted_algorithm.py` interactively
    # Number of test cases
    And I type "2"
    # Case 1
    # =======
    # N K
    # N = Length of elements
    # K = At most K positions away from its target position 
    And I type "3 3"
    # Elements
    And I type "2 1 3"
    # Case 2
    # =======
    # N K
    # N = Length of elements
    # K = At most K positions away from its target position 
    And I type "6 3"
    # Elements
    And I type "2 6 3 12 56 8"
    Then the output should contain:
    """
    1 2 3
    2 3 6 8 12 56
    """

  Scenario: The program should give error when number of test cases are entered below 1.
    When I run `nearly_sorted_algorithm.py` interactively
    # Number of test cases
    And I type "0"
    Then the exit status should not be 0

  Scenario: The program should give error when number of test cases are entered above 100.
    When I run `nearly_sorted_algorithm.py` interactively
    # Number of test cases
    And I type "101"
    Then the exit status should not be 0

  Scenario: The program should give error when the length of elements is entered below 1.
    When I run `nearly_sorted_algorithm.py` interactively
    # Number of test cases
    And I type "1"
    # N K
    # N = Length of elements
    # K = At most k positions away from its target position 
    And I type "0 3"
    Then the exit status should not be 0

  Scenario: The program should give error when the length of elements is entered above 1
    When I run `nearly_sorted_algorithm.py` interactively
    # Number of test cases
    And I type "1"
    # N K
    # N = length of elements
    # K = At most K positions away from its target position
    And I type "101 3"
    Then the exit status should not be 0

  Scenario: The program should give error when the value of positions away from its target position is entered below 1
    When I run `nearly_sorted_algorithm.py` interactively
    # Number of test cases
    And I type "1"
    # N K
    # N = length of elements
    # K = At most K positions away from its target position
    And I type "12 0"
    Then the exit status should not be 0

  Scenario: The program should give error when the value of positions away from its target positions is entered above then length of the elements
    When I run `nearly_sorted_algorithm.py` interactively
    # Number of test cases
    And I type "1"
    # N K
    # N = length of elements
    # K = At most K positions away from its target position
    And I type "12 13"
    Then the exit status should not be 0
