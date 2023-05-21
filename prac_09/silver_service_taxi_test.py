from prac_09.silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi("Hummer", 200, 2)

# Drive the taxi for 18 km
my_taxi.drive(18)
fare = my_taxi.get_fare()
print("Fare: ${:.2f}".format(fare))

