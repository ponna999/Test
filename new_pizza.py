import re
def pizza_list(a):
    pizza_variety = open('Pizza_variety.txt','r')
    pz1= pizza_variety.readlines()
    for i in pz1:
        if i.__contains__(a):
            temp =i.split(" ")
            Sel_pizza = int(temp[2])
    pizza_variety.close()
    return Sel_pizza


def pizza_top(b):
    pizza_topping = open('Pizza_toppings.txt','r')
    pt1= pizza_topping.readlines()
    for i in pt1:
        if i.__contains__(b):
            temp =i.split(" ")
            Sel_topping = int(temp[2])
    pizza_topping.close()
    return Sel_topping


def pizza_order():
    name_of_customer = str(input("Enter the name:"))
    mobile_num = input("Enter the mobile number:")
    if (len(mobile_num) != 10):
        print("Enter a vaild mobile number!!!!")
        exit()
    pizza_dict = {1:'margaritha',2:'farmhouse',3:'mexican'}
    pizza_topping = {1:'onion',2:'corn',3:'chicken'}
    keys  = pizza_dict.keys()
    keys1 = pizza_topping.keys()

    print("select the pizza you wanted:")
    for i in pizza_dict:
        print(i, "-", pizza_dict[i])
    choice= int(input())

    if choice in keys:
        select_pizza = pizza_dict[choice]
    else:
        print ("enter a valid choice")
        exit()

    print ("Select the topping for the pizza:")
    for i in pizza_topping:
        print(i,"-",pizza_topping[i])
    choice1 = int(input())

    if choice1 in keys1:
        select_topping = pizza_topping[choice1]
    else:
        print("enter a valid choice")
        exit()

    a = pizza_list(select_pizza)
    b = pizza_top(select_topping)

    print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print ("+++++++++++++++++++++Bill Reivew+++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print ("Name:",name_of_customer)
    print ("Mobile:",mobile_num)
    print ("Pizza Selected:",select_pizza)
    print ("Pizza topping:",select_topping)
    print ("Total money to be paid:", a +b )
    print("Thank you for shopping,Have a nice day")

    file = open(name_of_customer+'.txt','a')
    file.writelines("Name:")
    file.write(name_of_customer)
    file.write('\n')
    file.writelines("Mobile:")
    file.write(mobile_num)
    file.write('\n')
    file.writelines("Pizza Selected:")
    file.write(select_pizza)
    file.write('\n')
    file.writelines("Pizza topping:")
    file.write(select_topping)
    file.write('\n')
    # file.writelines("Total amount to be paid:")
    # total = a + b
    # file.write(total)
    file.close()

pizza_order()






