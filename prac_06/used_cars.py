"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from car import Car


def main():
    """Demo test code to show how to use car class."""
    limo = Car(name="Limo", fuel=100)
    limo.add_fuel(20)
    print(f"{limo.name} has fuel: {limo.fuel}")
    limo.drive(115)
    print(limo)

    my_car = Car(180, "Mazda")
    my_car.drive(30)
    print(f"{my_car}\n")

    limo = Car(100, "Limousine")
    limo.add_fuel(20)
    print(f"{limo}")
    limo.drive(115)
    print(f"After driving 115km: {limo}\n")

    main()


main()
