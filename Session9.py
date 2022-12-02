# This application was made By Wira Harsa from TI22I
from time import sleep


def Menu():

  print("Select Our Menu")
  print("1.List of Products")
  print("2.Insert Product")
  print("3.Delete Product")
  print("4.Delete Product by number")
  print("5.Exit")


Menu()
while True:
  choice = input("Enter menu (1/2/3/4/5): ")

  # List products

  if choice == '1':
    list_of_product = ['Chicken', 'Beef', 'Lamb', 'Human', 'Rabbit']

    print(list_of_product)

# Insert Product
  elif choice == '2':
    list_of_product = ['Chicken', 'Beef', 'Lamb', 'Human', 'Rabbit']
    list_of_product.append(input("What will you insert to the list? "))

    print(list_of_product)

# Delete product
  elif choice == '3':
    list_of_product = ['Chicken', 'Beef', 'Lamb', 'Human', 'Rabbit']
    list_of_product.remove('human')
    print(list_of_product)

# Delete product by number (index)
  elif choice == '4':
    list_of_product = ['Chicken', 'Beef', 'Lamb', 'Human', 'Rabbit']
    list_of_product.pop(
      int(input("What product will you delete from the list? ")) - 1)
    print(list_of_product)

# Exit
  elif choice == '5':
    print("Thank you for using my program")
    sleep(2)
    break

  else:
    print("Invalid Input")