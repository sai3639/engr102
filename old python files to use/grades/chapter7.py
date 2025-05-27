# read through a file that contains class, teacher, and grades
# print class in format *** class name ***
# teacher name avg grade 




# open file
grades = open("grades.txt")
lst = [] # empty list
# iterate through file
for element in grades:
    element = element.strip() #strip white space
    if element[:6] == "Class=":
        class1 = element.split("=") # split at the '='
        name = "*** " + str(class1[-1]) + " ***"
        lst.append(name)
    else:
        class1 = element.split(" ") # split at empty space
        teach = class1[0]
        total = 0
        count = 0
        for stuff in range(1,len(class1)):
            total = total + int(class1[stuff])
            count = count + 1
        avg = total/count
        teacher = teach + " " + str(avg)
        lst.append(teacher)
for out in lst:
    print(out)




