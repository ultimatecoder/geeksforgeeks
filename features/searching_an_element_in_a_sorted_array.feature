Feature: Solution for Searching an element in a sorted array
  Scenario: It should work against input given in example
    When I run `searching_an_element_in_a_sorted_array.py` interactively
    # Number of test cases
    And I type "2"
    # Case 1
    # =======
    # N K
    # N = Length of elements
    # K = Element to find in the given elements
    And I type "5 6"
    # Elements
    And I type "1 2 3 4 6"
    # Case 2
    # ======
    # N K
    # N = Length of elements
    # K = Elements to find in the given elements
    And I type "5 2"
    # Elements
    And I type "1 3 4 5 6"
    Then the output should contain:
    """
    1
    -1
    """

  Scenario: It should give an error when number of test cases are below 1.
    When I run `searching_an_element_in_a_sorted_array.py` interactively
    # Number of test cases
    And I type "0"
    Then the exit status should be 1

  Scenario: It should give error when number of test cases are above 100.
    When I run `searching_an_element_in_a_sorted_array.py` interactively
    # Number of test cases
    And I type "101"
    Then the exit status should be 1

  Scenario: It should give error when length of elements are entered below 1.
    When I run `searching_an_element_in_a_sorted_array.py` interactively
    # Number of test cases
    And I type "1"
    # N K
    # N = length of elements
    # K = element to be find in elements
    And I type "0 5"
    Then the exit status should be 1

  Scenario: It should give error when length of elements are entered above 10000000.
    When I run `searching_an_element_in_a_sorted_array.py` interactively
    # Number of test cases
    And I type "1"
    # N K
    # N = length of elements
    # K = element to be find in elements
    And I type "10000001 5"
    Then the exit status should be 1

  Scenario: It should give error when the element to be find is below 1.
    When I run `searching_an_element_in_a_sorted_array.py` interactively
    # Number of test cases
    And I type "1"
    # N K
    # N = length of elements
    # K = element to be find in elements
    And I type "2 0"
    Then the exit status should be 1

  Scenario: It should give error when the element to be find is above 10000000.
    When I run `searching_an_element_in_a_sorted_array.py` interactively
    # Number of test cases
    And I type "1"
    # N K
    # N = length of elements
    # K = element to be find in elements
    And I type "2 10000001"
    Then the exit status should be 1

  Scenario: It should give error when the element of the array is below 1.
    When I run `searching_an_element_in_a_sorted_array.py` interactively
    # Number of test cases
    And I type "1"
    # N K
    # N = length of elements
    # K = element to be find in elements
    And I type "2 4"
    # Elements
    And I type "-1 0 1 2 3"
    Then the exit status should be 1

  Scenario: It should give error when the element of the array is below 10000000
    When I run `searching_an_element_in_a_sorted_array.py` interactively
    # Number of test cases
    And I type "1"
    # N K
    # N = length of elements
    # K = element to be find in elements
    And I type "2 4"
    # Elements
    And I type "1 2 3 10000001"
    Then the exit status should be 1
