#!/usr/bin/env python3

# Question:
#  Return quarters, dimes, nickels and pennies given an amount

if __name__ == "__main__":
    x = int(input("Enter amount: "))
    quarters = int(x / 25)
    dimes = int((x - quarters * 25) / 10)
    nickels = int((x - quarters * 25 - dimes * 10) / 5)
    pennies = x - quarters * 25 - dimes * 10 - nickels * 5
    print(quarters, "quarters,", dimes, "dimes,", nickels, "nickels and", pennies, "pennies.")
