Feature: Queue Operations works on given input
  Scenario: Queue Operations should work on inputs given in the example
    When I run `queue_operations.py` interactively
    # Number of test cases
    And I type "1"
    # Length of elements
    And I type "8"
    # Elements
    And I type "1 2 3 4 5 2 3 1"
    # Length of elements to find frequency for
    And I type "5"
    # Elements whose their frequency will be funded
    And I type "1 3 2 9 10"
    Then the output should contain:
    """
    2
    2
    2
    -1
    -1
    """

  Scenario: Queue Operations should work when multiple inputs are given
    When I run `queue_operations.py` interactively
    # Number of Test cases
    And I type "2"
    # Case 1
    # =======
    # Length of elements
    And I type "3"
    # Elements
    And I type "4 5 2"
    # Length of elements for which their frequencies will be find
    And I type "2"
    # Elements whose frequencies will be founded
    And I type "10 2"
    # Case 2
    # ======
    # Length of elements
    And I type "5"
    # Elements
    And I type "1 2 3 4 6"
    # Length of elements whose frequencies will be founded
    And I type "1"
    # Elements whose frequencies will be founded
    And I type "3"
    Then the output should contain:
    """
    -1
    1
    1
    """
