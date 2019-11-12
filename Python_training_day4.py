import os
import datetime
import re

# Assignments on File
# 1) Write a version of a palindrome recognise that accepts a file name from the user, reads each line, and prints the line to the screen if it is a palindrome.

def palindrome_file():
    filename = input("Enter the file name:")
    fn = open(filename,'r')
    line = fn.readlines()
    for i in line:
        if i.__contains__('\n'):
            temp = i[:-1]
            if temp == temp[::-1]:
                print(i)
        elif i == i[::-1]:
            print (i)
        else:
            continue
    fn.close()
# palindrome_file()

# 2) Write a program that given a text file will create a new text file in which all the lines from the original file are numbered
# from 1 to n (where n is the number of lines in the file).

# def number_file():
#     file = input("Enter the file name:")
#     fn = open(file,'r')
#     line = fn.readlines()
#     total_lines = len(line)
#     nfile = open("New_Palindrome.txt",'a')
#     ln = 1
#     for i in range(0,total_lines):
#         line1 = str(ln)  + " " + line[i]
#         nfile.write(line1)
#         ln += 1
#     fn.close()
#     nfile.close()
# number_file()

# 3) write solution code for 2 problems –
# (a) Given a log file containing INFO, WARNING and DEBUG statements, separate the specific log statements into specific files (E.g., all INFO statements
#  into the INFO file and so on) and delete the original file.
# (b) Given multiple occurrences of characters in a string, output the character followed by its frequency.
#  E.g., if input is ‘aaaaabbbbc’, output should be ‘a4b3c1’.


# def log_seperation():
#     filename = input("Enter the file name:")
#     file = open(filename,'r')
#     log_list = file.readlines()
#     list_len = len(log_list)
#     info =[]
#     warn =[]
#     for i in range (0,list_len):
#     error = []
#         if log_list[i].__contains__("INFO"):
#             info.append(log_list[i])
#         elif log_list[i].__contains__("WARN"):
#             warn.append(log_list[i])
#         elif log_list[i].__contains__("ERROR"):
#             error.append(log_list[i])
#         else:
#             continue
#     file.close()
#     infofile = open('Info_log.txt','w')
#     infofile.writelines(info)
#     warnfile = open('Warn_log.txt','w')
#     warnfile.writelines(warn)
#     errorfile = open('Error_log.txt','w')
#     errorfile.writelines(error)
# log_seperation()


def count():
    str1 = input("Enter string:")
    dict = {}
    for i in str1:
        dict[i] = str1.count(i)
    temp = ''
    for i in dict:
        temp = temp + (i+str(dict[i]))
    print(temp)

# count()

# 4) Write a method that returns a count of each word in the file.

def count_word():
    filename = input("Enter the name of the file:")
    file = open(filename,'r')
    file_data = file.read()
    file_list = file_data.split()
    temp = {}
    for i in file_list:
        if i not in temp:
            temp[i] =file_data.count(i)
    print (temp)
    file.close()
# count_word()



# 5) Write a Python Script to open a file, file contains employee names and gender, and count how many male and female empolyee are there.

import re
def gender_count():
    filename = input("Enter the file name:")
    file = open(filename,'r')
    file_list = file.readlines()
    num_male = 0
    num_female = 0
    for i in file_list:
        if re.search('\W[MALE]',i):
            num_male += 1
        elif re.search('\W[FEMALE]',i):
            num_female += 1
        else:
            continue
    print("Total number of Male:",num_male)
    print("Total number of Female:", num_female)
    file.close()
# gender_count()



# 6) Write a Python Script to Count spaces, tabs and new lines in a file

import re
def count():
    filename = input("Enter the file name:")
    file = open(filename,'r')
    file_content= file.read()
    space = re.findall('\s',file_content)
    tab = re.findall('\t', file_content)
    newline = re.findall('\n',file_content)
    print (space)
    print (tab)
    print (newline)
    file.close()
# count()


def count():
    file = open(r'employee.txt','r')
    F = file.read()
    count_space = F.count(' ')
    count_newline = F.count('\n')
    count_tab = F.count('    ')
    print("Spaces:",count_space,"\nTab:",count_tab,"\nNewlines:",count_newline)
# count()


# 7) Write a Python Script to open a file and replace ‘8080’ number by ‘8099’ every where

import fileinput

def digit_replace():
    filename = input("enter the file:")
    file = open(filename,'r')
    filedata = file.read()
    filedata = filedata.replace('8080','8099')
    nfile = open(filename,'w')
    nfile.write(filedata)
    file.close()
    nfile.close()

# digit_replace()


# 8) Write a Python Script to copy one file contents to another file and delete the original file

import os
def duplicate ():
    filename = input("Enter the file name:")
    file = open(filename,'r')
    filedata = file.read()
    file.close()
    newfile = input("enter the new file name:")
    newdata = open(newfile,'w')
    newdata.write(filedata)
    newdata.close()
    os.remove(filename)
# duplicate()

# 9)  Write a program that will calculate the average word length of a text stored in a file
# (i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens).


def word_avg():
    filename = input("Enter the file name:")
    file = open(filename,'r')
    filedata = file.read()
    temp = filedata.split(" ")
    total_words = len(temp)
    count = 0
    for i in temp:
        a = len(i)
        count +=a
    print("The average word length:",round(count/total_words))
    file.close()
# word_avg()

# Assignments on Modules
# ======================
# 1)  Write a Python script to to find the count of all the ext files in a folder. File extension and path are the input to the file.
# Eg : def CFiles(ext, path) , CFiles(‘.py’, ‘D:/PythonPgms’) should give the output as 12

def CFiles(ext,path):
    dirlist = os.listdir(path)
    count  = 0
    for i in dirlist:
        if i.endswith(ext):
            count += 1
        else:
            continue
    print("Total file found with the extension i.e.",ext,":",count)

# CFiles('txt',r'C:\Users\pguptha\PycharmProjects\Training')

# 2)  Implement a calculator with all the Arithmetic operators of Python.
# MyCalc.py should have definition & declaration for all the 6 Arithmetic operators of Python. CalcEx.py should import MyCalc file

# import MyCalc
#
# print (MyCalc.Addition(20,10))
# print (MyCalc.Subtract(20,10))
# print (MyCalc.Multiplication(20,10))
# print (MyCalc.Divide(20,10))
# print (MyCalc.Modulus(20,12))
# print (MyCalc.Power(10,20))



# 3) Write a Python program to determine whether a given year is a leap year

def find_leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print (year,"Is a leap year")
    else:
        print(year, "Is not a leap year")

# find_leap_year(2004)

# 4) Write a Python program to add year(s) with a given date and display the new date
# Eg : (addYears is the user defined function name)
# print(addYears(datetime.date(2015,1,1), -1))
# print(addYears(datetime.date(2015,1,1), 0))
# print(addYears(datetime.date(2015,1,1), 2))
# print(addYears(datetime.date(2000,2,29),1))
#
# Expected Output :
# 2014-01-01
# 2015-01-01
# 2017-01-01
# 2001-03-01

def addyear(a,b,c,d):
    print (datetime.date(a+d,b,c))
# addyear(2015,1,1,-1)



