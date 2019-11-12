import random

# l = [1,2,3,4]
# m = [9,7,7]
# l.append(5)
# l.pop()
# l.extend(m)
# print (l)
#
# l.remove()


# li = []
# li = [i*i for i in range (1,10)]
# print (li)
#
# city = ['bang','mysore','hydera']
# z = [i[0] for i in city]
# print (z)

# list is mutable

# tuple is immutable
# tu  = (1,2,3)
# print (dir(tuple))


# str = 'praneth'
# str.fin
#
# l = [1,2,3,4,5,6,7,8]
# print (l[2:8])
#
#
# l = [1,2,3,4,5]
# sum = 0
# mul = 1
# for i in l:
#     sum  += i
#     mul *= i
# print (sum,mul)

# l = [1,2,3,4,5,6,7,8,8,8]
# nl =[]
# for i in l:
#     if i not in nl:
#         nl.append(i)
# print(nl)

# newfile = open('New.spml','w')
# for i in range (12111222000000,12111222000101):
#     newfile.write('<request xsi:type="spml:DeleteRequest">')
#     newfile.write("\n")
#     newfile.write('<version>LI_3GPPHSS_v10</version>')
#     newfile.write("\n")
#     newfile.write('<objectclass>Interception</objectclass>')
#     newfile.write("\n")
#     newfile.write('<identifier alias="imsi">')
#     newfile.write(str(i))
#     newfile.write('</identifier>')
#     newfile.write("\n")
#     newfile.write('</request>')
#     newfile.write("\n")
# newfile.close()


# 10) Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and
#     sorting them alphanumerically.
# 	Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again
# 	Then, the output should be: again and hello makes perfect practice world

#
# new = input("Enter the string:")
# new1 = new.split(" ")
# # print (new1)
# nl = []
# for i in new1:
#     if i not in nl:
#         nl.append(i)
# # print (emp)
# nl.sort()
# A=' '.join(nl)
# print(A)

# function
# ==========

# def Max(a,b):
#     if a == b:
#         print("both are same")
#     elif a > b:
#         print("max",a)
#     else:
#         print ("max",b)

# Max(2,3)
# Max(1,1)



# 8) Given a list of N numbers, use a single list comprehension to produce a new list that only contains even numbers from
# among those elements in the original list that have even indices. For example, if list[2] contains a value that is even,
# that value should be included in the new list, since it is also at an even index in the original list. However, if list[3] contains an even number,
# that number should not be included in the new list since it is at an odd index in the original list.

# def NewList(a):
#     even = []
#     b = len(a)
#     i = 0
#     while(i < b):
#         if a[i] % 2 == 0:
#             even.append(a[i])
#             i += 2
#         else:
#             i += 2
#     return even
# a = [2,3,4,8,8,6]
#
# print(NewList(a))

import turtle
from functools import reduce

from decorator import __init__


def draw_trianlge():
    window = turtle.Screen()
    window.bgcolor("yellow")
    gup = turtle.Turtle()
    gup.shape("turtle")
    gup.speed(1)
    gup.color("black")
    gup.left(45)
    gup.forward(100)
    gup.right(90)
    gup.forward(100)
    gup.right(135)
    gup.forward(130)

    window.exitonclick()


# draw_trianlge()

def draw_square():
    window = turtle.Screen()
    window.bgcolor("Green")
    gup = turtle.Turtle()
    gup.forward(100)
    gup.right(90)
    gup.forward(100)
    gup.right(90)
    gup.forward(100)
    gup.right(90)
    gup.forward(100)
    window.exitonclick()

# draw_square()


def draw_circle():
    window = turtle.Screen()
    gup = turtle.Turtle()
    window.bgcolor("Red")
    gup.color("yellow")
    gup.circle(100)
    window.exitonclick()
# draw_circle()


def draw_rectangle():
    gup = turtle.Turtle()
    window = turtle.Screen()
    window.bgcolor("Black")
    gup.color("Red")
    for i in range (1,37):
        for i in range (0,4):
            gup.forward(100)
            gup.right(90)
        gup.right(10)
    window.exitonclick()
# draw_rectangle()



# A = lambda x,y:x+y
# print (A(2,3))
#
# min = (lambda x,y: x if x<y else y)
# print (min(101*99,102*98))

# import os
# def cfile(filepath,ext):
#     file = 0
#     flist  = os.listdir(filepath)
#     for i in flist:
#         if i.endswith(ext):
#             file += 1
#     return file

import re
# phone = "2004-959-559 + this is phone number"
# a = re.sub(r'\D','',phone)
# print (a)

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


# from twilio.rest import Client
# #
# # account_sid = 'AC9ce5ccab7703e514fb666541695ebbde'
# # auth_token = 'cc0679397cde618f9edd9f2adae1fa68'
# # client = Client(account_sid, auth_token)
# # message = client.messages.create(body="Hi Hani I love you Darling.",from_='+13013580319',to='+91 9535347602')
# # print(message.sid)


# example of class variable and instance variable

class CSIT_Student():
    stream = "CSIT"
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
# a = CSIT_Student('Praneeth',1202)
# print (a.stream)
# print (a.name)
# print(a.roll)
# print (CSIT_Student.stream)


# example of changing class variable

class CSIT_Student():
    stream = "CSIT"
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

# a = CSIT_Student("praneeth",1202)
# b = CSIT_Student("Harini",1203)
# a.stream = "Degree"
# print (a.stream)
# print (b.stream)

# example of First Class functions in Python

#The below program tell's us that  We can assign one function to a variable and the same variable can be used just like a function

def shout(text):
    return text.upper()

# print (shout("Hi bro"))
# yell = shout
# print (yell("Hi Bro"))


# Functions can be passed as an argument

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(fun):
    a = fun("Hi this is the message that is being passed to other functions.")
    print (a)

# greet(shout)

# function can return to another function

def Test(x):
    def adder(y):
        return x+y
    return adder

a = Test(10)
# print (a(10))
# print (a(20))


# difference between str() and repr()


class Complex ():
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def __repr__(self):
        return 'Rational(%s,%s)'%(self.real,self.img)

    def __str__(self):
        return '%s + i%s'%(self.real,self.img)

# t = Complex(10,20)
# print (t.__str__())
# print (t.__repr__())


class sampleclass:
    count = 0  # class attribute

    def increase(self):
        sampleclass.count += 1

s1 = sampleclass()
s1.increase()
# print(s1.count)

# print (sampleclass.count)
# s2 = sampleclass()
# # print(s2.count)
# s2.increase()
# print(s2.count)

# print(sampleclass.count)

# Reflections are basically the below methods
# type(),isinstance(),callable(),dir(),getattr()

# name = ['praneeth','guptha','harini']
# marks = [90,91,89]
# roll = [1202,1203,1205]

# mapped = zip(name,roll,marks)
# mapped = set(mapped)
# print (mapped)


# polymorphism
#example 1

class Bird():
    def info(self):
        print ("There are many types of Birds.")
    def flight(self):
        print ("Most of them will fly and some of them will not.")
class Ostrich(Bird):
    def flight(self):
        print ("Ostrich can't fly.")
class Piegon(Bird):
    def flight(self):
        print ("Piegon can fly")

obj_bird = Bird()
obj_ostrich = Ostrich()
obj_piegon = Piegon()

# obj_ostrich.info()
# obj_ostrich.flight()
#
# obj_piegon.info()
# obj_piegon.flight()

# example 2

class India():
    def capital(self):
        print ("Delhi is the captial of INDIA.")
    def type(self):
        print ("INDIA is a developing country.")
    def language(self):
        print ("Telugu is the national language.")

class Us():
    def capital(self):
        print ("Washington D.C. is the captial of US.")
    def type(self):
        print ("US is a developed country.")
    def language(self):
        print ("English is the national language.")

obj_india = India()
obj_us = Us()

# for country in (obj_india,obj_us):
#     country.capital()
#     country.language()
#     country.type()


class A:
    def __init__(self, a):
        self.a = a
    def __add__(self, o):
        return self.a + o.a
# obj = A(1)
# obj1 = A(2)
# print (obj + obj1)

# for i in range(1,101):
#     if i > 1:
#         for b in (2,i):
#             if (i%b == 0):
#                 break
#             else:
#                 print (i)

# while True:
#     try:
#         n=input("Enter an integer:")
#         n = int(n)
#         break
#     except ValueError:
#         print ("No valid integer passed to the program!")
# print ("Good You have entered integer....")



# try:
#     new_file = open('New.txt','r')
#     new_file.read()
# except IOError:
#     print "ERROR: file is not present"
# else:
#     print "Reading file is successfull.."
# new_file.close()


# import sys
#
# while True:
#     try:
#         x = int(input("Enter the number:"))
#         r = float(1)/float(x)
#         break
#     except:
#         print (sys.exc_info()[0])
#         print ("Try again")
# print (r)



Gold={'Australia':100, 'France':75, 'Germany':34}
Silver={'Japan':24, 'Australia':65,'France':33}
Bronze={'Germany':100, 'Japan':10, 'Australia':45}
new = {}

for i in Gold:
    if i not in new:
        new[i] = Gold.get(i)
    # print (new)
for i in Silver:
    if i in new:
        new[i] = new.get(i) + Silver.get(i)
    else:
        new[i] = Silver.get(i)
for i in Bronze:
    if i in new:
        new[i] = new.get(i) + Bronze.get(i)
    else:
        new[i] = Bronze.get(i)
# print ("Total nuber of medal for each country:")
# for i in new:
#     print (i, '\t', new.get(i))

# Solution 2

Gold={'Australia':100, 'France':75, 'Germany':34}
Silver={'Japan':24, 'Australia':65,'France':33}
Bronze={'Germany':100, 'Japan':10, 'Australia':45}

new ={}
def dict_add(a):
    for i in a:
        if i not in new:
            new[i] = a.get(i)
        else:
            new[i] = a.get(i) + new.get(i)
    return new


# dict_add(Gold)
# dict_add(Silver)
# print (dict_add(Bronze))


# swap the elements in a list
import sys

SL=[[70,80,90],[40,50,60],[10,20,30],[20,30,40]]

def swapPositions(SL, pos1, pos2):
    try:
        if (len(SL) - 1) <= pos1:
            pass
        elif (len(SL)-1)<= pos2:
            pass
        else:
            exit
        SL[pos1], SL[pos2] = SL[pos2], SL[pos1]
        return SL
    except:
        print (sys.exc_info()[0])
        exit()

# print (swapPositions(SL,0,5))




# Program to find out whether the given number is even or odd

# try:
#     num = int(input("Enter the number:"))
#     if num < 0:
#         exit()
#     elif num % 2 == 0:
#         print (num,"is even:-)")
#     else:
#         print (num,"is odd:-(")
# except:
#     print (sys.exc_info()[0])
#     print ("The entered number must be greater than 0:",num)

def test(*var):
    for i in var:
        print (i)

# test(1,2,3,4,5,6,7,8)


# import library
import math, random


# function to generate OTP
def generateOTP():
    # Declare a digits variable
    # which stores all digits
    digits = "0123456789"
    OTP = ""

    # length of password can be chaged
    # by changing value in range
    for i in range(6):
        # print (i)
        OTP += digits[math.floor(random.random()*10)]

    print (OTP)
# generateOTP()
string = '1234567890ASDFGHJKLQWERTYUIOPZXCVBNMqwertuopasdgjklzxcvbnm'
# length = len(string)
# otp = ""
# for i in range(6):
#     otp += string[math.floor(random.random()*length)]
# print (otp)

# import turtle
# window = turtle.Screen()
# # window.bgcolor("yellow")
# a = turtle.Turtle()
# a.forward(250)
# a.left(90)
# a.forward(300)
# a.left(90)
# a.forward(250)
# a.left(90)
# a.forward(300)
# a.left(90)
# a.forward(250/10)
# a.left(90)
# a.forward(300)
# a.right(90)
# a.forward(250/10)
# a.right(90)
# a.forward(300)
# a.left(90)
# a.forward(250/10)
# a.left(90)
# a.forward(300)
# a.right(90)
# a.forward(250/10)
# a.right(90)
# a.forward(300)
# a.left(90)
# a.forward(250/10)
# a.left(90)
# a.forward(300)
# a.right(90)
# a.forward(250/10)
# a.right(90)
# a.forward(300)
# a.left(90)
# a.forward(250/10)
# a.left(90)
# a.forward(300)
# a.right(90)
# a.forward(250/10)
# a.right(90)
# a.forward(300)
# a.left(90)
# a.forward(250/10)
# a.left(90)
# a.forward(300)
# a.right(90)
# a.forward(250/10)
# a.right(90)
# a.forward(300)
#
# a.right(180)
# a.forward(300/10)
# a.left(90)
# a.forward(250)
# a.right(90)
# a.forward(300/10)
# a.right(90)
# a.forward(250)
#
# a.left(90)
# a.forward(300/10)
# a.left(90)
# a.forward(250)
#
# a.right(90)
# a.forward(300/10)
# a.right(90)
# a.forward(250)
#
# a.left(90)
# a.forward(300/10)
# a.left(90)
# a.forward(250)
#
# a.right(90)
# a.forward(300/10)
# a.right(90)
# a.forward(250)
# a.left(90)
# a.forward(300/10)
# a.left(90)
# a.forward(250)
#
# a.right(90)
# a.forward(300/10)
# a.right(90)
# a.forward(250)
#
# a.left(90)
# a.forward(300/10)
# a.left(90)
# a.forward(250)
#
# a.right(90)
# a.forward(300/10)
# a.right(90)
# a.forward(250)
#
#
# window.exitonclick()

# for i in range (101,102):
#     for j in range (1,11):
#         print  (i-j,end=" ")
#     print ()
#
# for i in range (81,91):
#     print (i,end=" ")
# print ()
#
# for i in range(81,82):
#     for j in range (1,11):
#         print  (i-j,end=" ")
#     print ()
#
# for i in range (61,71):
#     print (i,end=" ")
# print ()
#
# for i in range(51,52):
#     for j in range (1,11):
#         print  (i-j,end=" ")
#     print ()
#
# for i in range (41,51):
#     print (i,end=" ")
# print ()
#
# for i in range(31,32):
#     for j in range (1,11):
#         print  (i-j,end=" ")
#     print ()
#
# for i in range (21,31):
#     print (i,end=" ")
# print ()
#
# for i in range(21,22):
#     for j in range (1,11):
#         print  (i-j,end=" ")
#     print ()
# for i in range (1,11):
#     print (i,end="  ")


# a = turtle.Turtle()
# b = turtle.Screen()
# a.forward(200)
# a.right(90)
# a.forward(20)
# a.right(90)
# a.forward(200)
# a.right(90)
# a.forward(20)
# b.exitonclick()

import time
import threading
import sys

# def sleeper(i):
#     print ("thread sleeps for 5 seconds",i)
#     time.sleep(5)
#     print ("thread woke up after 5 seconds",i)
#
# for i in range(10):
#     t = Thread(target=sleeper,args=(i,))
#     t.start()

# Factorial with threading

# def fact(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     print(fact)
#
# try:
#     n = int(input("Enter the number:"))
#     if n > 1:
#         for i in range(1, n + 1):
#             t = threading.Thread(target=fact, args=(i,))
#             t.start()
# except:
#     print("entered number should be greater than zero")
#     print (sys.exc_info()[0]

import paramiko
def ssh(ip, port, username, password, cmd):
    try:
        ssh = paramiko.SSHClient()  # ??ssh??
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=int(port), username=username, password=password, )
        stdin, stdout, stderr = ssh.exec_command(cmd, timeout=100)
        result = stdout.read()
        result1 = result.decode()
        error = stderr.read().decode('utf-8')

        if not error:
            ret = {"ip": ip, "data": result1}
            ssh.close()
            print(ret)
    except Exception as e:
        error = "???????,{}".format(e)
        ret = {"ip": ip, "data": error}
        print (ret)

# ssh('192.168.103.67',22,'provgw','provgw1','sh /opt/provgw/tomcat/bin/run_as_provgw.sh status')

# import requests
#
# url = "http://192.168.103.67:8081/ProvisioningGateway/services/SPMLMultiappSubscriber10Service"
# body = """<?xml version="1.0" encoding="UTF-8"?>
# <spml:modifyRequest xmlns:spml="urn:siemens:names:prov:gw:SPML:2:0" xmlns:subscriber="urn:siemens:names:prov:gw:MULTIAPPSUBSCRIBER:1:0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
#   <version>MULTIAPPSUBSCRIBER_v10</version>
#    <objectclass>Subscriber</objectclass>
#    <identifier>262019900000050</identifier>
# 	 <modification name="hlr[@imsi='262019900000050']/extendedRoamSubscription[@priorityOrder='2']" operation="remove" scope="uniqueTypeMapping">
# 	 </modification>
#   </spml:modifyRequest>"""
# response = requests.post(url,body)
# print (response)


# import requests
# from suds.transport.http import HttpAuthenticated
# from suds.transport import Reply, TransportError
#
# class RequestsTransport(HttpAuthenticated):
#     def __init__(self, **kwargs):
#         self.cert = kwargs.pop('cert', None)
#         # super won't work because not using new style class
#         HttpAuthenticated.__init__(self, **kwargs)
#
#     def send(self, request):
#         self.addcredentials(request)
#         resp = requests.post(request.url, data=request.message,
#                              headers=request.headers, cert=self.cert)
#         result = Reply(resp.status_code, resp.headers, resp.content)
#         return result



# import socket
# import sys
# try:
#     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     print ("socket successfully created")
# except socket.gaierror:
#     print ("Socket creations is unsuccessfull....")
#
# port = 80
# try:
#     host_ip = socket.gethostbyname('www.facebook.com')
# except socket.gaierror:
#     print ("There was a problem resolving the host")
#
# s.connect((host_ip,port))
# print ("the socket has succesfully connected to facebook on port == %s"%(host_ip))


"""Multi threading program example"""

import threading
import os


def task1():

    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print ("The process ID of the thread: {}".format(os.getpid()))

def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print ("The process ID of the thread: {}".format(os.getpid()))


# if  __name__ == "__main__":
#     print("The process ID of the thread: {}".format(os.getpid()))
#     print("Main thread name:{}".format(threading.main_thread().name))
#     t1 = threading.Thread(target=task1(), name='t1')
#     t2 = threading.Thread(target=task2(), name='t2')
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()


##############################################################################
#                           List comprehensions                              #
##############################################################################
#
# mylist = [x if (x%2 == 0) else "odd" for x in range(1,10) ]
# print (mylist)
#
# newlist = [x*y for x in [2,4,6] for y in [100,200,400]]
# print (newlist)


def myfunc(a):
    newstring = ""

    for i in range(0,len(a)):
        if i%2 == 0:
            newstring += a[i].upper()
        else:
            newstring += a[i].lower()
    print (newstring)
# myfunc('gupta')

def lesser_of_two(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
# print(lesser_of_two(9,7))

def animal_checker(a,b):
    if a[0] == b[0]:
        return True
    else:
        return False
# print (animal_checker('lion','lepard'))
# print (animal_checker('lion','Tiger'))

def make_twenty(a,b):
    return a+b == 20 or a==20 or b==20
# print (make_twenty(1,10))


def captialize(a):
    first = a[:3]
    second = a[3:]
    return first.capitalize()+second.capitalize()
# print (captialize('praneeth'))

def master_yoda(word):
    word = word.split()
    word = word[::-1]
    return " ".join(word)

# print(master_yoda('I am on the way'))

def almost_there(num):
    return (abs(100-num) <=10) or (abs(200-num) <=10)
# print (almost_there(90))


def has_33(a):
    for i in range(0,len(a)-1):
        if a[i:i+2] == [3,3]:
            return True
    return False
a = [1,1,3,3]
# print(has_33(a))

def paper_doll(a):
    temp=""
    for i in a:
        temp = temp + i*3
    print (temp)
# paper_doll('guptha')

def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <=31:
        return sum([a,b,c])-10
    else:
        return "BUST"
# print (blackjack(9,9,11))

def summer_69(a):
    sum = 0
    for i in a:
        if i in[6,7,8,9]:
            pass
        else:
            sum += i
    return sum
# print (summer_69([1,3,5]))
# print (summer_69([4,5,6,7,8,9]))
# print (summer_69([2,1,6,9,11]))

def spy_game(a):
    code = [0,0,7,'x']
    for i in a:
        if i == code[0]:
            code.pop(0)
    return len(code) == 1
# print(spy_game([1,2,3,4,0,0,7,1]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))

def prime_checker(num):
    if num < 2:
        return False
    for i in range (2,num):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print (i,"is a prime number ")

# prime_checker(10)



def prime_counter(num):
    if num < 2:
        return "The num must be greater than or equal to 2"
    count = 0
    for i in range(2, num):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            count += 1
    return count
# print(prime_counter(10))

def print_name():
    a = input("Enter the name")
    print ("Hi {} how r u doing".format(a))

# print_name()
# for i in range (1,11):
    print (i)

# MAP Function#

def square(num):
    return num ** 2
# print (square(2))

my_list = [1,2,3,4,5]

# for i in my_list:
#     print (square(i))
# print(list(map(square,my_list)))

# Filter function#

def check_even(num):
    return num%2 == 0

my_list1 = [1,2,3,4,5,6]

# print(list(filter(check_even,my_list1)))

# lambda function using map and filter#

# print(list(map(lambda num:num**2,my_list)))

# print(list(filter(lambda num:num%2 == 0,my_list1)))

mystr = ['apple','ball','cat']

# print(list(map(lambda first_char:first_char[0],mystr)))

# find the volume of a spehere given a radius

def volume(r):
    return 4/3*22/7*r**3
# print(volume(2))

# function to check whether the given number is in range

def range_check(num,low,high):
    if  num in range(low,high):
        return True
    else:
        return False
# print(range_check(5,1,10))

# write a function to find out the upper letter and lower letters given a string#

def up_low(s):
    up = 0
    low = 0
    for i in s:
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
        else:
            continue
    return up,low
# print(up_low('Hello Mr. Rogers,how  are you this fine Tuesday?'))

# write a function that takes input as a list and returns a new list with contains only unique list#
a = [1,1,1,1,2,2,2,3,3,3,3,4,4,4,5,5,6,7,7,8,9]

def unique_list(a):
    return set(a)
# print(unique_list(a))

# Write a python function that multipy all the elements in a list#

def multiply(a):
    mul = 1
    for i in a:
        mul *= i
    return mul

# print(multiply([1,2,3,-4]))


# write a python function to check whether the given sting is a palindrome or not#
def palindrome(a):
    return a == a[::-1]

# print(palindrome('abc'))

# write a panagram to check whether a given sentence is a panagram or not

import string
def pangram(a,alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(a.lower())

# print(pangram("The quick brown fox jumps over the lazy dog"))

# num =-1
# if num in range(1,10):
#     print(True)
# else:
#     print (False)

def player_input():
    marker = input("Enter the player input X or O: ")
    if marker.lower() == 'x':
        return ('x','o')
    else:
        return ('o', 'x')
# play1,play2 = player_input()
# print (play1)
# print(play2)


# Class #
import math
class Line():
    def __init__(self,cord1,cord2):
        self.cord1 = cord1
        self.cord2 = cord2
    def slope(self):
        x1,y1 = self.cord1
        x2,y2 = self.cord2
        return (y2-y1)/(x2-x1)
    def distance(self):
        x1, y1 = self.cord1
        x2, y2 = self.cord2
        return math.sqrt(((x2- x1)**2)+((y2- y1)**2))

coordinate1 = (3,2)
coordinate2 = (8,10)

l = Line(coordinate1,coordinate2)
# print (l.slope())
# print(l.distance())

###########
class Cylinder:
    pi = 3.14
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi*(self.radius**2)*self.height

    def surface_area(self):
        return 2*Cylinder.pi*self.radius*self.height + 2* Cylinder.pi* self.radius**2

# c = Cylinder(2,3)
# print(c.volume())
# print(c.surface_area())

# BANK Account program using class

class Account():

    def __init__(self,Owner,Balance):
        self.Owner = Owner
        self.Balance = Balance

    def deposit(self,amount):
        self.Balance += amount
        print ("Amount Deposited and the total balance in the account is {}".format(self.Balance))

    def withdrawl(self,amount):
        if  self.Balance < amount:
            print ("Insufficient balance")
        else:
            self.Balance -= amount
            print ("Withdrawl accepted and the remaining balance in you account is {}".format(self.Balance))

acc = Account('guptha',100)
# print (acc.Owner)
# print (acc.Balance)
# acc.deposit(50)
# acc.withdrawl(160)
# acc.withdrawl(140)

# Exception handling#

# try:
#     for i in ['a','b','c']:
#         print(i**2)
# except TypeError:
#     print ("Integer can't be multiplied with string..")

# # problem 2

# x = 5
# y = 0
# try:
#     z = x/y
# except ZeroDivisionError:
#     print ("you can't devide any number with 0 times..")
# finally:
#     print ("All Done")

# Problem 3


def ask():
    waiting  = True
    while waiting:
        try:
            num = int(input("Enter the number to get the square of it:"))
        except ValueError:
            print ("Please enter a number")
        else:
            waiting = False

    print("{} square is:".format(num),square(num))

# ask()

# passing function to another function

def func():
    return "Hi this func() is being called.."

def calling_func(a):
    print ("calling_func is being executed")
    print(func())

# calling_func(func)

# returning a function

def hello(name= 'Gupta'):
    print ("hello() is being executed")
    def greet():
        return '\t hi this is greet ()'
    def welcome():
        return '\t hi this is welcome()'
    if name == 'Gupta':
        return greet
    else:
        return welcome

# new = hello()
# print(new())

def retrurn_func():
    print ("this is the main function")
    def hi():
        return ("Hi function is being returned")
    return hi()
# retrurn_func()

# Decorator


def deocrator (a):
    def wrap():
        print ("we are doing decorator for the function")
        a()
        print("we are doing post decorator for the function")
    return wrap

def fun_dec():
    print ("This is the function which is being decorated")

# new_dec = deocrator(fun_dec)
# new_dec()

@deocrator
def fun_dec():
    print ("This is the function which is being decorated")

# fun_dec()

# Generator

def cubes(n):
    # cube_list = []
    for i in range(n):
        yield i**3

# for i in cubes(10):
#     print (i)

# print(list(cubes(10)))

def fib(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        a,b = b,a+b
# for i in fib(5):
    print (i)


# a = 'Gaurav'
# b = iter(a)


# Create a generator which takes integer as an input and gives the sqare of it

def sqr(a):
    for i in range(a):
        yield i**2
# for i in sqr(10):
    print(i)

#Generate a random number b/w the range

def random_num(a,b):
    for i in range (a,b):
        yield random.randint(a,b)

# for i in random_num(1,10):
    print(i)

# Iter()

s = 'hello'
s_itr = iter(s)
# print(next(s_itr))

from collections import Counter

li = [1,1,1,1,1,1,1,1,1,2,3,2,3,2,43,2,4,2,3,1,4,4,3,33,3,3,3,3,3]
# print(Counter(li))

s = 'praneethguptha'
# print (Counter(s))

from collections import defaultdict

d = defaultdict(lambda:0)
d['one']
d['two']
d['three'] = 3
# print (d)


d = {}
d['a'] = 1
d['e'] = 5
d['b'] = 2
d['c'] = 3
d['d'] = 4

# for k,v in d.items():
#     print (k,v)

from collections import OrderedDict

E = OrderedDict()
E['a'] = 1
E['e'] = 5
E['b'] = 2
E['c'] = 3
E['d'] = 4

# for k,v in d.items():
#     print (k,v)
# print(d == E)


from collections import namedtuple

dog = namedtuple('dog','age breed sex eat')
doggy = dog(age=5,breed= 'street',sex = 'M',eat = 'Meat')
# print (doggy)
# print (doggy.sex)

import pdb

a = 5
b = 4
c = [1,2,3]
# print (a+b)
# pdb.set_trace()
# print (c+b)


import timeit

# print(timeit.timeit(('-'.join(str(i) for i in range(100))),number=10000))

# print ("-".join([str(i) for i in range(100)]))

a = 'praneeth'
b = 'guptha'

# print(type("-".join([str(i) for i in range(100)])))

s = (1,2)
# print (s[1])


def fun1(x,y):
    return x,y


def fun2(fun):
    a,b = fun[0],fun[1]
    c = a+b
    return c

#
# a = fun2(fun1(10,9))
# print (a)


# Convert binary digit to hexa decimal

def convert_to_hexa():
    num = int(input("Enter the number which you want to convert to hexadecimal.."))
    return hex(num)

# print (convert_to_hexa())

a =5.23222
# print (round(a,2))

s = 'hello how are you Mary, are you feeling okay?'
# print(s.islower())
# s = s.split(' ')
# for i in s:
#     if i.islower():
#         print (i,"is lower")
#     else:
#         print (i, "is upper")

s = 'twtwtwtwtwtwtwtwtwtwtwtwtwtwt'
# print (s.count('w'))

set1 = {2,3,1,5,6,8}
set2 ={3,1,7,5,6,8}

# print(set1.difference(set2))

# print (set1.union(set2))

# print({x:x**3 for x in range(5)})

import subprocess,os

# print(os.listdir('D:\EE cloud videos'))
# print(os.getcwd())

# cmd = 'git --version'
# a = os.system(cmd)
# print('a:',a)

# a = subprocess.call(cmd,shell=True)
# print('a:',a)

import subprocess
def run_win_cmd(cmd):
    result = []
    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    for line in process.stdout:
        result.append(line)
    errcode = process.returncode
    for line in result:
        print(line)
    if errcode is not None:
        raise Exception('cmd %s failed, see above for details', cmd)

# run_win_cmd('dir')

from ipywidgets import interact,interactive,fixed
import ipywidgets as widgets

def guptha(x):
    return x
# interact(guptha,x='hello')

# @interact(x=5,y=1)
def g(x,y):
    return(x,y)

# interact(guptha,x=['hello','hi','how'])

from IPython.display import display

def f(a,b):
    display(a+b)
    return a+b

w = interactive(f,a=10,b=20)
# display(w)

# for i in range(1,11):
#     print(random.randint(1,10))


# class Test():
#     def __init__(self,a):
#         self.a = a
#     def set_value(self,a):
#         self.a = a
#         # return self.a
#
# class Child(Test):
#     def __init__(self,a,b,c):
#         Test.__init__(self,a)
#         self.b = b
#         self.c = a
#     def sum_value(self):
#         return self.a + self.b + self.c
#
# a = Child(1,2,1)
# print (a.sum_value())
# a.set_value(10)
# print (a.sum_value())

# try:
#     a = int(input("Enter the number:"))
#     b = int(input("Enter the number:"))
#     print (a+b)
# except:
#     print(sys.exc_info()[1])
# finally:
#     print ("I am being executed at an case")


# try:
#     for i in ['a', 'b', 'c']:
#         print(i**2)
# except TypeError:
#     print ("string can't be multiplied with an integer!!!")


# try:
#     x = 5
#     y = 0
#     z = x/y
# except ZeroDivisionError:
#     print ("You can't divide by zero")

# def ask():
#     while True:
#         try:
#             a = int(input("Enter an integer to get the square of it: "))
#         except:
#             print ("Enter only integer!!!!")
#             continue
#         else:
#             break
#     print (a**2)
#
# ask()


l = [True,True,True,True,True,False]
# print (any(l))
# print (all(l))

a = 'how long are the words in this phrase'

# def word_len(phrase):
#     return list(map(len,phrase.split()))
#
# print (word_len(a))

# b = a.split()
# print (list(map(len,b)))


def digits_to_num(digits):
    return reduce(lambda x,y :x*10 +y,digits)
# print(digits_to_num([3,4,3,2,1]))


def filter_words(word_list,letter):
    b = []
    for i in word_list:
        if i[0] == letter:
            b.append(i)
    return b
# l = ['hello','hi','how','test','guptha','sumit','mav']
# print (filter_words(l,'h'))


# l = [1,2,3,4,5,6,7,8]

# for count,value in enumerate(l):
#     print (count,value)


# l = ['a','b','c']
# def d_list(l):
#     return {value:key for key,value in enumerate(l)}
# print (d_list(l))


l = [0,1,2,2,1,5,5,6,10]

def count_match(l):
    a = 0
    for count,num in enumerate(l):
        if count == num:
            a += 1
    return a
# print (count_match(l))

# i = 26201990000001
# for j in range (1,101):
#     sum = i + j
#     print ("<eirAllowedIMEI>",sum,"</eirAllowedIMEI>")

# a = 2
# print (a)
# print (id(a))
# a = a + 1
# print (id(a))

#
# a = [1,2,3,4,5,6,2,1,5]
# Length = len(a)
# sum = 8
#
# for i in a:
#     if i < sum:
#         for j in a[a.index(i)+1:]:
#             for k in a[a.index(j)+1:]:
#                 if i + j + k == 8:
#                     print (i,j,k)


a = [[1,2,3],[4,5,6],[7,8,9]]
b =[[0,0,0],[0,0,0],[0,0,0]]

f = open('Number.txt','r')
b = f.readlines()
sum = 0

for i in range (1,len(b) -1):
    sum = sum + i
# print (sum)


import re
a ='praneeth,guptha.amarana,satish.potnuru'


str = a.replace(',','*')
str = str.replace('.',',')
str = str.replace('*','.')
# print (str)

a = 'praneeth'
new_list = []
for i in a:
    new_list.append(i)
# print (new_list)
# print (type(new_list))



a = 'praneethguptha amarana'
tot_vowles = 0
vowels = ['a','e','i','o','u']
for i in a:
    if i in vowels:
        # print (i)
        tot_vowles = tot_vowles + 1
    else:
        continue
# print (tot_vowles)

# a = ord('A')
# print (a)

List = ['Geeks', 'For']
# print("\nMulti-Dimensional List: ")
# print(List)

# print (List[0])


List.insert(0,(10,5))
# print (List[0][0])

a = [1,2,3,4]
b = [5,6,7,8]

# List of strings
l = ['sat', 'bat', 'cat', 'mat']


# test = list(map(list, l))
# print (test)

li = [1,1]
ti =(1,1)
di = {ti:2 }
# print (di.keys())

s1 = set('geeksforgeeks')
# print(s1)

s1 = set()

s1.add(1)
s1.add(1)
s1.add(2)
s1.add(3)
s1.add(4)
s1.add(5)
s1.add(6)
# print (s1)

d1 = {1:'praneeth',2:'guptha',3:'hani'}
d1[4]='nirvaan'
d1[1]='satish'
# print(d1)

#
# dict1 = {1:'a',2:'b',3:'c'}
# dict1[4] = 'd'
# dict2 = {}
# dict2.update(dict1)
# print (dict2)
# # print (dict1)
# dict2.pop(1)
# print (dict2)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.setdefault('color', 'white')
# print (car)

import array

arr = array.array('B',[1,2,2,3,3])
arr1 = array.array('B',[1,2,3])
arr1.extend(arr)
# print (arr1)
# print (arr)
# arr.append(4)
# for i in range (0,6):
#     print(arr[i],end=" ")

# print (arr.itemsize)

def test():
    global s
    print (s)
    s = "Me too"
    print (s)
s = "this is praneeth"
#
# test()
# print (s)

# print (5/2)
# print (-5/2)
# print (5.0/2)
# print (-5.0/2)


class complex:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self,others):
        return self.a + others.a, self.b + others.b

    def __str__(self):
        return self.a,self.b

ob1 = complex(1,2)
ob2 = complex(2,3)
# print(ob1 + ob2)

import operator
a = 1
b = 2
z = operator.add(a,b)
# print (z)

a = [1,2,3,4,5,6]
z = operator.add(a,[1,2,3])
# print (z)
# print (a)

p = operator.iadd(a,[1,2,3])
# print (p)
# print (a)



def switch(a):
    switcher = {0:'zero',1:'one',2:'two'}
    return switcher.get(a,'nothing')
# print (switch(1))

cars = ["Aston" , "Audi", "McLaren "]
repair = ['gps','toolkit','tyree']
# for i,x in enumerate(cars):
    # print (i,x)

# for a,b in zip(cars,repair):
#     print (a,b)

a,b =  zip(*[('Aston', 'GPS'),('Audi', 'Car Repair'),('McLaren', 'Dolby sound kit')])
# print(a)
# print(b)

class Test:
    def __init__(self,limit):
        self.limit = limit
    def __iter__(self):
        self.x = 10
        return self
    def __next__(self):
        x = self.x
        if x > self.limit:
            raise StopIteration
        self.x  = x + 1;
        return x

# for i in Test(2000):
#     print (i)

import itertools
a = [1,2,3,4,5,6,7,8,9]
la = iter(a)

b = itertools.tee(la,3)
# print (b[0])

# print (list(itertools.permutatiprint (list(itertools.permutations('GfG',2))) ons('GfG',0)))


# for i in itertools.count(5,2):
#     if i < 100:
#         print (i)
#     else:
#         break

# for i in itertools.cycle([1,2,3,4]):
    # print (i)

# for i in itertools.repeat([1,2,3,4,5],6):
#     print (i)


# print (list(itertools.product('gef','str')))
# print (list(itertools.product('123','123')))
#
# print (list(itertools.combinations('1234',2)))
#
# print (list(itertools.permutations('1234',2)))
#
# print (list(itertools.combinations_with_replacement('1234',2)))

#
# def fib(limit):
#     a = 0
#     b = 1
#     count = 0
#     while count < limit:
#         print (a,end=" ")
#         a,b = b,a+b
#         count +=1
# fib(5)

def simpleGenfun():
    yield 1
    yield 9
    yield 2
# for i in simpleGenfun():
#     print (i)
# x = simpleGenfun()
# print (x.__next__());
# print (x.__next__());
# print (x.__next__());


def fib(limit):
    a,b =0,1
    while a < limit:
        yield a
        a,b = b,a+b
x = fib(5)
# print (x.__next__())
# print (x.__next__())
# print (x.__next__())
# print (x.__next__())
# print (x.__next__())


def create_adder(x):
    def adder (y):
        return x+y
    return adder

add_15 = create_adder(15)

# print (add_15(20))

# def speak(text):
#     return text.lower()
#
# def shout(text):
#     return text.upper()
#
# def greeting(fun):
#     some = fun("hi i am learning something new")
#     print (some)
#
# greeting(speak)
# greeting(shout)

#
# def shout(text):
#     return text.upper()
# print (shout('hi'))
#
# yell = shout
# print (yell('hi'))

#
# import logging
# logging.basicConfig(filename='example.log', level=logging.INFO)
# def logger(func):
#     def log_func(*args):
#         logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
#         print(func(*args))        # Necessary for closure to work (returning WITHOUT parenthesis)
#     return log_func
# def add(x, y):
#     return x + y
# def sub(x, y):
#     return x - y
# add_logger = logger(add)
# sub_logger = logger(sub)
# add_logger(3, 3)
# add_logger(4, 5)
# sub_logger(10, 5)
# sub_logger(20, 10)

# def test_decoratot(func):
#     def some_func(x):
#         return x + 2
#     return some_func
#
# def some(y):
#     return y
# some = test_decoratot(some)
# print (some(1))

# def our_decorator(func):
#     def function_wrapper(x):
#         print("Before calling " + func.__name__)
#         func(x)
#         print("After calling " + func.__name__)
#     return function_wrapper
#
# @our_decorator
# def foo(x):
#     print("Hi, foo has been called with "+ x)
#
# foo("Hi")

# from random import choice
# for i in range (1,10):
#     print (choice([1,2,3,4,5,6,7,8,9,0]))

# def argument_test_natural_number(f):
#     def helper(x):
#         if type(x) == int and x > 0:
#             return f(x)
#         else:
#             raise Exception("Argument is not an integer")
#
#     return helper
#
#
# @argument_test_natural_number
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# # for i in range(1, 10):
# #     print(i, factorial(i))
#
# print(factorial(3))
#
#
# fact = 1
# n = int(input("Please enter the number for which you want factorial:"))
# for i in range (1,n+1):
#     fact = fact * i
# print (fact)

def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    return helper

@call_counter
def succ(x):
    return x + 1

@call_counter
def mul1(x, y=1):
    return x * y + 1

# print (mul1(3, 4))
# mul1(4)
# mul1(y=3, x=2)

# print(succ.calls)

# def evening_greeting(func):
#     def function_wrapper(x):
#         print("Good evening, " + func.__name__ + " returns:")
#         func(x)
#     return function_wrapper
#
# def morning_greeting(func):
#     def function_wrapper(x):
#         print("Good morning, " + func.__name__ + " returns:")
#         func(x)
#     return function_wrapper
#
# @evening_greeting
# def foo(x):
#     print(42)
#
# # foo(1)


# def greeting(expr):
#     def greeting_decorator(func):
#         def function_wrapper(x):
#             print(expr + ", " + func.__name__ + " returns:")
#             func(x)
#         return function_wrapper
#     return greeting_decorator
#
#
# def foo(x):
#     print(42)
#
# greeting2 = greeting("καλημερα")
# foo = greeting2(foo)
# foo("Hi")


# def simple(expr):
#     def simple_decorator(func):
#         def wrapper_function(x):
#             print (expr + " I am the decorator getting executed inside a function")
#             func(x)
#         return wrapper_function
#     return simple_decorator
#
#
# def test(x):
#     print ("Hello")
#
# simple1 = simple("Hi")
# test = simple1(test)
# test(1)



# def simple(expr):
#     def simple_decorator(func):
#         def wrapper_function(x):
#             print (expr + "This is the expression that is passed to decorator!!!!")
#             print(func(x))
#         return wrapper_function
#     return simple_decorator
#
# @simple("Praneeth")
# def test(x):
#     return 42
# test(x)
#
# from functools import wraps
#
# def greeting(func):
#     @wraps(func)
#     def function_wrapper(x):
#         """ function_wrapper of greeting """
#         print("Hi, " + func.__name__ + " returns:")
#         return func(x)
#     return function_wrapper
#
# @greeting
# def test(x):
#     """Hi this is silly documentation"""
#     print ("I am using wrap function")
#
# test("hi")
# print ("function name: " + test.__name__)
# print ("module name: " + test.__module__)
# print ("documentation: "+  test.__doc__)


#
# class decorator2:
#     def __init__(self,f):
#         self.f = f
#
#     def __call__(self):
#         print ("decorating", self.f.__name__)
#         self.f()
# @decorator2
# def test():
#     print("I am being called from a class")
#
# test()

# demo = iter(range(6))
# for i in demo:
#     print (i)


# class data():
#     name = "no name"
#     age = 0
#
# def main():
#     my = data()
#     my.name = "praneeth"
#     my.age = 16
#     print ("Name: " + my.name + " " + "Age:",my.age)
#
# if __name__ == '__main__':
#     main()


# class Reverse():
#     def __init__(self,data):
#         self.data = data
#         self.index = len(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index -= 1
#         return self.data[self.index]
#
# def Main():
#     rev = Reverse('praneeth')
#     for char in rev:
#         print(char)
# if __name__ == '__main__':
#     Main()


# class Method():
#     x = 0
#     y = 0
#     def set(self,x,y):
#         self.x = x
#         self.y = y
#
# def Main():
#     me = Method()
#     me.set(5,6)
#     print(me.x,me.y)
#
# if __name__ =='__main__':
#     Main()

#
# class Pet():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# class Cat(Pet):
#     def __init__(self,name,age):
#         super().__init__(name,age)
#
# def Main():
#     rat = Pet("mouse",5)
#     dog = Cat("BowBow",10)
#     print (dog.name,dog.age)
#     print (rat.name,rat.age)
#     print (isinstance(dog,Cat))
#
# if __name__ == '__main__':
#     Main()

#
# class Hidden():
#     __hiddenvalue = 0
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def total(self):
#         print(self.a + self.b + self.__hiddenvalue)
#
# def Main():
#     hide = Hidden(10,20)
#     hide.total()
#
# if __name__ == '__main__':
#     Main()

#
# class Test():
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def __repr__(self):
#         return "Test a:%s b:%s" %(self.a,self.b)
#
# t = Test(1,2)
# print(t)

#
# class Base():
#     def __init__(self,name):
#         self.name = name
#     def getName(self):
#         return self.name
#     def isEmployee(self):
#         return False
#
# class derived(Base):
#     def __init__(self,name,age):
#         self.age = age
#         super().__init__(name)
#     def getAge(self):
#         return self.age
#     def isEmployee(self):
#         return True
#
# # b = Base('Praneeth')
# # print (b.getName(),b.isEmployee())
#
# c = derived('satish',20)
# print (c.getName(),c.getAge(),c.isEmployee())



# class mother():
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender =  gender
#
#     def getName(self):
#         return self.name
#     def getGender(self):
#         return self.gender
#     def getAge(self):
#         return self.age
#     def isEmployee(self):
#         return True
#
# class child():
#     def __init__(self,location):
#         self.location = location
#
#     def getLocation(self):
#         return self.location
#
# class subchild(mother,child):
#     def __init__(self,name,age,gender,location):
#         mother.__init__(self,name,age,gender)
#         child.__init__(self,location)
#         print ("They are derived from base & child Class")
#
# x = subchild("praneeth",30,"M","Banaglore")
# print (x.getName(),x.getAge(),x.getGender(),x.getLocation(),x.isEmployee())

'''Polymorphism of function'''
# def add(a,b,c=0):
#     return a+b+c
# print (add(1,2,5))

'''Polymorphism with class'''
# class India():
#     def Capital(self):
#         print ("New Delhi")
#     def Language(self):
#         print ("Hindi")
#     def type(self):
#         print("Developing country")
#
# class USA():
#     def Capital(self):
#         print ("Washington D C")
#     def Language(self):
#         print ("English")
#     def type(self):
#         print("Developed country")
# obj_india = India()
# obj_us = USA()
#
# for country in (obj_us,obj_india):
#     country.Capital()
#     country.Language()
#     country.type()

'''Polymorphism with inheritance'''
# class Bird():
#     def flight(self):
#         print("Most of the birds can fly")
#     def intro(self):
#         print("There are many types of birds")
#
# class sparrow(Bird):
#     def flight(self):
#         print ("sparrow can fly")
# class ostrich(sparrow):
#     def flight(self):
#         print ("ostrich can't fly")
#
# obj_bird = Bird()
# obj_sparrow = sparrow()
# obj_ostrich = ostrich()
#
# obj_bird.intro()
# obj_bird.flight()
#
# obj_sparrow.intro()
# obj_sparrow.flight()
#
# obj_ostrich.intro()
# obj_ostrich.flight()


'''Polymorphism with functions and objects'''
# class India():
#     def Capital(self):
#         print ("New Delhi")
#     def Language(self):
#         print ("Hindi")
#     def type(self):
#         print("Developing country")
#
# class USA():
#     def Capital(self):
#         print ("Washington D C")
#     def Language(self):
#         print ("English")
#     def type(self):
#         print("Developed country")
#
# def func(obj):
#     obj.Capital()
#     obj.Language()
#     obj.type()
# obj_india = India()
# obj_us = USA()
# func(obj_india)
# func(obj_us)

'''Class Method or Static Method'''

# from datetime import date
# class Person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def frombirthyear(cls,name,age):
#         return cls(name,date.today().year-age)
#
#     @staticmethod
#     def isAdult(age):
#         return age >18
#
# p1 = Person('praneeth',29)
# p2 = Person.frombirthyear('praneeth',1989)
#
#
# print (p1.age)
# print (p2.age)
# print (p1.isAdult(29))
#


'''Class variable and changing them'''

# class Student():
#     stream = 'CSIT'
#
#     def __init__(self,name,roll):
#         self.name = name
#         self.roll = roll
# a = Student('praneeth','06511A1202')
# b = Student('hani','123456789')
#
# a.stream = 'CSE'
# print (a.stream)
# print (Student.stream)
# print (b.stream)
# print (a.stream)

'''Destructor'''

# class A():
#     def __init__(self,a):
#         self.a = a
#     def __del__(self):
#         print ("Hi I am deleting the object")
#
# A(10)

# class A():
#     def __init__(self,a):
#         self.a = a
#
# class B():
#     def __init__(self):
#         self.a = A(self)
#     def __init__(self):
#         print ("Hi this is destructor")
#
# def func():
#     f = B()
# func()


'''str() and repr()'''
# s ='Hello,guru'
# a = 0.2/11.0
# print (s.__repr__())
# print (s.__str__())
# print (a.__repr__())
# print (a.__str__())


# class complex():
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return '%s,i%s'%(self.a,self.b)
#
#     def __repr__(self):
#         return 'Rational(%s,i%s)'%(self.a,self.b)
#
# c = complex(10,20)
# print(c.__str__())
# print (c.__repr__())

'''Class & instance attributes'''

# class Sampleclass():
#     count = 0
#     def increase(self):
#         Sampleclass.count +=1
# a = Sampleclass()
# a.increase()
# a.increase()
# print (a.count)


# class inst():
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def show(self):
#         print (self.a,self.b)
# i = inst(1,2)
# print (vars(i))
# print (dir(i))

'''Reflections'''
# def reverse(seq):
#     SeqType = type(seq)
#     emptySeq = SeqType()
#     if seq == emptySeq:
#         return emptySeq
#     restrev = reverse(seq[1:])
#     first = seq[0:1]
#     # Combine the result
#     result = restrev + first
#     return result
#
# print (reverse([1,2,3,4]))


# class Employee:
#     salary = 25000
#     com_name = "Nokia"
#
# emp =Employee()
# print (getattr(emp,"com_name"))
# print (emp.salary)

# from functools import wraps
# def debug(func):
#     '''decorator for debugging passed function'''
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Full name of this method:", func.__qualname__)
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# def debugmethods(cls):
#     '''class decorator make use of debug decorator
#        to debug class methods '''
#
#     # check in class dictionary for any callable(method)
#     # if exist, replace it with debugged version
#     for key, val in vars(cls).items():
#         if callable(val):
#             setattr(cls, key, debug(val))
#     return cls
#
#
# # sample class
# @debugmethods
# class Calc:
#     def add(self, x, y):
#         return x + y
#
#     def mul(self, x, y):
#         return x * y
#
#     def div(self, x, y):
#         return x / y
#
#
# mycal = Calc()
# print(mycal.add(2, 3))
# print(mycal.mul(5, 2))


import threading

'''Timer setting and Timer cancelling '''
# def print_str():
#     print ("Hi this is praneeth")

# timer = threading.Timer(5,print_str)
# timer.start()
# print ("Byeee....")
#


# timer = threading.Timer(5,print_str)
# timer.start()
# print ("Byeee........")
# timer.cancel()


'''Garbage collection'''

# import gc
#
# collect = gc.collect()
# print (collect)

# a = {'adam':100,'drichard':200,'cvoldmart':30,'bmanfred':50}

# for i in sorted(a.keys()):
#     print (i,a[i])

# a = {'adam':100,'drichard':200,'cvoldmart':30,'bmanfred':50}
# for i in sorted(a.values()):
#     for j in a.items():
#         if i in j:
#             print (j)

# L = ['abt', 'efgh', 'defg', 'efkjkl', 'abc', 'defk', 'cbtefg']
# L.sort(key=len)
# print(L)

# def taketwo(ele):
#     return ele[0]
# L = [(7,6),(2,3),(3,9),(4,5)]

# L.sort(key=taketwo)
# print (L)

# N=[]
# for i in L:
#     N.append(i[0])
# for j in sorted(N):
#     for i in L:
#         if j == i[0]:
#             print (i)

j = 1
for i in "praneeth":
    print(j,":",i)
    j += 1
