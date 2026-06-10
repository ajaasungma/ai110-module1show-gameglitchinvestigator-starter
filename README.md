# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Purpose:** A Streamlit number-guessing game — guess the secret number within a limited number of attempts, with higher/lower hints and a score.
- [x] **Bugs found:** Higher/Lower hints were backwards; the secret turned into a string on some attempts, breaking comparisons; scoring was inconsistent (wrong "too high" guesses sometimes gained points); the attempt counter started at 1; and "New Game" stayed stuck after a win.
- [x] **Fixes applied:** Refactored the logic into `logic_utils.py`, corrected the hint direction, made all wrong guesses cost the same with a clean win bonus, started attempts at 0, and reset full game state on "New Game".

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 50
2. Game returns "Too Low"
3. User enters a guess of 60 → "Too High"
4. Score updates correctly after each guess
5. Game ends after the correct guess
6. New Game can be started

