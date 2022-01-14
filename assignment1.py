          #1st program
print("                 1st program")
numb1=int(input("enter first number: "))  
numb2=int(input("enter second number: "))
numb3=int(input("enter third number: "))
avg=(numb1+numb2+numb3)/3
print("average is:",avg)




           #2nd program
print("                 2nd program")
#taking input from user
gross_income=float(input("Enter your gross Income sir-$"))
Num_Dependants=int(input("Enter total number of Dependants-"))

#rounding of tax to pennies
gross_income=round(gross_income,2)

#Defnining some variable some required constant values
std_deduction=10000
dep_deduction=3000
tax=0

#calculating the taxable income
taxable_income=gross_income-std_deduction-dep_deduction*Num_Dependants

#Checking if the taxable income is greater than 0
if taxable_income>0:
    tax=0.20*taxable_income
else :
    tax=0
#printing the tax
print("Your tax = ",tax,sep="$")





                    #3rd program
print("             3rd program")

#taking input from user
SID=int(input("SID-"))
Name=input("Name-")
Gender=input("Gender(F,M orU)-")
Course_name=input("Course name-")
Course_name=Course_name.upper()
CGPA=float(input("CGPA-"))

#storing all the collected data into a list
student=[SID,Name,Gender,Course_name,CGPA]

#printing the data to check the program
print(student)






                   #4th program
print("             4th program")
#taking input from user
students=[]
print("Plz give marks as Input\n")
for i in range(0,5):
    element=int(input())
    students.append(element)

#sorting the marks of the students
students.sort()

#seperating input from output
print("*************************")

#printing the sorted result
print(*students,sep="\n")







                    #5th program
print("             5th program")
#making list of colors as specified
color =['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

print("Part a")
#Part(a)-Removing 4th elemnt and printing new list
color.pop(3)

print(color)

print("Part b")
color =['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#part(b)- Removing "Black" and "Pink" from the list
del color[3:5]; color.insert(3,'Purple')
print(color)
