#Python training Day 1 excercises

#1.	Write a program that declare two numeric variables and print their sum and product.

# a = 3
# b = 5
# print (a + b)

# 2. Write a program that declare two string (name & second name) and print concatenation of string

# name = "Praneeth"
# second_name = "Guptha"
# print (name + " " + second_name)

# 3. Write a program that takes 4 input numbers and print the biggest number of the 4 numbers.

# a = int(input("enter 1st numbers a:"))
# b = int(input("enter 2nd numbers b:"))
# c = int(input("enter 3rd numbers c:"))
# d = int(input("enter 4th numbers d:"))
#
# if a > b and a > c and a > d:
#     print("The largest number among all:", a)
# elif b > a and b > c and b > d:
#     print("The largest number among all:", b)
# elif c > a and c > b and c > d:
#     print("The largest number among all:", c)
# else:
#     print ("The largest number among all:",d)

# 4. Given two int values, print their sum. Unless the two values are the same, then print double their sum.

# a = int(input("enter 1st number:"))
# b = int(input("enter 2nd number:"))
#
# if a == b:
#     print(2*(a + b))
# else:
#     print (a + b)


# 5. Given an int n, print  the absolute difference between n and 21, except print  double the absolute difference if n is over 21.

# a = int(input("enter a number:"))
# if a > 21:
#     print (2*(abs(a-21)))
# else:
#     print (abs(a-21))

# 6. Given 2 ints, a and b, print  True if one of them is 10 or if their sum is 10.
#
# a = int(input("enter the 1st number:"))
# b = int(input("enter the 2nd number:"))
# sum = a + b
# if a == 10 or b == 10:
#     print ("True")
# elif sum == 10:
#     print ("True")
# else:
#     print ("The given condition does not match any criteria")

# 7. Given 3 int values, a b c, print their sum. However, if one of the values is the same as.

# a = int(input("Enter the 1st number:"))
# b = int(input("Enter the 2nd number:"))
# c = int(input("Enter the 3rd number:"))
# sum = 0
# if (a != b and a != c):
#     sum += a
# if (b != c and b != a):
#     sum += b
# if (c != a and c != b):
#     sum += c
# print (sum)


# Basic Assignments on Loops, Conditions.

# 1. Write a Python script to check if an input string is a Palindrome.

# str = input("Enter a string:")
# new_str = str[::-1]
# if str == new_str:
#     print ("The string is Palindrome")
# else:
#     print ("It is not a Palindrome")

# 2.Write a Python script to count the number of vowels in a given input string.

# str = input("Enter a string:")
# sum = 0
# vowels = ['a','e','i','o','u']
#
# for s in str:
#     if s in vowels:
#         sum += 1
# print (sum)

# 3. Write a Python script to print the sum of digits of a given input integer. Eg : z=134628

# num = int(input("Enter a number:"))
# sum = 0
# for n in str(num):
#     sum += int(n)
# print (sum)

# 4. Write a Python script to print the count of digits of a given input integer. Eg : z=1346289

# num = int(input("Enter a number:"))
# count = 0
# for n in str(num):
#     count += 1
# print (count)


# 5. Write a Python script to print numbers between  1000-3000 which are multiple of 7 and not divisible by 5.

# for x in range(1000,3000):
#     if (x%7==0) and (x%5 !=0):
#         print (x)


# 6. Write a Python script to print numbers between  1000-3000 whose all digits are even.
#
# import re
# for i in range(1000,3000):
#     if re.search("[13579]",str(i)):
#         continue
#     else:
#         print(i,end=', ')

# result = []
# for num in range (1000,3000):
#     temp = []
#     for i in str(num):
#         if i == 0:
#             temp.append(i)
#         elif int(i) % 2 == 0:
#             temp.append(i)
#         else:
#             temp = []
#             break
#     if temp:
#         result.append("".join(temp))
# print (",".join(result))

# 7. Write a Python script to find largest and smallest number from the given 4 numbers.

# list = []
# num  =  int(input("how many numbers you want to enter:"))
#
# for i in range(0,num):
#     list.append(int(input("enter the number:")))
# print ("The largest number:", max(list))
# print ("The smallest number:", min(list))


# 8. Write a Python script to print first 10 Fibonacci series.

# a = 0
# b = 1
# i = 0
# while (i < 10):
#     print (a,end = ",")
#     fib = a + b
#     a = b
#     b = fib
#     i += 1

# 9. Write a Python script to print sum of prime numbers between 1 and 50.

# lower = 1
# upper = 100
#
# print("Prime numbers between",lower,"and",upper,"are:")
#
# for num in range(lower,upper + 1):
# # prime numbers are greater than 1
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)


# 10. Write a Python script to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console
# (n>0).  Example: If the following n is given as input to the program: 5  Then, the output of the program should be: 3.55

# n = int(input("Enter the number:"))
# a = 1
# sum = 0
# while (n >= a):
#     sum = sum + (a/(a+1))
#     a += 1
# print (round(sum,2))

# 11.	Write a program to take a odd number between 1-10 and print as below
# 999999999
#   7777777
#     55555
#       333
#         1

# for i in range (1,10):
#     for j in range (0,i):
#         if (i%2 == 0):
#             break
#         else:
#             print(i,end = " ")
#     print("\r")

#
# for i in range (10,0,-1):
#     for j in range (0,i):
#         if (i%2 == 0):
#             break
#         else:
#             print(i,end=" ")
#     print (" ")


# for i in range (10,0,-1):
#     space = i
#     for j in range (0,i):
#         if (i%2 == 0):
#             break
#         else:
#             print(i,end=" ")
#     print (" ")




# 12.	Write a program to print below fig
#            ***
#             **
#              *
#             **
#            ***

# for i in range (3,1,-1):
#     for j in range (0,i):
#         print ("*",end=" ")
#     print ("")
# for i in range (1,4):
#     for j in range (0,i):
#         print ("*",end=" ")
#     print (" ")
#

# 13.	Write a program to take a odd number between 1-10 and print as below
# 999999999
#   7777777
#     55555
#       333
#         1
#      333
#     55555
#    7777777
#  999999999
#
# for i in range(1,6):
#  for j in range(1,1+i):
#    print "",
#  for k in range(1,7-i):
#   print "*",
#  print


# for i in range (1,10):
#     for j in range (1,1+i):
#         print("",end=" ")
#     for k in range (1,11-i):
#         print ("*",end="")
#     print ()

#
# for i in range (10,0,-1):
#     for j in range (0,i):
#         if (i%2 == 0):
#             break
#         else:
#             print (i,end="",)
#     print ()





# 14. Write a PYTHON program to print sum of all even numbers between 1 to n.

# n = int(input("Enter the number:"))
# sum = 0
# for i in range (1,n+1):
#     if (i%2 == 0):
#         sum = sum + i
# print (sum)

# 15. Write a PYTHON program to print sum of all odd numbers between 1 to n.

# n = int(input("Enter the number:"))
# sum = 0
# for i in range (1,n):
#     if (i%2 != 0):
#         sum = sum + i
# print (sum)

# 16. Write a Python program to enter any number and find its first and last digit.

# n = input("Enter the number:")
# a = len(n)
# print ("First digit",n[0])
# print ("Last digit",n[-1])

# 17. Write a Python program to enter any number and print its reverse.

# n = input("Enter the number:")
# print ("reverse number",n[::-1])

# 18. Write a Python program to enter any number and find the sum of first and last digit of the number.

# n = input("Enter the number:")
# print ("Sum of first and last digit",int(n[0]) + int(n[-1]))

# 19. Write a Python program to print to check if a given input number is an Armstrong.
# Armstrong number is a special number whose sum of cube of its digits is equal to the original number.
# Example: 371 is an Armstrong number because 33 + 73 + 13 = 371

# Sol:-1
# num = int(input("Enter the number:"))
# sum = 0
# temp = num
# while (temp > 0):
#     digit = temp % 10
#     sum += digit ** 3
#     temp //= 10
#
# if num == sum:
#     print ("Yes it is Armstrong Number")
# else:
#     print ("Oh! no it is not armstrong number")

# Sol:-2

# num = input("Enter the number:")
# sum = 0
# for i in num:
#     sum = sum + int(i)**3
# if (int(num) == sum):
#     print ("It is Armstrong Number")
# else:
#     print ("Oh! no it is Armstrong Number")

# 20. Write a Python program to print all Perfect numbers between 1 to n.
# A perfect number is a positive integer which is equal to the sum of its proper positive divisors.
# Example: 6 is the first perfect number . Proper divisors of 6 are 1, 2, 3  And 1+2+3 = 6. Hence 6 is a perfect number

# n = int(input("Enter the number:"))
# for i in range (1,(n+1)):
#     sum = 0
#     for j in range (1,i):
#         if (i%j == 0):
#             sum += j
#             j += 1
#         else:
#             j += 1
#             continue
#     if (i == sum):
#         print (i, "is a perfect number" )

# 21.	Write a Python program to construct the following pattern, using a nested for loop
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


# for i in range (1,6):
#     for j in range (0,i):
#         print ("*",end=" ")
#     print (" ")
# for i in range (4,0,-1):
#     for j in range (1,i+1):
#         print ("*",end = " ")
#     print (" ")
#

# print(dir(list))

# 22.	Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Expected Output : 0 1 2 4 5

# temp = []
# for i in range (0,7):
#     if (i == 3) or (i == 6):
#         continue
#     else:
#         temp.append(i)
# print (temp)

# 23.	Print sum of digits of numbers from 1 to 100( both included).
# sum = 0
# for i in range (1,101):
#     sum += i
# print (sum)

