Feature: Solution for C++ Generic sort

  Scenario: The program should work against inputs given in the example
    When I run `c++_generic_sort.py` interactively
    # Number of test cases
    And I type "3"
    # Case 1
    # =======
    # N Q
    # N = Length of elements
    # Q = Data type of elements.
    #   1 = All the elements are integer
    #   2 = All the elements are string
    #   3 = All the elements are floating type
    And I type "3 3"
    # Elements of array
    And I type "34.23 -4.35 3.4"
    # Case 2
    # =======
    # N Q
    # N = Length of elements
    # Q = Data type of elements.
    #   1 = All the elements are integer
    #   2 = All the elements are string
    #   3 = All the elements are floating type
    And I type "4 1"
    # Elements of array
    And I type "123 -2311 837 0"
    # Case 3
    # =======
    # N Q
    # N = Length of elements
    # Q = Data type of elements.
    #   1 = All the elements are integer
    #   2 = All the elements are string
    #   3 = All the elements are floating type
    And I type "5 2"
    # Elements of array
    And I type "focus on challenges in implementing"
    Then the output should contain:
    """
    -4.35 3.4 34.23
    -2311 0 123 837
    challenges focus implementing in on
    """

  Scenario: The program should give error when the test cases are entered below 1.
    When I run `c++_generic_sort.py` interactively
    # Number of test cases
    And I type "0"
    Then the exit status should be 1

  Scenario: The program should give error when the test cases are entered above 50.
    When I run `c++_generic_sort.py` interactively
    # Number of test cases
    And I type "51"
    Then the exit status should be 1

  Scenario: The program should give error when number of elements are entered below 1.
    When I run `c++_generic_sort.py` interactively
    # Number of test cases
    And I type "1"
    # N Q
    # N = Length of elements
    # Q = Data type of elements.
    #   1 = All the elements are integer
    #   2 = All the elements are string
    #   3 = All the elements are floating type
    And I type "0 1"
    Then the exit status should be 1

  Scenario: The program should give error when number of elements are entered above 100.
    When I run `c++_generic_sort.py` interactively
    # Number of test cases
    And I type "1"
    # N Q
    # N = Length of elements
    # Q = Data type of elements.
    #   1 = All the elements are integer
    #   2 = All the elements are string
    #   3 = All the elements are floating type
    And I type "101 1"
    Then the exit status should be 1

  Scenario: The program should give error when data type choice is out of choices.
    When I run `c++_generic_sort.py` interactively
    # Number of test cases
    And I type "1"
    # N Q
    # N = Length of elements
    # Q = Data type of elements.
    #   1 = All the elements are integer
    #   2 = All the elements are string
    #   3 = All the elements are floating type
    And I type "10 -1"
    Then the exit status should be 1

  Scenario: The program should give error when data type choice is out of choices.
    When I run `c++_generic_sort.py` interactively
    # Number of test cases
    And I type "1"
    # N Q
    # N = Length of elements
    # Q = Data type of elements.
    #   1 = All the elements are integer
    #   2 = All the elements are string
    #   3 = All the elements are floating type
    And I type "10 23"
    Then the exit status should be 1
