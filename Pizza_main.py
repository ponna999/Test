import re
def pizza_order():
    name_of_customer = str(input("Enter the name:"))
    mobile_num = input("Enter the mobile number:")
    if (len(mobile_num) != 10):
        print("Enter a vaild mobile number!!!!")
        exit()
    pizza_variety = open('Pizza_variety.txt','r')
    print("The below are the available pizza's")
    pz1= pizza_variety.readlines()
    for i in pz1:
        print (i)
    sel_pizza = input("Enter the pizza of which you want from the available menu:")
    for i in pz1:
        if i.__contains__(sel_pizza):
            temp =i.split(" ")
            pizza_base = int(temp[2])

    pizza_topping = open('Pizza_toppings.txt','r')
    print("The below are the available pizza toppings")
    pt1= pizza_topping.readlines()
    for i in pt1:
        print (i)
    sel_topping = input("Enter the topping of which you want from the available menu:")
    for i in pt1:
        if i.__contains__(sel_topping):
            temp =i.split(" ")
            pizza_topping = int(temp[2])

    print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print ("+++++++++++++++++++++Bill Reivew+++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print ("Name:",name_of_customer)
    print ("Mobile:",mobile_num)
    print ("Pizza Selected:",sel_pizza)
    print ("Pizza topping:",sel_topping)
    print ("Total money to be paid:",pizza_base+pizza_topping)
    print("Thank you for shopping,Have a nice day")
    file = open(name_of_customer+'.txt','a')
    file.writelines("Name:")
    file.write(name_of_customer)
    file.writelines("Mobile:")
    file.write(mobile_num)
    file.writelines("Pizza Selected:")
    file.write(sel_pizza)
    file.writelines("Pizza topping:")
    file.write(sel_topping)
    # file.close()
    # pizza_topping.close()
    # pizza_variety.close()
pizza_order()