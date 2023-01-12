#
# name = input("Please enter your name :")
# print("Privet " + name)

# num1 = input("Enter X: ")
# num2 = input("Enter Y: ")
# suma = int(num1) + int(num2)
# print(suma)

mylist = []
mes = ""
while mes != "stop":
    mes = input("Enter new item, and STOP finish 1")
    mylist.append(mes)

print(mylist)