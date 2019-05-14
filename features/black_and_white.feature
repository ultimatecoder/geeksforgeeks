Feature: Solution for Black and White

  Scenario: The program should work against inputs given in example
    When I run `black_and_white.py` interactively
    # Number of test cases
    And I type "3"
    # Case 1
    # ======
    # N M
    # N = Rows of Matrix
    # M = Columns of Matrix
    And I type "2 2"
    # Case 2
    # ======
    # N M
    # N = Rows of Matrix
    # M = Columns of Matrix
    And I type "2 3"
    # Case 3
    # ======
    # N M
    # N = Rows of Matrix
    # M = Colums of Matrix
    And I type "4 5"
    Then the output should contain:
    """
    12
    26
    312
    """

  Scenario: The program should give error when number of test cases are below 1.
    When I run `black_and_white.py` interactively
    # Number of Test cases
    And I type "0"
    Then the exit status should be 1

  Scenario: The program should give error when number of test cases are above 100.
    When I run `black_and_white.py` interactively
    # Number of test cases
    And I type "101"
    Then the exit status should be 1

  Scenario: The program should give error when the value of rows and columns are below 0.
    When I run `black_and_white.py` interactively
    # Number of test cases
    And I type "1"
    # N M
    # N = Number of rows
    # M = Number of columns
    And I type "0 0"
    Then the exit status should be 1

  Scenario: The program should give error when the value of rows and columns are above 1000000.
    When I run `black_and_white.py` interactively
    # Number of test cases
    And I type "1"
    # N M
    # N = Number of rows
    # M = Number of columns
    And I type "1000001 1000001"
    Then the exit status should be 1
