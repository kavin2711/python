try:
    x=int(input("Please enter a number: "))
    y=1/x
    print("The reciprocal of", x, "is", y)
except ValueError:
    print("pls enter a valid number")
except ZeroDivisionError:
    print("The reciprocal of zero is undefined")
