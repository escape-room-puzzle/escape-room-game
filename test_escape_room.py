import unittest
import escape_room_student as student


# -----------------------------
# Laser Path Simulation Tests
# -----------------------------
class TestLaserPath(unittest.TestCase):
    def test_in_bounds(self):
        self.assertTrue(student.in_bounds(0, 0))
        self.assertTrue(student.in_bounds(student.GRID_WIDTH - 1, student.GRID_HEIGHT - 1))
        self.assertFalse(student.in_bounds(-1, 0))
        self.assertFalse(student.in_bounds(0, -1))
        self.assertFalse(student.in_bounds(student.GRID_WIDTH, 0))
        self.assertFalse(student.in_bounds(0, student.GRID_HEIGHT))

    def test_hits_laser(self):
        self.assertTrue(student.hits_laser(2, 2))
        self.assertTrue(student.hits_laser(8, 7))
        self.assertFalse(student.hits_laser(0, 0))
        self.assertFalse(student.hits_laser(9, 9))

    def test_apply_move(self):
        self.assertEqual(student.apply_move(0, 0, "U"), (0, 1))
        self.assertEqual(student.apply_move(0, 0, "R"), (1, 0))
        self.assertEqual(student.apply_move(5, 5, "D"), (5, 4))
        self.assertEqual(student.apply_move(5, 5, "L"), (4, 5))

    def test_simulate_path_out_of_bounds(self):
        # starting at (0,0), moving left goes out
        self.assertEqual(student.simulate_path("L"), "OUT")
        # moving down goes out
        self.assertEqual(student.simulate_path("D"), "OUT")

    def test_simulate_path_hits_laser(self):
        # One path that hits (2,2): R,R,U,U
        self.assertEqual(student.simulate_path("RRUU"), "LASER")

    def test_simulate_path_reaches_goal_exact(self):
        # Straight to goal: 9 rights then 9 ups
        moves = "R" * 9 + "U" * 9
        self.assertEqual(student.simulate_path(moves), "GOAL")

    def test_simulate_path_safe_but_not_goal(self):
        # A small safe path that doesn't reach goal
        self.assertEqual(student.simulate_path("RU"), "OK")

    def test_simulate_path_stops_when_goal_reached(self):
        # If goal is reached early, should return GOAL even if moves remain
        moves = "R" * 9 + "U" * 9 + "LLLL"
        self.assertEqual(student.simulate_path(moves), "GOAL")

    def test_simulate_path_custom_start_goal(self):
        # custom mini-goal
        self.assertEqual(student.simulate_path("RR", start=(0, 0), goal=(2, 0)), "GOAL")


# -----------------------------
# Caesar Cipher Tests
# -----------------------------
class TestCaesarCipher(unittest.TestCase):
    def test_shift_char_back_3_upper(self):
        self.assertEqual(student.shift_char_back_3("D"), "A")
        self.assertEqual(student.shift_char_back_3("A"), "X")
        self.assertEqual(student.shift_char_back_3("C"), "Z")

    def test_shift_char_back_3_lower(self):
        self.assertEqual(student.shift_char_back_3("d"), "a")
        self.assertEqual(student.shift_char_back_3("b"), "y")
        self.assertEqual(student.shift_char_back_3("a"), "x")

    def test_shift_char_back_3_non_letter(self):
        self.assertEqual(student.shift_char_back_3("!"), "!")
        self.assertEqual(student.shift_char_back_3(" "), " ")
        self.assertEqual(student.shift_char_back_3("5"), "5")

    def test_caesar_decode_basic(self):
        self.assertEqual(student.caesar_decode("Khoor"), "Hello")
        self.assertEqual(student.caesar_decode("Zruog!"), "World!")
        self.assertEqual(student.caesar_decode("Fdhvdu"), "Caesar")

    def test_caesar_decode_mixed(self):
        text = "Wkh nhb frgh lv: FODVVURRP"
        decoded = student.caesar_decode(text)
        self.assertIn("the key code is:", decoded.lower())
        self.assertIn("classroom", decoded.lower())


# -----------------------------
# Fibonacci Missing Number Tests
# -----------------------------
class TestFibonacciMissing(unittest.TestCase):
    def test_is_fibonacci_sequence_true(self):
        self.assertTrue(student.is_fibonacci_sequence([0, 1, 1, 2, 3, 5]))
        self.assertTrue(student.is_fibonacci_sequence([2, 3, 5, 8, 13]))
        self.assertTrue(student.is_fibonacci_sequence([0, 1]))  # short list ok
        self.assertTrue(student.is_fibonacci_sequence([7]))     # short list ok

    def test_is_fibonacci_sequence_false(self):
        self.assertFalse(student.is_fibonacci_sequence([0, 1, 2, 3, 5]))
        self.assertFalse(student.is_fibonacci_sequence([1, 1, 3, 4]))

    def test_find_missing_middle(self):
        self.assertEqual(student.find_missing_fibonacci([0, 1, None, 2, 3, 5]), 1)
        self.assertEqual(student.find_missing_fibonacci([0, 1, 1, 2, None, 5, 8]), 3)
        self.assertEqual(student.find_missing_fibonacci([2, 3, 5, None, 13, 21]), 8)

    def test_find_missing_first(self):
        self.assertEqual(student.find_missing_fibonacci([None, 1, 1, 2, 3, 5]), 0)
        self.assertEqual(student.find_missing_fibonacci([None, 3, 5, 8, 13]), 2)

    def test_find_missing_second(self):
        self.assertEqual(student.find_missing_fibonacci([0, None, 1, 2, 3, 5]), 1)
        self.assertEqual(student.find_missing_fibonacci([2, None, 5, 8, 13]), 3)

    def test_find_missing_last(self):
        self.assertEqual(student.find_missing_fibonacci([0, 1, 1, 2, 3, None]), 5)
        self.assertEqual(student.find_missing_fibonacci([2, 3, 5, 8, 13, None]), 21)


if __name__ == "__main__":
    unittest.main()
