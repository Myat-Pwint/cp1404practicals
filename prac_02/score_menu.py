def main():
    MENU = "(G)et a valid score \n(P)rint result \n(S)how stars \n(Q)uit"
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            result = calculate_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice!")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell!")


def get_score():
    while True:
        score = input("Enter a score(0-100): ")
        if score.isdigit() and int(score) in range(0, 101):
            return int(score)
        else:
            print("Invalid score. Please enter a number between 0 and 100.")


def calculate_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    print("*" * score)


main()
