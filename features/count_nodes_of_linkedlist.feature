Feature: Count nodes of Linkedlist works
  Count nodes of Linkedlist giving correct results
  Scenario: It should work against inputs given in the example
    When I run `count_nodes_of_linkedlist.py` interactively
    # Number of test cases
    And I type "2"
    # Case 1
    # ======
    # Length of the data
    And I type "5"
    # Data for linkedlist
    And I type "1 2 3 4 5"
    # Case 2
    # ======
    # Length of the data
    And I type "7"
    # Data for linkedlist
    And I type "2 4 6 7 5 1 0"
    Then the output should contain:
    """
    5
    7
    """
