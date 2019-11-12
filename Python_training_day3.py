# 1) Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct available in Python.

# def Max(a,b):
#     if a == b:
#         print("both are same")
#     elif a > b:
#         print("max",a)
#     else:
#         print ("max",b)

# Max(2,3)
# Max(1,1)

# 2) Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.

# def max_of_three(a,b,c):
#     if a > b and a > c:
#         print ("Max of 3 numbers is:",a)
#     elif b > c and b > a:
#         print ("Max of 3 numbers is:",b)
#     elif c > b and c > a:
#         print ("Max of 3 numbers is:",c)
#     else:
#         print ("They are same")

# max_of_three(1,1,1)
# max_of_three(3,5,9)

# sol-2
# =====
# def max_of_three(a):
#     return (max(a))
#
# a = [1,-2,-3]
# print(max_of_three(a))


# 3)  Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise

# def char(a):
#     vowels = ['a','e','i','o','u']
#     if a in vowels:
#         return True
#     else:
#         return False
#
# print(char('a'))

# 4)  Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers.
# For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.

# def Addition(a):
#     sum = 0
#     for i in a:
#         sum += i
#     return sum
#
# def Multiplication(a):
#     Mul = 1
#     for i in a:
#         Mul *= i
#     return Mul
# a = [1,2,3,4]
#
# print(Addition(a))
# print(Multiplication(a))

# 5) Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
# For example, is_palindrome("radar") should return True.

# def is_palindrome(a):
#     if a == a[::-1]:
#         return True
#     else:
#         return False
#
# print(is_palindrome("radae"))
# print(is_palindrome("radar"))


# 6) Define a menu driven function with choice of
# 1) Add, 2) Subtract 3) Multiply 4) Divide 5) Quit.
# Add functions for addition, subtraction, multiplication, division, & Quit.
# In short implement your own calculator

# def Addition(a,b):
#     sum = a + b
#     return sum
# def Multiplication(a,b):
#     Mul = a * b
#     return Mul
# def Subtract(a,b):
#     sub = a - b
#     return sub
# def Divide(a,b):
#     div = a / b
#     return div
# def Quit():
#     exit()
# def calculator():
#     print("select the operation listed below:")
#     print ("Addition")
#     print ("Multiplication")
#     print ("Subtract")
#     print ("Divide")
#     print ("Quit")
#     choice = input("enter you choice by entering the function name Addition/Multiplication/Subtract/Divide/Quit:")
#     if choice == 'Quit':
#         Quit()
#     else:
#         a = int(input("enter the first number:"))
#         b = int(input("enter the second number:"))
#     if choice == 'Addition':
#         print(Addition(a,b))
#     elif choice == 'Multiplication':
#         print(Multiplication(a,b))
#     elif choice == 'Subtract':
#         print(Subtract(a,b))
#     else:
#         print(Divide(a,b))
#
# calculator()


# 7) Write a function find_longest_word() that takes a list of words and returns the length of the longest one.


# def find_longest_word(a):
#     return max(a)
#
# a = ['praneeth','guptha','hi','hello']
# print(find_longest_word(a))

# 8) Given a list of N numbers, use a single list comprehension to produce a new list that only contains even numbers from among those elements in the original
# list that have even indices. For example, if list[2] contains a value that is even, that value should be included in the new list,
# since it is also at an even index in the original list.
# However,if list[3] contains an even number, that number should not be included in the new list since it is at an odd index in the original list.

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
# print(NewList(a))

# 9) A pangram is a sentence that contains all the letters of the English alphabet at least once,
# for example: The quick brown fox jumps over the lazy dog.
# Your task here is to write a function to check a sentence to see if it is a pangram or not

# def pangram(a):
#     alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     for i in a:
#         if i.isspace():
#             continue
#         elif i not in alphabet:
#             return "Not a pangram"
#         else:
#             return "It is a pangram"
#
# a = "The quick brown fox jumps over the lazy dog"
# a = "abcd efgh ijkl mnop qrstu vwxyz"
# print (pangram(a))


# 10) Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting
# them alphanumerically.Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again
# Then, the output should be: again and hello makes perfect practice world


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


# 11) Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.

# def max_len_str(a,b):
#     if len(a) == len(b):
#         print (a)
#         print (b)
#     elif len(a) > len(b):
#         print (a)
#     else:
#         print (b)
#
# max_len_str('praneeth','somethin')
# max_len_str('praneeth','guptha')

# 12) Write a function f(a, b) which takes two character string arguments and returns a string containing only the characters
# found in both strings in the order of a.


# def common(a,b):
#     common_char = " "
#     for i in a:
#         if i in b:
#             common_char += i
#     return common_char
#
# print(common("guptha","praneeth"))

# 13) Given two int Lists. Write functions to find out common numbers and different numbers.

# def common_diff(a,b):
#     common = []
#     diff= []
#     for i in a:
#         if i in b:
#             common.append(i)
#         else:
#             diff.append(i)
#     for i in b:
#         if i in a:
#             if i in common:
#                 continue
#             else:
#                 common.append(i)
#         else:
#             diff.append(i)
#     return common,diff
#
# a = [1,2,3,4]
# b = [2,9,6,8]
# print (common_diff(a,b))

# 14) Write a function to test if the given set of brackets are balanced or not. e.g. {{}}{)([][]

# a = '{{{}}}()()[]]['
# # a = '{{}}{)([][]'
# open = ['{','[','(']
# close = [']','}',')']
# new_open=[]
# new_close=[]
# for i in a:
#     if i in open:
#         new_open.append(i)
#     else:
#         new_close.append(i)
#
# if new_open.count('{') == new_close.count('}') and new_open.count('(') == new_close.count(')') and  new_open.count('[') == new_close.count(']'):
#     print ("it is balanced")
# else:
#     print("it is unbalanced")
#

# 15) Write func repeat(e, n).
# Args: e: any object , n: a number of times  Returns: an iterator producing the element e n times

# def itre():
#     str = input("enter the object that you want to iterate:")
#     str1 = int(input("enter the number of times you want to iterate:"))
#
#     for i in range(0,str1):
#         print (str,end="")
#
# itre()

# 16) Write a function that accepts  inputs  as two number and an operator (+,-,*) and performs
# Operation on the given numbers

# def calcu(a,b,opr):
#     # a = int(input("enter the first number:"))
#     # b = int(input("enter the first number:"))
#     # opr = input("enter the operator i.e. '+','-','*':")
#     if opr == '+':
#         print (a + b)
#     elif opr == '-':
#         print ( a - b)
#     elif opr == '*':
#         print (a * b)
#     else:
#         print ("enter the correct operator")
# calcu(10,2,'+')

# 17) Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I".

# def reverse(a):
#     print (a[::-1])
#
# reverse("I am testing")

# 18) Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# def oreder_list(a):
#     temp = []
#     for i in a:
#         temp.append(i)
#     a.sort()
#     if a == temp:
#         print ("TRUE")
#     else:
#         print ("FALSE")
#
# a = [9,1,2,3,4]
# oreder_list(a)


# 19) Optimize the code using List comphrension
#         Def AppendWords(words):
# 	Nw=[]
# 	For word in words:
# 		Nw.append(word+’s’)
# 	Return Nw
# For w in AppendWords([‘A’,’B’,’C’]):
# 	Pirnt w


# 20) ) Write a function which calculates the arithmetic mean of a variable number of values.
# Def A_Mean(x,*a):
# ….
# A_Mean(4,7,9)
# A_Mean(4,7,9,45,-3.7,99)

# def A_Mean(*num):
#     len = 0
#     sum = 0
#     mean = 0
#     for i in num:
#         sum += i
#         len += 1
#     mean = sum/len
#     print (type(num))
#     return mean

# print(A_Mean(1,2,3,4,5))


import webbrowser
import time

# print (time.ctime())
# for i in range (0,3):
#     # time.sleep(2*3600)
#     webbrowser.open("https://www.youtube.com/watch?v=VkmXX_jKmZw")
#     print(time.ctime())




# import os
#
# file_list = os.listdir(r"C:\Users\pguptha\Desktop\prank")
# os.chdir(r"C:\Users\pguptha\Desktop\prank")
# for file_name in file_list:
#     new_str =""
#     for i in file_name:
#         if i.isnumeric():
#             continue
#         else:
#             new_str += i
#     os.rename(file_name,new_str)
