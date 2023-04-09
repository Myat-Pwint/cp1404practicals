"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    display_subjects(data)


def get_data():
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    input_file.close()
    return data


def display_subjects(data):
    for subject in data:
        if subject[2] == 1:
            print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")
        else:
            print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()
