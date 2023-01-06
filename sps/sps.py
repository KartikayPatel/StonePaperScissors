print ("Calculator")

num1 = float(input("enter your first number: "))
num2 = float(input("enter your second number: "))

print ("Press 1 for addition \nPress 2 for subtraction \nPress 3 for Multiplication \nPress 4 for Division")

Choice = int(input("Enter Your Choice Between 1-4: "))

if Choice == 1:
    print (num1 + num2)

elif Choice == 2:
    print (num1 - num2 )

elif Choice == 3:
    print (num1 * num2)

elif Choice == 4:
    print (num1 / num2)

else:
    print("Invalid Input")