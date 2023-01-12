# age = 13
#
# if (age <= 4):
#     print("you are baby")
# elif (age > 4) and (age < 12):
#     print("You are kid")
# elif (age >= 12) and (age <=19):
#     print("You are teenager")
# else:
#     print("You are old")

all_cars = ["chrysler", "dacia", "bmw", "KIA", "vw", "seat", "skoda", "lada", "audi", "ford", "Chevrolet"]
german_cars = ["bmw", "vw", "audi"]

for car in all_cars:
    if car in german_cars:
        print(car + " in german car")