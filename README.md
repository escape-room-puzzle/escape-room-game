# 🧩 Python Escape Room Lab

Welcome to the Escape Room!

Your mission is to complete the functions in `main.py` and solve three coding puzzles. Each puzzle unlocks the next one. When all puzzles pass, you escape!

---

## 🔴 Puzzle 1: Laser Grid

Write code to check whether a coordinate:

- Is inside the grid
- Is not on a laser

If the coordinate is invalid or hits a laser, the user must try again.

---

## 🔐 Puzzle 2: Caesar Cipher

Decode a secret message where each letter was shifted **forward by 3**.

Your job:
- Shift letters back by 3
- Keep uppercase/lowercase the same
- Leave spaces and punctuation unchanged

If the decoded message contains the correct key phrase, the puzzle passes.

---

## 🚪 Puzzle 3: Fibonacci Door Code

Generate the first **n Fibonacci numbers** using a loop.

The final number in the sequence unlocks the door.

---

## Submission
Please submit your work in this google form: [Google Form]([https://example.com](https://docs.google.com/forms/d/e/1FAIpQLSd8KWzgms12T5Cz6st3Cwilk_YnI6v6qQfDAv0xxDk1dstTNg/viewform?usp=publish-editor))

## 🛠 How to Work

1. Open `main.py`
2. Complete the `# TODO` sections
3. Do not change function names or parameters
4. Run the tests:

```bash
python -m unittest test_escape_room.py
