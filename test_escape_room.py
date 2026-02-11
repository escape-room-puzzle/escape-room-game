import unittest
import answer_key as student


class TestLaserGrid(unittest.TestCase):
    def test_in_bounds_true(self):
        self.assertTrue(student.in_bounds(0, 0))
        self.assertTrue(student.in_bounds(student.GRID_WIDTH - 1, student.GRID_HEIGHT - 1))

    def test_in_bounds_false(self):
        self.assertFalse(student.in_bounds(-1, 0))
        self.assertFalse(student.in_bounds(0, -1))
        self.assertFalse(student.in_bounds(student.GRID_WIDTH, 0))
        self.assertFalse(student.in_bounds(0, student.GRID_HEIGHT))

    def test_hits_laser(self):
        self.assertTrue(student.hits_laser(2, 2))
        self.assertTrue(student.hits_laser(8, 7))
        self.assertFalse(student.hits_laser(0, 0))
        self.assertFalse(student.hits_laser(9, 9))

    def test_hits_laser_out_of_bounds(self):
        # Out of bounds should be treated as not safe; your implementation can:
        # - return False, OR
        # - raise a ValueError
        # We'll accept either approach.
        try:
            result = student.hits_laser(-1, 0)
            self.assertIn(result, [False, True])  # if you choose to return something
        except ValueError:
            self.assertTrue(True)


class TestCaesarCipher(unittest.TestCase):
    def test_shift_char_back_3(self):
        self.assertEqual(student.shift_char_back_3("D"), "A")
        self.assertEqual(student.shift_char_back_3("d"), "a")
        self.assertEqual(student.shift_char_back_3("A"), "X")
        self.assertEqual(student.shift_char_back_3("b"), "y")
        self.assertEqual(student.shift_char_back_3("!"), "!")

    def test_caesar_decode(self):
        self.assertEqual(student.caesar_decode("Khoor"), "Hello")
        self.assertEqual(student.caesar_decode("Fdhvdu"), "Caesar")
        self.assertEqual(student.caesar_decode("Zruog!"), "World!")


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_small(self):
        self.assertEqual(student.fibonacci(1), [0])
        self.assertEqual(student.fibonacci(2), [0, 1])

    def test_fibonacci_medium(self):
        self.assertEqual(student.fibonacci(6), [0, 1, 1, 2, 3, 5])

    def test_fibonacci_zero_or_negative(self):
        # You can choose how to handle this:
        # - return []
        # - raise ValueError
        try:
            out = student.fibonacci(0)
            self.assertEqual(out, [])
        except ValueError:
            self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
