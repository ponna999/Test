import sys

def main():
    print("I am",sys.argv[1],"learning python")

def repeat(s,exclaim):
    """
    Repeat the string s for 3 times and
    add !!! if exclaim is true else don't add anything
    """
    result = s + s + s
    if exclaim:
        result = result + '!!!'
    return result

def main ():
    print (repeat('a',True))
    print (repeat('yes',False))

if __name__== '__main__':
    main()

