# Menu of the restaruant
menu ={
    'Pizza':200,
    'Pasta':149,
    'Burger':139,
    'Fries':80,
    'Rosted Chicken':120,
    'Coffee':70,
    'Tea':30,
}

#Start Greating
print("Hi There Welcome to Tanzirs 7")
print(" Pizza: 200TK\n Pasta: 149TK\n Burger: 139TK\n Fries: 80TK\n Rosted Chicken: 120TK\n Coffee: 70TK\n Tea: 30TK")

order_total = 0

item_1 =input("Enter a name of the item you want to order")
if item_1 in menu:
    order_total += menu[item_1]
    print("Your item has been added ")
    
else:
    print("Please order something else from the menu")
    
another_order = input ("Do you want to add another item? (Y/N)")
if another_order =="Y":
    item_2 =input("Enter 2nd item you want to order= ")
    if item_2 in menu:
        order_total += menu[item_2]
        print("Another item has been added")
    else:
        print("Pleas order Correctely")
        

if another_order =="N":
   
    print("Thank you For your time.")
        
print(f"The total amount of items to pay is {order_total}")
