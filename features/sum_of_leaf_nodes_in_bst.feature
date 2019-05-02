Feature: Solution for Sum of leaf nodes should work appropriately
  Scenario: It should work against input given in the example
    When I run `sum_of_leaf_nodes_in_bst.py` interactively
    # Number of testcases
    And I type "2"
    # Case 1
    # ======
    # Number of elements in BST
    And I type "6"
    # Elements of BST
    And I type "67 34 82 12 45 78"
    # Case 2
    # ======
    # Number of elements in BST
    And I type "1"
    # Elements of BST
    And I type "45"
    Then the output should contain:
    """
    135
    45
    """

  Scenario: The program should give error when test cases entered below 1.
    When I run `sum_of_leaf_nodes_in_bst.py` interactively
    # Number of test cases
    And I type "0"
    Then the exit status should be 1

  Scenario: The program should give error when test cases are above 1000.
    When I run `sum_of_leaf_nodes_in_bst.py` interactively
    # Number of test cases
    And I type "1001"
    Then the exit status should be 1

  Scenario: The program should give error when number of elements in BST is below 1.
    When I run `sum_of_leaf_nodes_in_bst.py` interactively
    # Number of test cases
    And I type "1"
    # Number of elements in BST
    And I type "0"
    Then the exit status should be 1

  Scenario: The program should give error when number of elements in BST is above 1000000
    When I run `sum_of_leaf_nodes_in_bst.py` interactively
    # Number of test cases
    And I type "1"
    # Number of elements in BST
    And I type "1000001"
    Then the exit status should be 1
