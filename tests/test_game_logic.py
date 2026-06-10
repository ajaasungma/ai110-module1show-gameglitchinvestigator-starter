from logic_utils import (
    check_guess,
    update_score,
    parse_guess,
    get_range_for_difficulty,
)

# check_guess returns a tuple: (outcome, message)
# outcome is what the game logic cares about; message is the hint shown in the UI.


# --- Starter tests (fixed to unpack the outcome from the tuple) ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug: the high/low HINT MESSAGE was backwards ---
# It's not enough that the outcome label is right; the advice shown to the
# player must point the correct direction.

def test_too_high_tells_player_to_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_tells_player_to_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# --- Bug: the int/str "glitch" caused wrong comparisons on some attempts ---
# check_guess must give the same correct answer no matter what; passing a plain
# integer secret should always work.

def test_check_guess_is_consistent():
    assert check_guess(80, 50)[0] == "Too High"
    assert check_guess(20, 50)[0] == "Too Low"
    assert check_guess(50, 50)[0] == "Win"


# --- Bug: scoring was incoherent ---

def test_wrong_guess_always_loses_points_regardless_of_direction():
    # "Too High" used to give +5 on even attempts -- rewarding a wrong guess.
    assert update_score(100, "Too High", 2) == 95
    assert update_score(100, "Too High", 3) == 95
    assert update_score(100, "Too Low", 2) == 95
    assert update_score(100, "Too Low", 3) == 95

def test_win_bonus_is_higher_for_fewer_attempts():
    first_try = update_score(0, "Win", 1)
    third_try = update_score(0, "Win", 3)
    assert first_try == 100          # full points on the first attempt
    assert first_try > third_try     # more attempts -> smaller bonus

def test_win_bonus_never_below_floor():
    # Even after many attempts the win bonus should not drop under 10.
    assert update_score(0, "Win", 20) == 10


# --- Supporting logic ---

def test_parse_guess_accepts_valid_number():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_rejects_non_number():
    ok, value, err = parse_guess("hello")
    assert ok is False
    assert value is None

def test_parse_guess_rejects_empty():
    ok, value, err = parse_guess("")
    assert ok is False

def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    # Unknown difficulty falls back to the default range.
    assert get_range_for_difficulty("Whatever") == (1, 100)
