Feature: Reverse first K elements of Queue

  Scenario: The program should work against sample input given in example
    When I run `reverse_first_k_elements_of_queue.py` interactively
    # Number of Testcases
    And I type "1"
    # N K
    # 5 = Number of elements. Value of N in the example.
    # 3 = Number of elements to be reversed. Value of K in the example.
    And I type "5 3"
    # Elements of the queue
    And I type "1 2 3 4 5"
    Then the output should contain:
    """
    3 2 1 4 5
    """

  Scenario: The program should work when more than one test cases are given
    When I run `reverse_first_k_elements_of_queue.py` interactively
    # Number of Testcases
    And I type "2"
    # Case 1
    # =======
    # N K
    # N = number of elements
    # K = elements to reverse
    And I type "3 1"
    # Elements
    And I type "4 5 6"
    # Case 2
    # ======
    # N K
    # N = number of elements
    # K = elements to reverse
    And I type "5 2"
    # Elements
    And I type "5 4 3 2 1"
    Then the output should contain:
    """
    4 5 6
    4 5 3 2 1
    """
