import random


def main():
    score = float(input("Enter score: "))
    message = get_message(score)
    print(message)

    random_score = random.randint(0, 100)
    random_message = get_message(random_score)
    print(f"Random score: {random_score}, Result: {random_message}")


def get_message(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
