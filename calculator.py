x = int(input("Please, enter first number:"))
y = int(input("Please, enter second number:"))
operation = int(input("Which operation do you want to use? \n 1) Addition \n 2) Substraction \n 3) Multiplication"
                      " \n 4) Division \n 5) Exponentation \n 6) Remainder \n 7) Exit"))
while True:
    if operation == 1:
        print(x + y)
    if operation == 2:
        print(x - y)
    if operation == 3:
        print(x * y)
    if operation == 4:
        if y == 0:
            print("Error, you could not devide by zero.")
        else:
            print(x // y)
    if operation == 5:
        print(x ** y)
    if operation == 6:
        if y == 0:
            print("Error, you could not devide by zero.")
        else:
            print(x % y)
    if operation == 7:
        break

print( " Program has ended successfully.")