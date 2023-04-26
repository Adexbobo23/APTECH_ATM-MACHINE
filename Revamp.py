import math

def hello():
    pass


def greet(*name):
    # name = input("Enter your name here: ")
    age = int(input("Enter your age here: "))

    print(f"\nWelcome to APTECH TEST CLASS {name}")
    if age <= 18:
        print("You are very young, So don't do YAHOO")

    else:
        print("You are matured enough to determine how your future will look like")


def hi():
    greet()


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


tri_recursion(7)


def num():
    global x
    x = 12
    print(x)


num()
x = 20
print(x)