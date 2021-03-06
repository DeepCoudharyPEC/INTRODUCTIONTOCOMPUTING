#ques 4
print("\nSolution for fourth ques:")
class Student:                                                                                          #Creating class Student
    def __init__(self,name,rno):
        self.name = name
        self.rno = rno
        print("Object Created\n")
    def __del__(self):
        print("\nObject destroyed")
name = input("Enter name of student: ").strip()                                                         #Inputting name and roll number from the user
roll_no = int(input("Enter SID of %s: " % (name)))
student1 = Student(name,roll_no)                                                                        #Creating object
print("The name of the student is %s and his/her roll number is %d" % (student1.name,student1.rno))     #Printing the assigned values
del student1


#ques 5
print("\nSolution for fifth ques:")
class Employee:                                                                                         #Creating class Employee
    def __init__(self,name,salary):        
        self.name = name
        self.salary = salary
    def print_data(self):
        print("%s has a salary of %d rupees" % (self.name,self.salary))
employee1 = Employee("Mehak",40000)                                                                     #Creating instances for different employees
employee2 = Employee("Ashok",50000)
employee3 = Employee("Viren",60000)
print("The current database is:")                                                                       #Printing the initial values
for i in [employee1,employee2,employee3]:
    i.print_data()

print("\na. Updated the salary of %s from %d to " % (employee1.name,employee1.salary), end = "")        #Updating salary of Mehak to 70000
employee1.salary = 70000
print(employee1.salary)

print("\nb. Deleted the record of %s(whose salary is %d)" % (employee3.name,employee3.salary))
del employee3

print("\nThe final database is:")                                                                       #Printing the final values
for i in [employee1,employee2]:
    i.print_data()                         #Deleting the object
