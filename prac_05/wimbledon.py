import csv

def main():
    champion_data = read_csv_file("wimbledon.csv")
    champtions = get_champions(champion_data)
    display_champions(champtions)
    countries = get_countries(champion_data)
    display_countries(countries)

def read_csv_file(file_name):
    with open(file_name, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        return [row for row in reader]


def get_champions(champion_data):
    champions = {}
    for row in champion_data:
        champion = row[2]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def get_countries(champion_data):
    countries = set()
    for row in champion_data:
        country = row[1]
        countries.add(country)
    return sorted(countries)


def display_champions(champions):
    print("Wimbledon Champions:")
    for champion, count in sorted(champions.items()):
        print(f"{champion} {count}")


def display_countries(countries):
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(countries))



main()
