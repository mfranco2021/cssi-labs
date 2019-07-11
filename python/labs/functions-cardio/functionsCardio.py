print("welcome to onse function cardio")

num1 = int(raw_input("Give me a 1 side length: "))
num2 = int(raw_input("Give me a 2 side length: "))
num3 = int(raw_input("Give me a 3 side length: "))

def is_triangle(s1, s2, s3):
    sum1 = s1 + s2
    sum2 = s2 + s3
    sum3 = s3 + s1
    if sum1 > s3 and sum2 > s1 and sum3 > s2:
        return True
    else:
        return False

    is_triangle(num1, num2, num3)
