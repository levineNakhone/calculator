
from secrets import choice

def add(a, b):
    answer = a+b
    print(str(a) + "+ " + str(b) + " = " + str(answer))

def sub(a, b):
    answer = a-b
    print(str(a) + "- "+ str(b)+ " = " + str(answer))

def mult (a, b):
    answer = a*b
    print(str(a) + " * "+ str(b)+ " = " + str(answer))

def div (a, b):
    answer = a/b
    print(str(a) + " / "+ str(b)+ " = " + str(answer))
while True:

    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice == input("input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("input first number:"))
        b = int(input("input second number:"))
        add(a, b)

    elif choice == "b" or choice == "B":
        print("Substraction")
        a = int(input("input first number:"))
        b = int(input("input second number:"))
        sub(a, b)

    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("input first number:"))
        b = int(input("input second number:"))
        mult(a, b)

    elif choice == "c" or choice == "C":
        print("Division")
        a = int(input("input first number:"))
        b = int(input("input second number:"))
        div(a, b)


    elif choice == "e" or "E":
        print("program ended")
        quit()