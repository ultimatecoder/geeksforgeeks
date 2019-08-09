import unittest

from arrays.active_and_inactive_cells_after_k_days import calculate_state


class TestCalcualteState(unittest.TestCase):

    def test_calcualte_state(self):
        sample_inputs_and_expected_answer = (
            ([1, 0, 1, 1,], 2, [0, 1, 1, 1]),
            ([0, 1, 0, 1, 0, 1, 0, 1], 3, [1, 0, 1, 0, 0, 0, 0, 0]),
            ([], 3, []),
            ([1, 1, 1], 1, [1, 0, 1])
        )
        for initial_state, days, expected_answer in (
            sample_inputs_and_expected_answer
        ):
            with self.subTest(
                initial_state=initial_state,
                days=days,
                expected_answer=expected_answer
            ):
                self.assertListEqual(
                    calculate_state(initial_state, days),
                    expected_answer
                )
