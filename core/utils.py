# core/utils.py

import Levenshtein

def calculate_accuracy(user_input: str, original: str) -> float:
    if not user_input: 
        return 0.0
    distance = Levenshtein.distance(user_input, original[:len(user_input)])
    accuracy = max(0.0, (1 - distance / len(user_input)) * 100)
    return accuracy

def calculate_wpm(user_input: str, elapsed_time: float) -> float:
    if elapsed_time <= 0:
        return 0.0
    total_chars = len(user_input)
    wpm = (total_chars / 5) / (elapsed_time / 60)
    return wpm