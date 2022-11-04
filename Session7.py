# This program was made by Wira Harsa Aiyasa Rifki Ghani | TI22I class.
from time import sleep

def Area_of_Triangle(x,y):
    return x*y/2
def Area_of_Rectangle(x,y):
    return x*y
def Odd_and_Even ():
    
    print("Select operation.")
    print("1.Area of Triangle")
    print("2.Area of Rectagle")
    print("3.Determine Odd and Even number")
    print("4.Exit")
while True:
    choice = input("Enter your choice(1/2/3/4): ")
    
# Python Program to find the area of triangle   
    if choice == '1':
        a = float(input('Enter Base side: '))
        b = float(input('Enter Height side: '))
# calculate the area
        area = (a * b) /2
        print('The area of the triangle is', area)
    
# Python program to find the area of rectangle
    elif choice == '2':
        c= float(input('Enter Length side: '))
        d = float(input('Enter Width side: '))
# Python program to find the area of Rectangle
        area = (c * d)
        print('The area of the triangle is', area)

# python program to determine Odd and Even Number
    elif choice == '3':
        num = int(input("Enter your number : "))
        if (num % 2) == 0:
            print("{0} is An even number".format(num))
        else:
            print("{0} is An odd Number".format(num))

    elif choice == '4':
        print("Thank you for using my program")
        sleep(2)
        break
    
    else:
        print("Invalid Input")

        
    
    
    