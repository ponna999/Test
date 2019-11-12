# file = input("Enter the file name:")
file = 'C:\\Users\\pguptha\\PycharmProjects\\Training\\Code_Retreat\\praneeth_61469717_08_Apr_2019.txt'
file_data = open(file,'r')
new_list = file_data.readlines()
new = []
file = open(r'C:\Users\pguptha\PycharmProjects\Training\Code_Retreat\Valid_Student_names.txt','w')
for i in new_list:
    if i not in new:
        new.append(i)
        file.writelines(i)


