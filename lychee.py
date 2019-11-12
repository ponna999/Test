# test = 1234567898760000
#
# for i in range(101,120):
#     print('<request xsi:type="spml:AddRequest">')
#     print("<version>~NSR_VERSION~</version>")
#     print('<object xsi:type="nsr:HLRImeisvWildCardList">')
#     print("<identifier>Test"+str(i)+"</identifier>")
#     print("<imeisvWildCard>1234567898760979</imeisvWildCard>")
#     print("</object>")
#     print ("</request>")


class Praneeth():
    company_name = "Maruthi"

    def __init__(self, vehicle, model, price):
        self.vehicle = vehicle
        self.model = model
        self.price = price

    def get_vehical_details(self):
        print("The person is having", Praneeth.company_name, self.vehicle, "and the make of the year is", self.model,
              "the price is", self.price)


# a = Praneeth('Car',2015,500000)
# print (a.model)
# print(a.vehicle)
# a.get_vehical_details()
# print(a.company_name)



class ClassA(object):
    def __init__(self):
        self.var1 = 1
        self.var2 = 2
    def method(self):
        self.var1 = self.var1 + self.var2
        return self.var1

class ClassB(ClassA):
    def __init__(self):
        ClassA.__init__(self)

# object1 = ClassA()
# sum = object1.method()
# object2 = ClassB()
# print (sum)


class Vehicle(object):
    def __init__(self,vehicle_name,vehicle_price,vehicle_model,vehicle_company):
        self.vehicle_name = vehicle_name
        self.vehicle_price = vehicle_price
        self.vehicle_model = vehicle_model
        self.vehicle_company = vehicle_company

    def start(self):
        print ("Started")

    def stop(self):
        print ("stopped")


class Car(Vehicle):

    def __init__(self,a,b,c,d):
        Vehicle.__init__(self,a,b,c,d)

    def run(self):
        print ("Running")

a = Car(123,12134,1212121,12121)


# class A:
#     def __init__(self):
#         print('Initializing: class A')
#
#     def sub_method(self, b):
#         print('Printing from class A:', b)
#
#
# class B(A):
#     def __init__(self):
#         print('Initializing: class B')
#         super().__init__()
#
#     def sub_method(self, b):
#         print('Printing from class B:', b)
#         super().sub_method(b + 1)
#
#
# class C(B):
#     def __init__(self):
#         print('Initializing: class C')
#         super().__init__()
#
#     def sub_method(self, b):
#         print('Printing from class C:', b)
#         super().sub_method(b + 1)
#
#
# if __name__ == '__main__':
#     c = C()
#     c.sub_method(1)