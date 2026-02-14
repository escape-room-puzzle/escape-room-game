# test_escape_room.py
import unittest
import escape_room_student as student


# -----------------------------
# Puzzle 1: Laser Path Simulation Tests
# -----------------------------
class TestLaserPath(unittest.TestCase):
    def test_in_bounds_true(self):
        self.assertTrue(student.in_bounds(0, 0))
        self.assertTrue(student.in_bounds(student.GRID_WIDTH - 1, student.GRID_HEIGHT - 1))
        self.assertTrue(student.in_bounds(5, 5))

    def test_in_bounds_false(self):
        self.assertFalse(student.in_bounds(-1, 0))
        self.assertFalse(student.in_bounds(0, -1))
        self.assertFalse(student.in_bounds(student.GRID_WIDTH, 0))
        self.assertFalse(student.in_bounds(0, student.GRID_HEIGHT))

    def test_hits_laser_true(self):
        self.assertTrue(student.hits_laser(2, 2))
        self.assertTrue(student.hits_laser(2, 4))
        self.assertTrue(student.hits_laser(5, 7))
        self.assertTrue(student.hits_laser(8, 7))

    def test_hits_laser_false(self):
        self.assertFalse(student.hits_laser(0, 0))
        self.assertFalse(student.hits_laser(9, 9))
        self.assertFalse(student.hits_laser(4, 7))

    def test_hits_laser_out_of_bounds(self):
        # Out of bounds should NOT crash; expected False
        self.assertFalse(student.hits_laser(-1, 0))
        self.assertFalse(student.hits_laser(0, -1))
        self.assertFalse(student.hits_laser(student.GRID_WIDTH, 0))
        self.assertFalse(student.hits_laser(0, student.GRID_HEIGHT))

    def test_apply_move(self):
        self.assertEqual(student.apply_move(0, 0, "U"), (0, 1))
        self.assertEqual(student.apply_move(0, 0, "R"), (1, 0))
        self.assertEqual(student.apply_move(5, 5, "D"), (5, 4))
        self.assertEqual(student.apply_move(5, 5, "L"), (4, 5))

    def test_apply_move_invalid(self):
        # If invalid move, we expect "no change"
        self.assertEqual(student.apply_move(3, 3, "X"), (3, 3))
        self.assertEqual(student.apply_move(3, 3, ""), (3, 3))

    def test_simulate_path_out_of_bounds(self):
        self.assertEqual(student.simulate_path("L"), "OUT")
        self.assertEqual(student.simulate_path("D"), "OUT")
        self.assertEqual(student.simulate_path("UUUUUUUUUU"), "OUT")  # 10 ups from y=0 goes out

    def test_simulate_path_hits_laser(self):
        # Hits (2,2) after RRUU
        self.assertEqual(student.simulate_path("RRUU"), "LASER")
        # Hits (2,3) after RRUUU
        self.assertEqual(student.simulate_path("RRUUU"), "LASER")

    def test_simulate_path_reaches_goal_exact(self):
        moves = "R" * 9 + "U" * 9
        self.assertEqual(student.simulate_path(moves), "GOAL")

    def test_simulate_path_reaches_goal_early(self):
        # Custom goal reached before moves end
        moves = "RRRRLLLL"
        self.assertEqual(student.simulate_path(moves, start=(0, 0), goal=(4, 0)), "GOAL")

    def test_simulate_path_safe_but_not_goal(self):
        self.assertEqual(student.simulate_path("RU"), "OK")
        self.assertEqual(student.simulate_path("RRR"), "OK")

    def test_simulate_path_custom_start_goal(self):
        self.assertEqual(student.simulate_path("RR", start=(0, 0), goal=(2, 0)), "GOAL")
        self.assertEqual(student.simulate_path("UUU", start=(2, 2), goal=(2, 5)), "GOAL")


# -----------------------------
# Puzzle 2: Caesar Cipher Tests
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
        self.assertEqual(student.shift_char_back_3(":"), ":")

    def test_caesar_decode_basic(self):
        self.assertEqual(student.caesar_decode("Khoor"), "Hello")
        self.assertEqual(student.caesar_decode("Zruog!"), "World!")
        self.assertEqual(student.caesar_decode("Fdhvdu"), "Caesar")

    def test_caesar_decode_sentence(self):
        text = "Wkh nhb frgh lv: FODVVURRP"
        decoded = student.caesar_decode(text)
        self.assertIn("the key code is:", decoded.lower())
        self.assertIn("classroom", decoded.lower())


# -----------------------------
# Puzzle 3: Fibonacci Tests
# -----------------------------
class TestFibonacci(unittest.TestCase):
    def test_fibonacci_small(self):
        self.assertEqual(student.fibonacci(1), [0])
        self.assertEqual(student.fibonacci(2), [0, 1])

    def test_fibonacci_medium(self):
        self.assertEqual(student.fibonacci(6), [0, 1, 1, 2, 3, 5])

    def test_fibonacci_larger(self):
        self.assertEqual(student.fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_fibonacci_zero_or_negative(self):
        # Accept returning [] for n <= 0
        self.assertEqual(student.fibonacci(0), [])
        self.assertEqual(student.fibonacci(-3), [])


if __name__ == "__main__":
    unittest.main()
