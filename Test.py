# print ("guptha")

# fi = open('abc.txt',"r+")
# print (fi.read())

# file1 = open ("New.txt","w")
# file1.write("Hi this is praneeth started learning python \n")
# file1.write("How ever it is not difficult to learn \n")
# file1.write("It's matter of dedication you show towards it \n")
#
# file1 = open("New.txt","r")
# print (file1.read())

# num = 123
# Reverse = 0
# while( num > 0):
#     rem = num%10
#     Reverse = (Reverse*10) + rem
#     num = num//10
# print(Reverse)

# a = 1
# b = 2
# if (a > b):
#      print ("a is big")
# else:
#     print ("b is big")


# count = 0
# f = open ("New.txt",'r')
# for line in f:
#     count = count + int(line)
# print (count)


# print (dir(str))
# import string
# text = ("%d little pigs come out, or I will %s, or I will %s, I will blow your %s down."%(3, 'huff', 'puff', 'house'))
# print(text)


# def donuts(count):
#     # +++your code here+++
#     if count >= 10:
#         print ("Number of donuts:many")
#     else:
#         print ("Number of donuts:",count)
#
# def both_ends(s):
#     strlen = len(s)
#     if strlen < 2:
#         print ("String is empty")
#         exit()
#     else:
#         newstr = s[:2] + s[-2:]
#     print (newstr)

# import string
# def fix_start(s):
#     b = s[1:]
#     print(s[0] +(b.replace(s[0],'*')))

# fix_start('nirvann')

# def mix_up(a, b):
#     print("'",b[0:2]+a[2:],"",a[0:2]+b[2:],"'")
#
#
# mix_up('mix', 'pod')
# mix_up('dog', 'dinner')
# mix_up('gnash', 'sport')
# mix_up('pezzy', 'firm')

# a = 'mix'
# b = 'pod'
# b = b[0:2]
# print(b + a[2:])

# def verbing(s):
#     if len(s) >= 3:
#         if s[-3:] != 'ing':
#             s = s + 'ing'
#         else:
#             s = s + 'ly'
#     return s
#
# print(verbing('hail'))
# print(verbing('swiming'))
# print(verbing('do'))

# def front_back(a, b):
#     la = int(len(a)/2)
#     lb = int(len(b)/2)
#     if  len(a) % 2 == 1:
#         la = la + 1
#     if len(b) % 2 == 1:
#         lb = lb + 1
#     front = a[:la] + b[:lb]
#     back  = a[la:] + b[lb:]
#     return (front+back)
#     # return (la,lb)
#
# print(front_back('abcd', 'xy'))
# print(front_back('abcde', 'xyz'))
# print(front_back('Kitten', 'Donut'))

# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
# def not_bad(s):
#     a = s.find('not')
#     b = s.find('bad')
#     if a != -1 and b != -1 and b > a:
#         s = s[:a] + 'good' + s[b+3:]
#     return (s)
#
# print(not_bad('This movie is not so bad'))


# a = [1,2,3]
# b = ['a','b','b']
# for i in a:
#     print (i)
# for i in b:
#     print (i)

# def  match_ends(words):
#     count = 0
#     for a in words:
#         if len(a) >= 2 and a[0] == a[-1]:
#             count = count + 1
#     return count
# print (match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']))
# print(match_ends(['', 'x', 'xy', 'xyx', 'xx']))
# print(match_ends(['aaa', 'be', 'abc', 'hello']))

# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.

# def front_x(words):
#     n = sorted(words)
#     return n
#
# # print(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']))
# # front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
# # front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
#
#
# a = ['axx', 'bbb', 'ccc', 'xaa', 'xzz']
# a = ['ccc', 'bbb', 'aaa', 'xcc', 'xaa']
# a = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
#
# def front_x(words):
#     na = []
#     nb = []
#     for i in words:
#         b = i[:1]
#         if b == 'x':
#             na.append(i)
#         else:
#             nb.append(i)
#     n = sorted(na) + sorted(nb)
#     return n
#
# print(front_x(['axx', 'bbb', 'ccc', 'xaa', 'xzz']))
# print(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']))
# print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))



# na = []
# nb = []
# for i in a:
#     b = i[:1]
#     if b == 'x' :
#         na.append(i)
#     else:
#         nb.append(i)
#         # na = na + [i]
# # print (na)
# # print (nb)
# new = sorted(na) + sorted(nb)
# print (new)


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.

# def last(a):
#     return a[-1]
#
# def sort_last(tuples):
#     return sorted(tuples,key=last)
#
# print (sort_last([(1, 3), (3, 2), (2, 1)]))


# def remove_adjacent(nums):
#     result = []
#     for num in nums:
#         if len(result) == 0 or num != result[-1]:
#             result.append(num)
#     return result
# print (remove_adjacent([2, 2, 2, 2]))

# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.

# def linear_merge(list1, list2):
#     list1 = sorted(list1)
#     list2 = sorted(list2)
#     list3 = list1 + list2
#     return sorted(list3)
#
# print(linear_merge(['aa', 'xx', 'zz'],['bb', 'cc']))
# print(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']))
# print(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']))

import re
# def print_words(filename):
#     fopen = open(filename,'+r')
#     a = fopen.read()
#     regex = r'\w+'
#     list = re.findall(regex,a)
#     # print (list)
#     # print (match)
#     # return (len(list))
#     count = 0
#     for i in list:
#         count = count + 1
#         print (i,count)
#
# print_words('abc.txt')
# import re
# a = "Hi this is praneeth guptha"
# match = re.findall(r'\s', a)
# print (len(match))

# def print_top(filename):
#     fopen = open(filename,'+r')
#     fopen = fopen.read()
#     regex = r'\w+'
#     list = re.findall(regex,fopen)
#     list1 = list[0:20]
#     return (sorted(list1))
# print (print_top('abc.txt'))

# def word_count_dict(filename):
#   """Returns a word/count dict for this filename."""
#   # Utility used by count() and Topcount().
#   word_count = {}  # Map each word to its count
#   input_file = open(filename, 'r')
#   for line in input_file:
#     words = line.split()
#     for word in words:
#       word = word.lower()
#       # Special case if we're seeing this word for the first time.
#       if not word in word_count:
#         word_count[word] = 1
#       else:
#         word_count[word] = word_count[word] + 1
#   input_file.close()  # Not strictly required, but good form.
#   return word_count

#
# def word_dict_count(filename):
#     input_file = open(filename,'r+')
#     word_dict = {}
#     for lines in input_file:
#         words = lines.split()
#         for word in words:
#             word = word.lower()
#             if not word in word_dict:
#                 word_dict[word] = 1
#             else:
#                 word_dict[word] = word_dict[word] + 1
#     # word_dict = sorted(word_dict.keys())
#     input_file.close()
#     return word_dict
# 
# def print_words(filename):
#     word_dict = word_dict_count(filename)
#     # print (word_dict)
#     words = sorted(word_dict.keys())
#     # print (words)
#     for word in words:
#         print (word, word_dict[word])
#
#
#
# print_words('abc.txt')


# dict = {'a' : 1, 'b' : 2}
# print (dict)
