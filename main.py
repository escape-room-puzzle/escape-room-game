"""
Escape Room Lab (Student Skeleton)

You will solve 3 puzzles by writing Python functions:
1) Laser Path (simulate moving across a grid to a goal square)
2) Caesar Cipher decoder (shift letters back by 3)
3) Fibonacci missing number (find the missing value)

Run tests with:
    python -m unittest test_escape_room.py
"""

# Puzzle 1: Laser Path Simulation

GRID_WIDTH = 10
GRID_HEIGHT = 10

START = (0, 0)
GOAL = (9, 9)

# Lasers are positions (x, y) that are "danger squares".
LASERS = {
    (2, 2), (2, 3), (2, 4),        # vertical laser segment
    (5, 7), (6, 7), (7, 7), (8, 7) # horizontal laser segment
}

def in_bounds(x: int, y: int) -> bool:
    """
    Return True if (x, y) is inside the grid, otherwise False.
    """
    # TODO
    return False

def hits_laser(x: int, y: int, lasers=LASERS) -> bool:
    """
    Return True if (x, y) is a laser coordinate, otherwise False.
    """
    # TODO
    return False

def apply_move(x: int, y: int, move: str) -> tuple[int, int]:
    """
    Given a current position (x, y) and a move letter:
        'U' = up    (y + 1)
        'D' = down  (y - 1)
        'L' = left  (x - 1)
        'R' = right (x + 1)

    Return the NEW (x, y).

    Assumption:
    - move will be a single character like 'U', 'D', 'L', 'R'
    """
    # TODO
    return (x, y)

def simulate_path(moves: str, start=START, goal=GOAL, lasers=LASERS) -> str:
    """
    Simulate walking through the room starting at start.
    moves is a string like "RRUUUR".

    At EACH step:
    - Update position using apply_move
    - If out of bounds -> return "OUT"
    - If hits a laser -> return "LASER"
    - If reaches goal -> return "GOAL"

    If all moves are used and you never reached the goal,
    return "OK" (meaning: safe so far, but not at the goal yet).
    """
    # TODO
    return "OK"

def laser_puzzle() -> bool:
    """
    Interactive puzzle:
    - Student enters a move string like RRUUURRDD...
    - If they reach the goal safely, they pass.
    - Otherwise, they fail and can try again.

    Repeat until correct.
    """
    print("\n========== Puzzle 1: Laser Path ==========")
    print(f"Grid size: {GRID_WIDTH} by {GRID_HEIGHT}")
    print(f"Start: {START}  Goal: {GOAL}")
    print("Enter moves using only U D L R (example: RRUUURR)")

    # TODO: loop until success
    # TODO: read moves using input()
    # TODO: call simulate_path()
    # TODO: print helpful messages depending on result
    return False


# Puzzle 2: Caesar Cipher (shift by 3)

def shift_char_back_3(ch: str) -> str:
    """
    Shift ONE letter back by 3 in the alphabet.
    - Preserve case: 'D' -> 'A', 'd' -> 'a'
    - Wrap around: 'A' -> 'X', 'b' -> 'y'
    - Non-letters should be returned unchanged (spaces, punctuation, digits).
    """
    # TODO
    return ch

def caesar_decode(ciphertext: str) -> str:
    """
    Decode a Caesar cipher where letters were shifted FORWARD by 3.
    That means we shift BACK by 3 to decode.

    Example:
        "Khoor" -> "Hello"
    """
    # TODO: build a decoded string character-by-character (loop)
    return ""

def cipher_puzzle() -> bool:
    """
    Interactive puzzle:
    - Give students an encoded message
    - Ask them to decode it using caesar_decode
    - If their decoded text contains the correct 'key phrase', they pass

    NOTE: For the lab, you can make the key phrase obvious or hidden.
    """
    print("\n=== Puzzle 2: Caesar Cipher ===")

    encoded = "Wkh nhb frgh lv: FODVVURRP"
    print("A note on the wall reads:")
    print(encoded)

    # TODO: decode with caesar_decode
    # TODO: check if the decoded result includes the key phrase (case-insensitive is fine)
    # TODO: print messages
    return False


# Puzzle 3: Fibonacci

def fibonacci(n: int) -> list[int]:
    """
    Return a list of the first n Fibonacci numbers.

    Use this definition:
    - fibonacci(1) -> [0]
    - fibonacci(2) -> [0, 1]
    - fibonacci(6) -> [0, 1, 1, 2, 3, 5]

    Hints:
    - Handle small n carefully
    - Use a loop to build the list
    """
    # TODO
    return []


def fibonacci_puzzle() -> bool:
    """
    Interactive puzzle:
    - Ask for n
    - Generate the first n Fibonacci numbers
    - The "door code" is the last number in the list
    """
    print("\n=== Puzzle 3: Fibonacci Door Code ===")

    # TODO: get n from input and convert to int
    # TODO: call fibonacci(n)
    # TODO: print the sequence
    # TODO: print the "door code" as the last number
    return False


# Escape Room Driver

def run_escape_room() -> None:
    """
    Runs all 3 puzzles in order.
    Students escape if they pass all puzzles.
    """
    print("Welcome to the Python Escape Room!")
    print("Solve the puzzles by completing the functions in this file.")

    # TODO: call each puzzle function
    # TODO: only proceed if the previous puzzle was passed
    # TODO: print a victory message if all are passed
    pass


if __name__ == "__main__":
    run_escape_room()
