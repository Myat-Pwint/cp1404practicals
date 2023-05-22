from prac_09.unreliable_car import UnreliableCar

my_car = UnreliableCar("Unreliable Car", 100, 50)

# Drive the car 50 km
distance_driven = my_car.drive(50)
print("Distance driven:", distance_driven)

# Drive the car 100 km
distance_driven = my_car.drive(100)
print("Distance driven:", distance_driven)