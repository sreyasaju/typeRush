
def calculate_accuracy(user_input, original):
   correct = sum(1 for i, c in enumerate(user_input) if i < len(original) and c == original[i])
   accuracy = (correct / len(original)) * 100
   return accuracy


def calculate_wpm(user_input: str, elapsed_time: float) -> float:
    if elapsed_time <= 0:
        return 0.0
    total_words = len(user_input.split())
    wpm = (total_words / elapsed_time) * 60
    return wpm