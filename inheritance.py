class Parent():
    def __init__(self,name,color):
        print ("Parent constructor is being called")
        self.last_name = name
        self.eye_color = color

    def show_info(self):
        print ("Last Name :- ", self.last_name)
        print("Eye Color :- ", self.eye_color)

class Child(Parent):
    def __init__(self,last_name,eye_color,toys):
        print ("Child constructor is being called")
        Parent.__init__(self,last_name,eye_color)
        self.num_of_toys = toys

    def show_info(self):
        print("Last Name :- ", self.last_name)
        print("Eye Color :- ", self.eye_color)
        print ("Number of Toys :- ", self.num_of_toys)

# test1 = Parent('guptha','black')
# test1.show_info()

# test = Child('guptha','black',5)
# test.show_info()


class Emp():
    """This class can be used to create emp details """
    emp_count = 0
    def __init__(self,name,salary):
        self.emp_name = name
        self.emp_salary = salary
        Emp.emp_count += 1

    def display_count(self):
        print (Emp.emp_count)
    def display_employee(self):
        print (self.emp_name,self.emp_salary)

test = Emp('guptha',10000)
# test.display_count()
test1 = Emp('Praneeth',5000)
# test1.display_employee()

print ("Employee.__doc__:", Emp.__doc__)
print ("Employee.__name__:", Emp.__name__)
print ("Employee.__module__:", Emp.__module__)
print ("Employee.__bases__:", Emp.__bases__)
print ("Employee.__dict__:", Emp.__dict__)