
import difflib

def calculate_accuracy(user_input, original):
    if not original:
        return 100.0
    matcher = difflib.SequenceMatcher(None, user_input, original)
    return matcher.ratio() * 100


def calculate_wpm(user_input: str, elapsed_time: float) -> float:
    if elapsed_time <= 0:
        return 0.0
    total_words = len(user_input.split())
    wpm = (total_words / elapsed_time) * 60
    return wpm