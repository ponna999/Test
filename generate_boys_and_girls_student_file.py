# file = input("Enter the file name:")
file = 'C:\\Users\\pguptha\\PycharmProjects\\Training\\Code_Retreat\\Valid_Student_names.txt'
file_content  = open(file,'r')
boys = open('C:\\Users\\pguptha\\PycharmProjects\\Training\\Code_Retreat\\boys.txt','w')
boys.write("student_name,Gender")
boys.writelines('\n')

girls = open('C:\\Users\\pguptha\\PycharmProjects\\Training\\Code_Retreat\\girls.txt','w')
girls.write("student_name,Gender")
girls.writelines('\n')

file_data = file_content.readlines()
for i in file_data:
    if i.__contains__('Gender'):
        continue
    elif i.__contains__('M'):
        boys.writelines(i)
    else:
        girls.writelines(i)
