import platform, os

platform = platform.system()
def program_title():
    print("""
Wira Harsa Abiyasa Rifki Ghani || TI221
#######################################
#######################################
###### Welcome To My Application ######
#######################################
#######################################
   -----------+++====+++------------
""")

def thank():
    print("\nThank You for using the program...\n")

def clear_display():
    if platform == "Linux":
        os.system("clear")
    if platform == "Windows":
        os.system("cls")

def sum_list(var_list,t_list):
    total  = sum(var_list)
    t_list.append(total)
    
clear_display()
program_title()

prd_name, prd_price, ordr_quantity, buy_price = [],[],[],[]
prcnt, prft, sllng_price, itm_sld, ttl_prft, ttl_income = [],[],[],[],[],[]

t_income, t_profit = [],[]

def main():
    run = True
    while run:
        # Product Name
        product_name = input("Product name: ").title()
        prd_name.append(product_name)

        # Product Price
        purchase_price = float(input("Price: "))
        prd_price.append(purchase_price)

        # Items Quantity
        order_quantity = int(input("Order Quantity: "))
        ordr_quantity.append(order_quantity)

        # selling price = product price * order quantity
        total_cost = purchase_price * order_quantity
        buy_price.append(total_cost)

        # Profit
        percent = input("Percent: ").split("%")
        
            
        prcnt.append(percent)
        
        
        profit = (purchase_price * float(percent[0])/100 )
        prft.append(profit)

        # selling price = product price + profit
        selling_price = purchase_price + profit
        sllng_price.append(selling_price)

        # items have been sold
        item_sold = int(input("Item sold: "))
        itm_sld.append(item_sold)

        # total profit
        income = item_sold * selling_price
        ttl_income.append(income)

        # total income
        total_profit = income - total_cost
        ttl_prft.append(total_profit)

        # another transaction
        enter_again = input("\nIs there anything else?, y/n: ").lower()
        if enter_again == "y":
            run = True
        elif enter_again == "n":
            run = False
        else:
            print("Invalid input")
            
    clear_display()

    sum_list(ttl_income,t_income)
    sum_list(ttl_prft, t_profit)

    print("="*45)
    print(f"Product Name   : {prd_name}\nPurchase Price : {prd_price}\nOrder Quantity : {ordr_quantity}\n\
Total Cost     : {buy_price} \nPercent        : ",end='')
    if len(prcnt)> 1: 
        for i in range(0, len(prcnt[0])):
            print(prcnt[i][0],"%", end=", ")
    else:
        print(prcnt[0][0],"%")
    print(f"\nMargin Profit  : {prft}\nSelling Price  : {sllng_price}\n\
Item sold      : {itm_sld}\nIncome         : {ttl_income}\nTotal Income   :  {t_income[0]}\nProfit         : {ttl_prft}\nTotal Profit   :  {t_profit[0]}")
    
    tanda = 45
    if len(prd_name) >= 4:
        tanda += 35
    print('='* tanda)
    
if __name__ =="__main__":
    main()
    thank()