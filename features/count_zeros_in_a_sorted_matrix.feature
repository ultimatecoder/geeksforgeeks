Feature: Solution for Count zeros in a sorted matrix

  Scenario: The program should work correctly against given input in example
    When I run `count_zeros_in_a_sorted_matrix.py` interactively
    # Number of test cases
    And I type "1"
    # M N
    # M = Length of column in a Matrix
    # N = Length of rows in a Matrix
    And I type "3 3"
    # Elements of Matrix
    And I type "0 0 0 0 0 1 0 1 1"
    Then the output should contain:
    """
    6
    """

  Scenario: The program should work when more than two test cases are given.
    When I run `count_zeros_in_a_sorted_matrix.py` interactively
    # Number of test cases
    And I type "2"
    # Case 1
    # =======
    # M N
    # M = Length of columns in a Matrix
    # N = Length of rows in a Matrix
    And I type "3 4"
    # Elements
    And I type "0 0 1 1 1 1 1 1 1 1 1 1"
    # Case 2
    # ======
    # M N
    # M = Length of columns in a Matrix
    # N = Length of rows in a Matrix
    And I type "3 3"
    # Elements
    And I type "0 0 0 0 0 0 0 0 1"
    Then the output should contain:
    """
    2
    8
    """

  Scenario: The program should give error when number of test cases are entered below 1.
    When I run `count_zeros_in_a_sorted_matrix.py` interactively
    # Number of test cases
    And I type "0"
    Then the exit status should be 1

  Scenario: The program should give error when number of test cases are entered above 50.
    When I run `count_zeros_in_a_sorted_matrix.py` interactively
    # Number of test cases
    And I type "51"
    Then the exit status should be 1

  Scenario: The program should give error when the value of column is below 1.
    When I run `count_zeros_in_a_sorted_matrix.py` interactively
    # Number of test cases
    And I type "1"
    # M N
    # M = Length of columns in a Matrix
    # N = Length of rows in a Matrix
    And I type "0 2"
    Then the exit status should be 1

  Scenario: The program should give error when the value of column is above 50.
    When I run `count_zeros_in_a_sorted_matrix.py` interactively
    # Number of test cases
    And I type "1"
    # M N
    # M = Length of columns in a Matrix
    # N = Length of rows in a Matrix
    And I type "51 2"
    Then the exit status should be 1

  Scenario: The program should give error when the value of row is below 1.
    When I run `count_zeros_in_a_sorted_matrix.py` interactively
    # Number of test cases
    And I type "1"
    # M N
    # M = Length of columns in a Matrix
    # N = Length of rows in a Matrix
    And I type "2 0"
    Then the exit status should be 1

  Scenario: The program should give error when the value of row is below 1.
    When I run `count_zeros_in_a_sorted_matrix.py` interactively
    # Number of test cases
    And I type "1"
    # M N
    # M = Length of columns in a Matrix
    # N = Length of rows in a Matrix
    And I type "2 0"
    Then the exit status should be 1

  Scenario: The program should give error when the value of row is above 50.
    When I run `count_zeros_in_a_sorted_matrix.py` interactively
    # Number of test cases
    And I type "1"
    # M N
    # M = Length of columns in a Matrix
    # N = Length of rows in a Matrix
    And I type "2 0"
    Then the exit status should be 1

  Scenario: The program should give error when Matrix elements are not 0 or 1.
    When I run `count_zeros_in_a_sorted_matrix.py` interactively
    # Number of test cases
    And I type "1"
    # M N
    # M = Length of columns in a Matrix
    # N = Length of rows in a Matrix
    And I type "2 2"
    # Elements
    And I type "0 1 2 2"
    Then the exit status should be 1
