# 1.	Write a program that declare a list and prints 2nd element till 8th element.

# a = [1,2,3,4,5,6,7,8,9,10,11]
# print (a[1:8])

# 2.	Write a Python Script to sum and multiply the List elements.
#  L1=[1,2,3,4,5] Output : Total =15, Mult=120

# l1 = [1,2,3,4,5]
# sum = 0
# mul = 1
# for i in l1:
#     sum = sum + i
#     mul = mul * i
#
# print (sum,mul)

# 3.	Write a Python Script to remove duplicate elements of the List.
#  L2= [12,24,35,24,88,120,155,88,120,155], Output :[12,24,35,88,120,155]

# l2 = [12,24,35,24,88,120,155,88,120,155]
# l1 = []
#
# for i in l2:
#     if i not in l1:
#         l1.append(i)
# print (l1)


# 4.	L1=[1,2,3,4,5,6,7,8]. Find the indexes even square& indexes odd square from the given list?
# OddI=[2,4,6,8]  OddISq=[4,16,36,64]
# EvenI=[1,3,5,7,9]  EvenISq=[1,9,25,49,81]

# l1 = [1,2,3,4,5,6,7,8]
# a = len(l1)
# i = 0
# j = 1
# OddI = []
# EvenI = []
# while (a>i):
#     EvenI.append(l1[i])
#     i +=2
# while (a>j):
#     OddI.append(l1[j])
#     j +=2
# EvenIsq = [i*i for i in EvenI]
# OddIsq = [i*i for i in OddI]
# print (EvenIsq,OddIsq)

# 5.Find the length of each element of the list
# L2=[‘welcome’,’to’,’Python’, ‘Scripting’], Output : LL=[7,2,6,9]

# L2=["welcome", "to", "Python", "Scripting"]
# L1 = []
#
# for i in range (0,len(L2)):
#     L1.append(len(L2[i]))
# print (L1)


# 6.	Write a Python Script to print a given elements index. Eg L=[12,200,300,34,5]
# Z=input(“enter element”)
# Z= 200, index  I =1
# Z=1000 Element not present in list

# L = [12,200,300,34,5]
#
# z = int(input("Enter the number:"))
# if z in L:
#     print (L.index(z))
# else:
#     print (z,"Element not present in the list")


# 7.	Write a program that add all the marks of students for given subject.
# Each element of the list is array of marks L1 = [[90,60,30],[69,80,79],[89,90,60]]

# L1 = [[90,60,30],[69,80,79],[89,90,60]]
# NL1 = []
#
# for i in range (0,len(L1)):
#     sum = 0
#     for j in  range (0,len(L1[i])):
#         sum += L1[i][j]
#     NL1.append(sum)
# print (NL1)


# 8.	Write a program that keep taking the name as input from the user and keep adding to the list if not already present. It stops when user enter "end"

# names = []
# name = ''
# while name != "end":
#     name = input("Please tell me someone I should know, or enter 'end': ")
#     if name == 'end':
#         break
#     if name not in names:
#         names.append(name)
# print(names)

# 9.	Write a program to print all elements of list in different line L1 = [2,5,3,4,"apple",7,"mango",40]

# L1 = [2,5,3,4,"apple",7,"mango",40]
# for i in L1:
#     print (i)

# 10.	write a program to print all elements of list in same line  line  L1 = [2,5,3,4,"apple",7,"mango",40]

# L1 = [2,5,3,4,"apple",7,"mango",40]
# for i  in L1:
#     print (i,end=" ")

# 11.	Write a Python program which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

# SqrList = []
# for i in range (1,21):
#     SqrList.append(i*i)
# print (SqrList)

# SqrList = [i*i for i in range (1,21)]
# print (SqrList)

# 12.	Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included)

# SqrList = []
# for i in range (1,31):
#     SqrList.append(i*i)
# print (SqrList)
# print (SqrList[0:5]+ SqrList[25:])


# 13.	Write a Python program to generate and print a list except the first 5 elements, where the values are square of numbers between 1 and 30 (both included)

# SqrList = []
# for i in range (1,31):
#     SqrList.append(i*i)
# print (SqrList)
# print (SqrList[5:])

# 14. L=[1,2,3,4,5,6,7,8,9,10,20,31,51,99] Print prime & composite numbers from the list

# prime =[]
# for i in range (1,101):
#     if i > 1:
#         for j in range (2, i):
#             if i % j == 0:
#                 break
#         else:
#             prime.append(i)
# composite=[]
# for i in range (2,101):
#     if i not in prime:
#         composite.append(i)
# print ("prime number:",prime)
# print ("composite number:",composite)






# 18.	Given an array of ints length 3, figure out which is larger between the first and last elements in the array, and set all the other elements to be that value. Return the changed array.
# Eg: [1,2,3] Output :[3,3,3]
# [11, 5, 9] Output : [11, 11, 11]

# L = [1,2,3]
# L =[11,5,9]
# L1 = []
# print (max(L))
# for i in L:
#     L1.append(max(L))
# print (L1)

# 15.	Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

# L1 = [6,1,3,4,5,6,0]
#
# if L1[0] == 6 or L1[-1]== 6:
#     print ("True")


# 16.	Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal

# L1 = [6,1,2,3,4,5,6]
#
# if len(L1)>  1 and L1[0] == L1[-1]:
#     print ("True")

# 17.	Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.

# L1 = [6,1,2,3,4,5,6]
# L2 = [6,2,3,4,5,6]
#
# if (len(L1) > 1) and (len(L2) > 1):
#     if L1[0]==L2[0] or L1[-1] == L2[-1]:
#         print ("True")


# 19.	Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements
# Eg: [7, 7, 7], [3, 8, 0] Output: [7, 8]

# L1 = [7,7,7]
# L2 = [3,8,0]
# L3 = []
# L3.append(L1[1])
# L3.append(L2[1])
# print (L3)

# 20.	Return the number of even ints in the given array
# Eg: [2, 1, 2, 3, 4]) → 3

# L1 = [2,1,2,3,4]
# sum = 0
# for i in L1:
#     if i%2 == 0:
#         sum += 1
# print (sum)


# 21.	Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array
# Eg: [10, 3, 5, 6] Output → 7

# L1 = [10,3,5,6]
# print (max(L1) - min(L1))

# Assignment on Dictionary and Tuple
# ===================================
# 1)	Write a Python program that will take the following list of words as input and output a dictionary with a the frequency of each word:
# words = ['apple', 'apple', 'banana', 'banana', 'banana', 'pear', 'banana', 'pear', 'pear', 'pear', 'pear', 'pear']
# count={‘apple’:2, ‘pear’:6,’banana’:4}

# words = ['apple', 'apple', 'banana', 'banana', 'banana', 'pear', 'banana', 'pear', 'pear', 'pear', 'pear', 'pear']
# count = {'apple':words.count('apple'),'banana':words.count('banana'),'pear':words.count('pear')}
# print (count)

# sol-2
# =====

# count ={}
# words = ['apple', 'apple', 'banana', 'banana', 'banana', 'pear', 'banana', 'pear', 'pear', 'pear', 'pear', 'pear']
# for i in words:
#     count[i]=words.count(i)
# print (count)

# 2)	Write a program that count vowels in the given string using Dictionary

# str = input("enter a string:")
# vowel_dict ={}
# vowel = ['a','e','i','o','u']
# for i in str:
#     if i in vowel:
#         vowel_dict[i]=str.count(i)
# print (vowel_dict)


# 3)	Write a Python program which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

# Sqr =[]
# for i in range (1,21):
#     Sqr.append(i*i)
# print(tuple(Sqr))

# 4)	Write a Python program which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

# Sqr_dict= {}
# for i in range (1,21):
#     Sqr_dict[i]= i*i
# print (Sqr_dict)


# 5)	Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

# T1 = (1,2,3,4,5,6,7,8,9,10)
# T2 = []
# for i in T1:
#     if i%2 == 0:
#         T2.append(i)
# print (tuple(T2))


# 6)	Write a Python script to concatenate following dictionaries to create a new one.
# Eg: dic1={1:10, 2:20}  dic2={3:30, 4:40} dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4={}
# for i in dic1:
#     dic4[i]=dic1[i]
#
# for i in dic2:
#     dic4[i]=dic2[i]
#
# for i in dic3:
#     dic4[i]=dic3[i]
#
# print (dic4)

# so:-2
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4={}
#
# for i in (dic1,dic2,dic3):
#     dic4.update(i)
# print (dic4)


# 7)	Write a Python program to sum all the items in a dictionary

# student={'Telugu':99,'Maths':98,'English':97,'Science':96,'Social':95,'Hindi':94}
# sum = 0
# for i in student.values():
#     sum += i
# print (sum)

# 8)	Write a Python program to multiply all the items in a dictionary

# student={'Telugu':99,'Maths':98,'English':97,'Science':96,'Social':95,'Hindi':94}
# sum = 1
# for i in student.values():
#     sum *= i
# print (sum)


# Assignment on Strings
# ---------------------
# 1)	Str1=”New Year is celebrated on 1st Jan 2017”
# Write a Python script to count number of  a)digits b) Alphabets c) upper case d) lowercase and e) spaces in Str1

# Str1='New Year is celebrated on 1st Jan 2017'
# Upper = 0
# Lower = 0
# Space = 0
# Digit = 0
#
# for i in Str1:
#     if i.isspace():
#         Space += 1
#     elif i.islower():
#         Lower += 1
#     elif i.isupper():
#         Upper += 1
#     else:
#         i.isdigit()
#         Digit += 1
# print ("Upper:",Upper,"Lower:",Lower,"Space:",Space,"Digit:",Digit)

# 2)	Str2=raw_input()
# Write a Python script to convert upper case to lower case and vice versa

# str = input("Enter the string:")
#
# if  str.islower():
#     print (str.upper())
# else:
#     print(str.lower())


# 3)	Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program: ‘34,67,55,33,12,98’
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# str = input("Enter the number by seperating it with comma:")
# print (str.split(","))
# print (tuple(str.split(",")))


# 4)	write a program which count and print the numbers of each character in a string input by console.
# Example: If the following string is given as input to the program: abcdefgabc
# Then, the output of the program should be:
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

# str = input("Enter the string:")
# list = []
# for i in str:
#     if i not in list:
#         print(i, str.count(i))
#         list.append(i)
#     else:
#         continue

# 5)	Write a Python script to count number of identical chars in a given string with some special case handling, and return the number with highest count,
# Eg, given string "coffee tuffee", should return 4.


# str = "coffee tuffee"
#
# dict = {}
# for i in str:
#     if i == " ":
#         continue
#     else:
#         dict[i] = str.count(i)
# print (max(dict.values()))


# 6)	Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program: Hello world Practice makes perfect
# Then, the output should be: HELLO WORLDPRACTICE MAKES PERFECT

# lines = []
# while True:
#     line = input()
#     if line:
#         lines.append(line.upper())
#     else:
#         break
# for i in lines:
#     print (i,end=" ")




# 7)	Write a program to determine whether an input string x is a substring of another input string y.
# (For example,"bat"is a substring of "abate",but not of "beat".)??

# x = input("Enter a string:")
# y = input("Enter a substring:")
# if (y.find(x)) == -1:
#     print ("x is not sub string of Y")
# else:
#     print("x is a sub string of Y")


# 8) Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example: 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

# list1 = input("enter the number by separating it with comma:")
# list1 = list1.split(",")
#
# for i in list1:
#     if int(i)%5  == 0:
#         print (i)



# 9)	Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
# except the first char itself.
# Ex : 'restart'
# Expected Result : 'resta$t'

# str = input("Enter the string:")

# str = "restart"
# char = str[0]
# for i in str:
#     if str.count(i) > 1:
#         str = str.replace(i,'$')
#         break
# str = char + str[1:]
# print (str)

# 10)	Remove white spaces from the string SN=”aaa bbb ccc ddd eee FFF JJJ kkk LLL”

# str = 'aaa bbb ccc ddd eee FFF JJJ kkk LLL'
# str1 = " "
# for i in str:
#     if i.isspace():
#         exit
#     else:
#         str1 += i
#
# print (str1)


# 11)	Given a string, return a new string where the first and last chars have been exchanged.

# str = input("Enter the string:")
#
# start = str[0]
# end = str[-1]
# nstr = end + str[1:-1] + start
# print (nstr)

# 12)	Given a string, we'll say that the front is the first 3 chars of the string.
# If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
# # Eg: Java output: JavJavJav
# Chocolate output :ChoChoCho

# str = input("enter the string:")
#
# nstr = str[0:3]
# if len(str)>3:
#     print (3*nstr)
# else:
#     exit()

# 13)	Given two strings, a and b, return the result of putting them together in the order
# e.g. "Hi" and "Bye" returns "HiByeByeHi".

# str = input("enter the string:")
# str1 = input("enter the second string:")
# print (str+str1+str1+str)


