# Assignments on RE
# =================
import re

# 1) A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example: If the following passwords are given as input to the program:
# ABd1234@1, a F1#,2w3E*, 2We3345
# Then, the output of the program should be:ABd1234@1

def password_check():
    password = input("Enter the password:")
    if len(password) >= 6 and len(password) <= 12:
        if re.search(r'[A-Z]',password) and re.search(r'[a-z]',password) and re.search(r'[0-9]',password) and re.search(r'[@#$]',password):
            print ("Passowrd is valid")
        else:
            print("Password is not valid")
    else:
        print ("Password did not meet the length criteria")

# password_check()



# 2) Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
# Example: If the following email address is given as input to the program:anita@google.com
# Then, the output of the program should be: anita

def get_user_name():
    email = input("Enter the email ID:")
    a = re.search('\w*',email)
    print(a.group())

# get_user_name()

# 3) Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the
# company name of a given email address. Both user names and company names are composed of letters only.
# Example: If the following email address is given as input to the program:anita@google.com
# Then, the output of the program should be:google


def get_company_name():
    email = input("Enter the email ID:")
    a = re.search('@\w*',email)
    print(a.group())

# get_company_name()

# 4) Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
# Example: If the following words is given as input to the program:2 cats and 3 dogs.
# Then, the output of the program should be:['2', '3']

def get_digits():
    str = input("Enter the string:")
    a = re.findall('\d',str)
    print (a)

# get_digits()

# 5) Write a regular expression which matches a email address.

def match_email():
    email = input("Enter the email ID:")
    if re.search('\w.*\@\w.*\.\w',email):
        print ("valid email")
    else:
        print("Not a valid email")
# match_email()

# 6) Write a Python script to validate an IP address

def ip_validator():
    ip = input("Enter the ip:")
    if re.search('[0-2][0-9][0-9][:][0-2][0-9][0-9][:][0-2][0-9][0-9][:][0-2][0-9][0-9]',ip):
        print (ip,"Is valid")
    else:
        print (ip,"Is not  valid")
# ip_validator()

# 7) Write a Python script to validate a Date
def date_validator():
    enter_date = input("Enter the date:")
    if re.search('[0-3][0-9][-][0-1][0-9]-[0-9][0-9][0-9][0-9]',enter_date):
        print (enter_date,"Is valid")
    else:
        print (enter_date,"Is not  valid date")

# date_validator()

# 8) Write a Python script to validate a MAC Address

def mac_validator():
    mac_address = input("Enter the Mac Address:")
    if re.search('[0-9][A-Z][-][0-9][A-Z][-][A-Z][0-9][-][A-Z][0-9]-[A-Z][A-Z][-][0-9][0-9]',mac_address):
        print (mac_address,"Is valid mac address")
    else:
        print(mac_address, "Is not valid mac address")

# mac_validator()
# mac = 3C-6A-A7-D7-FE-56


# 9) Write a Python script to validate an URL




# 10) Write a Python Script that takes IP addess as input and check if the route for the same is present or not from above data



# 11) Write a Python Script to print all the numbers between the string.
# st1 = " some 192 has 63 and some has 40 and 5003 and 90"
# the output should be 192,63,40,5003,90

def extract_digits():
    st1 = input("Enter the string with digits:")
    a = re.sub(r'[^0-9]'," ",st1)
    # a = re.search(r'[^\W]',st1)
    print (a)
# extract_digits()


# 12) Write a Python script to read a file and collect all ip address in it.
# Eg : File contain:
# router 1 192.168.1.1 user name abc password 123hhc
# router2 12.1.2.1 username xyz password abb12
# route3 10.1.1.2 username xxa password aabba

# 13) Write a Python script to read a file and collect all email addresses. The file may contain lines as :
# Some lines have contact hck@tech.com
# all others contact kkc12@nic.com
# the file also contain email address like gma!12@gmail.com

def extract_email():
    # file = input("Enter the file name from which you want to extract email ID's:")
    nfile = open('email.txt','r')
    file_content = nfile.readlines()
    for i in file_content:
        if re.search('\w+.\w+@\w+.com',i):
            a = re.search('\w+.\w+@\w+.com',i)
            print (a.group())

# extract_email()

# 14) Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string is already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Eg : 'abc'   Expected Result : 'abcing'
# Eg : 'string' Expected Result : 'stringly'


def add_ing ():
    st = input("Enter the string:")
    if len(st) >= 3:
        if st.endswith('ing'):
            nst = st + 'ly'
            return nst
        else:
            nst = st + 'ing'
            return nst
# print(add_ing())