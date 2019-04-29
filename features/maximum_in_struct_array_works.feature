Feature: Maximum in Struct array works
  The program Maximum in Struct array should work against given example input
  in its defintion
  Scenario: Test Maximum in Struct Array program with input given in example
    When I run `maximum_in_struct_array.py` interactively
    # Number of test cases
    And I type "2"
    # Case 1
    # =======
    # Length of feets and inches
    And I type "2"
    # Combination of feets and inches
    And I type "1221"
    # Case 2
    # ========
    # Length of feets and inches
    And I type "4"
    # Combination of feets and inches
    And I type "35795655"
    Then the output should contain:
    """
    25
    93
    """
