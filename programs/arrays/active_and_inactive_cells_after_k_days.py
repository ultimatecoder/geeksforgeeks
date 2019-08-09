"""
Problem

    Given a binary array of size n where n > 3. Possible value of cell can be
    active or in-active. An active cell is the one which has 1 as a value.
    In-active cell has 0 as a value.  After every day, status of i’th cell
    becomes active if left and right cells are not same and inactive if left
    and right cell are same (both 0 or both 1).

    Since there are no cells before leftmost and after rightmost cells, the
    value cells before leftmost and after rightmost cells is always considered
    as 0 (or inactive).

    Given a number k, the task is to find state of cell after k days.

    Note

        For calculating state for next day, take value of state of previous day
        as a reference.

Examples - 1

    Input

        state = [1, 0, 1, 1], days = 2

    Output

        [0, 1, 1, 1]

    Explanation

        After 1 day,

            [0, 0, 1, 1]

        After 2 day,

            [0, 1, 1, 1]

Examples - 2

    Input

        state = [0, 1, 0, 1, 0, 1, 0, 1], days = 3

    Output

        [1, 0, 1, 0, 0, 0, 0, 0]

    Explanation

        After 1 day,

            [1, 0, 0, 0, 0, 0, 0, 0]

        After 2 day,

            [0, 1, 0, 0, 0, 0, 0, 0]

        After 3 day,

            [1, 0, 1, 0, 0, 0, 0, 0]
"""

def _compute_state_of_cell(state, index):
    left_index = index - 1
    if left_index < 0:
        left_cell = 0
    else:
        left_cell = state[left_index]

    try:
        right_cell = state[index + 1]
    except IndexError:
        right_cell = 0
    if left_cell == right_cell:
        return 0
    else:
        return 1


def _compute_state_for_next_day(state):
    new_state = state[:]
    for index in range(len(state)):
        new_state[index] = _compute_state_of_cell(state, index)
    return new_state


def calculate_state(initial_state, days):
    """Calculates state from initial state after K days

    This method computes state of initial cells after iterating K number of
    days.
    """
    for day in range(days):
        initial_state = _compute_state_for_next_day(initial_state)
    return initial_state
