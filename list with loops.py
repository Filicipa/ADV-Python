# cars = ["bmw", "vw", "seat", "skoda", "lada"]
# for car in cars:
#     print(car.upper())
#
# for x in range(1, 6):
#     print(x)

mynumber_list = list(range(0, 10))
print(mynumber_list)

for x in mynumber_list:
    x = x * 2
    print(x)

mynumber_list.reverse()
print(mynumber_list)
print("Max number is: " + str(max(mynumber_list)))
print("Min number is: " + str(min(mynumber_list)))
print("Sum of list is: " + str(sum(mynumber_list)))

cars = ["bmw", "vw", "seat", "skoda", "lada"]
mycars = cars[1:4]
print(mycars)
mycars = cars[-1:]
print(mycars)

cars = ["bmw", "vw", "seat", "skoda", "lada"]
mycars = cars[:]
