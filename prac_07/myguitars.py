import csv
from prac_06.guitar import Guitar


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __lt__(self, other):
        return self.year < other.year


def read_guitars(filename):
    guitars = []
    with open(filename, "r") as file:
        for line in file:
            name, year, cost = line.strip().split(",")
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars


def write_guitars(filename, guitars):
    with open(filename, "w") as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost:.2f}\n")


def main():
    filename = "guitars.csv"
    guitars = read_guitars(filename)

    print("All guitars:")
    for guitar in guitars:
        print(guitar.name, guitar.year, guitar.cost)

    # prompt user for new guitars
    while True:
        name = input("Enter guitar name (or 'quit' to exit): ")
        if name == "quit":
            break
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

    guitars.sort()

    print("All guitars (sorted by year):")
    for guitar in guitars:
        print(guitar.name, guitar.year, guitar.cost)

    # write guitars to file
    write_guitars(filename, guitars)


if __name__ == "__main__":
    main()
