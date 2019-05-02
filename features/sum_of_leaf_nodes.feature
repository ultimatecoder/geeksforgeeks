Feature: Sum of Leaf Nodes
  Solution for Sum of Leaf Nodes should work
  Scenario: Should work against inputs given in the example
    When I run `sum_of_leaf_nodes.py` interactively
    # Number of Test cases
    And I type "2"
    # Case 1
    # ========
    # Number of edges between two nodes
    And I type "2"
    # a b (L or R)
    # a = Parent node
    # b = Child node
    # L = Node b is left of a
    # R = Node b is right of a
    # In below case
    #         1
    #       2   3
    And I type "1 2 L 1 3 R"
    # Case 2
    # ======
    # Number of edges between two nodes
    And I type "5"
    # a b (L or R)
    # a = Parent node
    # b = Child node
    # L = Node b is left of a
    # R = Node b is right of a
    # In below case
    #             10
    #         20        30
    #      40    60  90
    And I type "10 20 L 10 30 R 20 40 L 20 60 R 30 90 L"
    Then the output should contain:
    """
    5
    190
    """

  Scenario: When Number of test cases are above 100, the program should generate error
    When I run `sum_of_leaf_nodes.py` interactively
    # Number of test cases
    And I type "101"
    Then the exit status should be 1

  Scenario: When Number of test cases are below 1, the program should generate error
    When I run `sum_of_leaf_nodes.py` interactively
    # Number of test cases
    And I type "0"
    Then the exit status should be 1

  Scenario: When Length of pairs are above 1000 the program should generate error
    When I run `sum_of_leaf_nodes.py` interactively
    # Number of test cases
    And I type "1"
    # Length of pairs
    And I type "1001"
    Then the exit status should be 1

  Scenario: When length of pairs are below 1 the program should generate error
    When I run `sum_of_leaf_nodes.py` interactively
    # Number of test cases
    And I type "1"
    # Length of pairs
    And I type "0"
    Then the exit status should be 1
