import Levenshtein

def calculate_accuracy(user_input: str, original: str) -> float:
    if not original:
        return 100.0
    distance = Levenshtein.distance(user_input, original)
    accuracy = max(0.0, (1 - distance / len(original)) * 100)
    return accuracy


def calculate_wpm(user_input: str, elapsed_time: float) -> float:
    if elapsed_time <= 0:
        return 0.0
    total_words = len(user_input.split())
    wpm = (total_words / elapsed_time) * 60
    return wpm