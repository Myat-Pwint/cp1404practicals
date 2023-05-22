from taxi import Taxi, SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()

    while choice != "q":

        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            choose_taxi(taxis, total_bill)

        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
                print("Bill to date: ${:.2f}".format(total_bill))
            else:
                distance = float(input("Drive how far? "))
                fare = current_taxi.get_fare(distance)
                current_taxi.start_fare()
                total_bill += fare
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, fare))
                print("Bill to date: ${:.2f}".format(total_bill))

        else:
            print("Invalid option")
            print("Bill to date: ${:.2f}".format(total_bill))

        print(MENU)
        choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis, total_bill):
    taxi_choice = int(input("Choose taxi: "))
    if taxi_choice < 0 or taxi_choice >= len(taxis):
        print("Invalid taxi choice")
        print("Bill to date: ${:.2f}".format(total_bill))
    else:
        current_taxi = taxis[taxi_choice]
        print("Bill to date: ${:.2f}".format(total_bill))


main()