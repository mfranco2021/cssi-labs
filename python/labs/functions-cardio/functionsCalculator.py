print("Welcome to monse cauculator")

num1 = int(raw_input("Give me a whole number: "))
num2 = int(raw_input("Give me another whole number: "))


def myAddFunction(add1, add2):
    sum = add1 + add2
    return sum
print("Here is the sum: " + str(myAddFunction(num1, num2)))


def mySubFunction(sub1, sub2):
    difr = sub1 - sub2
    return difr
print("Here is the diffrence: " + str(mySubFunction(num1, num2)))

def myMultFunction(mult1, mult2):
    prod = mult1 * mult2
    return prod
print("Here is the product: " + str(myMultFunction(num1, num2)))
