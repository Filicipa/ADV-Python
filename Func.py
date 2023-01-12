def pechat(name):
    """Print priv"""
    print("HELLO FUNC " + name)
    print("CONGR ")


def summa(x, y):
    return x + y


def factorial(x):
    """Calc factorial"""
    otvet = 1
    for i in range(1, x + 1):
        otvet = otvet * i
    return otvet

print("--------")
pechat("SASHA")
pechat("DIMA")


x = summa(33, 22)
print(x)

for i in range(1, 10):
    print(str(i) + "!\t = " + str(factorial(i)))

