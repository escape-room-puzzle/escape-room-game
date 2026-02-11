"""
Escape Room Lab 

You will solve 3 puzzles by writing Python functions:
1) Laser Grid (coordinate checking)
2) Caesar Cipher decoder (shift letters back by 3)
3) Fibonacci helper (generate/check a sequence)

Run tests with:
    python -m unittest test_escape_room.py

To write a function;
    Replace your code with # TODO
    Replace return False with the function parameter you are required to return
"""

# Puzzle 1: Laser Grid

GRID_WIDTH = 10
GRID_HEIGHT = 10

# Lasers are positions (x, y) that are "danger squares".
# Coordinates are integers, with 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT.
LASERS = {
    (2, 2), (2, 3), (2, 4),        # vertical laser segment
    (5, 7), (6, 7), (7, 7), (8, 7) # horizontal laser segment
}

def in_bounds(x: int, y: int) -> bool:
    """
    Return True if (x, y) is inside the grid, otherwise False.
    TODO: implement using comparisons and boolean logic.
    """
    # TODO
    return False

def hits_laser(x: int, y: int, lasers = LASERS) -> bool:
    """
    Return True if (x, y) is a laser coordinate, otherwise False.

    Hints:
    - Make sure the point is in bounds first.
    - A set makes membership checks fast: (x, y) in lasers
    """
    # TODO
    return False

def laser_puzzle() -> bool:
    """
    Interactive puzzle:
    - Ask the student for x and y.
    - If they are safe (in-bounds and NOT a laser), they pass this puzzle.
    - Otherwise, they fail and can try again.

    Repeat until correct.
    """
    print("\n========== Puzzle 1: Laser Grid ========== ")
    print("Enter coordinates to step through the room.")
    print(f"Grid size: {GRID_WIDTH} by {GRID_HEIGHT}")
    print("Tip: Coordinates are whole numbers (integers).")

    # TODO: get user input using input()
    # TODO: convert to int
    # TODO: use hits_laser and in_bounds to decide success/failure
    # TODO: print messages
    return False



# Puzzle 2: Caesar Cipher 

def shift_char_back_3(ch: str) -> str:
    """
    Shift ONE letter back by 3 in the alphabet.
    - Preserve case: 'D' -> 'A', 'd' -> 'a'
    - Wrap around: 'A' -> 'X', 'b' -> 'y'
    - Non-letters should be returned unchanged (spaces, punctuation, digits).

    Hint: Use modulos operator (%) to wrap around the alphabet!
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
    This is the main flow for the Caesar cipher.:
    - There is an encoded message
    - Decode it using caesar_decode
    - If the decoded text contains the correct 'key phrase', it passes

    NOTE: Key Phrase can be any word in the encoded message.
    """
    print("\n========== Puzzle 2: Caesar Cipher ========== ")

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
    print("\n========== Puzzle 3: Fibonacci Door Code ==========")

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
    print("Welcome to the Escape Room!")
    print("Solve the puzzles by completing the functions in this file.")

    # TODO: call each puzzle function
    # TODO: only proceed if the previous puzzle was passed
    # TODO: print a victory message if all are passed
    pass


if __name__ == "__main__":
    run_escape_room()
