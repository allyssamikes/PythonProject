class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2


def getDouble(message):
    return float(input(message + ": "))


def getString(message):
    return input(message + ": ")


calc = Calculator()
check = True
while check == True:
    num1 = getDouble("Enter a number")
    num2 = getDouble("Enter another number")
    print("You want to add", format(num1, ".2f"), "and", format(num2, ".2f"))
    print("Answer:", calc.add(num1, num2))
    print("You want to subtract", format(num1, ".2f"), "and", format(num2, ".2f"))
    print("Answer:", calc.subtract(num1, num2))
    print("You want to multiply", format(num1, ".2f"), "and", format(num2, ".2f"))
    print("Answer:", calc.multiply(num1, num2))
    print("You want to divide", format(num1, ".2f"), "and", format(num2, ".2f"))
    print("Answer:", calc.divide(num1, num2))
    input()
    answer = getString("Would you like to continue? y/n")
    if answer == "y":
        continue
    else:
        print("Goodbye")
        check = False