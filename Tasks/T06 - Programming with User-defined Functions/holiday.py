# Practical Task 1

# city options
def options():
    print("City Options:")
    print("l = London")
    print("t = Tokyo")
    print("p = Paris")
    print("b = Berlin")

options()
# different city, diferent flight cost
city_flight = {
    "London" : 100,
    "Tokyo" : 150,
    "Paris" : 200,
    "Berlin" : 300,
}

# input city
city_short = input("Which city are you flying to? \n")
# input number of nights in hotel
num_nights = int(input("How many nights are you staying at a hotel? \n"))
# input number of days hiring a car
rental_days = int(input("How many days are you hiring a car? \n"))

# calculate plane cost
def plane_cost(city):
    if city == "l":
        return city_flight["London"]
    elif city == "t":
        return city_flight["Tokyo"]
    elif city == "p":
        return city_flight["Paris"]
    elif city == "b":
        return city_flight["Berlin"]
    else:
        print("Unrecognized your city.")
        return 0
# calculate hotel cost
def hotel_cost(nights):
    return nights * 200
# calculate car rental
def car_rental(days):
    return days * 100
# calculate total holiday cost
def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental
# call functions
pc = plane_cost(city_short)
hc = hotel_cost(num_nights)
cr = car_rental(rental_days)

print("The details about the holiday cost: ")
print(f"The plane cost is £{pc}.")
print(f"The hotel cost is £{hc}.")
print(f"The car rental cost is £{cr}.")
print(f"The total holiday cost is £{holiday_cost(hc, pc, cr)}.")
