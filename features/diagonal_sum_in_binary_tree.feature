Feature: Solution for Diagonal Sum in Binary Tree

  Scenario: The program should work against inputs given as an example
    When I run `diagonal_sum_in_binary_tree.py` interactively
    # Number of test cases
    And I type "2"
    # Case 1
    # =======
    # Length of nodes
    And I type "3"
    # Nodes
    And I type "4 1 L 4 3 R 3 3 L"
    # Case 2
    # ======
    # Length of Nodes
    And I type "5"
    # Nodes
    And I type "10 8 L 10 2 R 8 3 L 8 3 L 8 5 R 2 2 L"
    Then the output should contain:
    """
    7 4
    12 15 3
    """

  Scenario: The program should give error when number of test cases are below 1.
    When I run `diagonal_sum_in_binary_tree.py` interactively
    # Number of test cases
    And I type "0"
    Then the exit status should be 1

  Scenario: The program should give error when number of test cases are above 100.
    When I run `diagonal_sum_in_binary_tree.py` interactively
    # Number of test cases
    And I type "101"
    Then the exit status should be 1

  Scenario: The program should give error when length of elements are below 0.
    When I run `diagonal_sum_in_binary_tree.py` interactively
    # Number of test cases
    And I type "1"
    # Length of nodes
    And I type "0"
    Then the exit status should be 1

  Scenario: The program should give error when length of elements are above 100.
    When I run `diagonal_sum_in_binary_tree.py` interactively
    # Number of test cases
    And I type "1"
    # Length of nodes
    And I type "101"
    Then the exit status should be 1
