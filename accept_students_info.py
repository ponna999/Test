
num = int(input("Enter the total number of students records you want to create:"))
file = open(r'C:\Users\pguptha\PycharmProjects\Training\Code_Retreat\praneeth_61469717_08_Apr_2019.txt','w')
file.write("student_name,Gender,English,Maths,Telugu,Science,Social")
file.writelines('\n')
def student_info():
    stu_name = input("Enter the name:")
    stu_gender = input("Enter the gender M ==> Male, F ==> Female:")
    total_marks = 100
    while True:
        try:
            sub_english = int(input("Enter the marks he/she scored for the subject English:"))
        except ValueError:
            print("Please provide proper numerical value")
            continue
        else:
            break
    if (total_marks < sub_english):
        print ("Enter the number in between 1 to 100")
        sub_english = int(input("Enter the marks he/she scored for the subject English:"))
    else:
        pass
    while True:
        try:
            sub_maths = int(input("Enter the marks he/she scored for the subject Maths:"))
        except ValueError:
            print("Please provide proper numerical value")
            continue
        else:
            break
    if (total_marks < sub_maths):
        print ("Enter the number in between 1 to 100")
        sub_maths = int(input("Enter the marks he/she scored for the subject Maths:"))
    else:
        pass
    while True:
        try:
            sub_telugu = int(input("Enter the marks he/she scored for the subject Telugu:"))
        except ValueError:
            print("Please provide proper numerical value")
            continue
        else:
            break
    if (total_marks < sub_telugu):
        print ("Enter the number in between 1 to 100")
        sub_telugu = int(input("Enter the marks he/she scored for the subject Telugu:"))
    else:
        pass
    while True:
        try:
            sub_science = int(input("Enter the marks he/she scored for the subject Science:"))
        except ValueError:
            print("Please provide proper numerical value")
            continue
        else:
            break
    if (total_marks < sub_science):
        print ("Enter the number in between 1 to 100")
        sub_science = int(input("Enter the marks he/she scored for the subject Science:"))
    else:
        pass
    while True:
        try:
            sub_social = int(input("Enter the marks he/she scored for the subject Social:"))
        except ValueError:
            print("Please provide proper numerical value")
            continue
        else:
            break
    if (total_marks < sub_social):
        print ("Enter the number in between 1 to 100")
        sub_social = int(input("Enter the marks he/she scored for the subject Social:"))
    else:
        pass
    file.writelines(stu_name)
    file.writelines(',')
    file.writelines(stu_gender)
    file.writelines(',')
    file.writelines(str(sub_english))
    file.writelines(',')
    file.writelines(str(sub_maths))
    file.writelines(',')
    file.writelines(str(sub_telugu))
    file.writelines(',')
    file.writelines(str(sub_science))
    file.writelines(',')
    file.writelines(str(sub_social))
    file.writelines('\n')

for i in range(0,num):
    student_info()
#
# file = open('praneeth_61469717_08_Apr_2019.txt','r')
# new_list = file.read()
# print (new_list)