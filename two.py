import one

def two_fun():
    print ("this is the function present in two.py file")

one.one_func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")