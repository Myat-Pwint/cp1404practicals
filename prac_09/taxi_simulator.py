from taxi import Taxi, SilverServiceTaxi


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    while True:
        try:
            choice = int(input("Choose taxi: "))
            if 0 <= choice < len(taxis):
                return taxis[choice]
            else:
                print("Invalid taxi choice")
        except ValueError:
            print("Invalid input")


def main():
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0.0

    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == 'q':
            break
        elif choice == 'c':
            display_taxis(taxis)
            current_taxi = choose_taxi(taxis)
            print("Bill to date: ${:.2f}".format(bill))
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    fare = current_taxi.drive(distance)
                    bill += fare
                    print("Your {} trip cost you ${:.2f}".format(current_taxi.name, fare))
                    print("Bill to date: ${:.2f}".format(bill))
                except ValueError:
                    print("Invalid distance")
        else:
            print("Invalid option")
            print("Bill to date: ${:.2f}".format(bill))

    print("Total trip cost: ${:.2f}".format(bill))
    print("Taxis are now:")
    display_taxis(taxis)


main()
