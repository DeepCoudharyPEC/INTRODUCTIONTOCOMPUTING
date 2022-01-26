#ASSIGNMENT 2
#Ques 1
print("\nanswer of ques 1:")
text="Python is a case sensitive language."
text_a=len(text) #number of characters in text
print("a:", text_a)
text_b=text[::-1] #reversing the order
print("b:", text_b)
text_c=text[10:26] 
print("c:", text_c)
text_d=text.replace("a case sensitive", "object oriented")
print("d:", text_d)
text_e=text.find("a")
print("e:", text_e)
text_f=text.replace(" ", "")
print("f:", text_f)
#############################################################################
#Ques 2
print("\nanswer of ques 2:")
name="Deep Choudhary"
SID="21105008"
Department_name="ECE"
CGPA="9.9"
print("Hey, " + name + " Here!")
print("My SID is " + SID)
print("I am from " + Department_name + " department and my CGPA is " + CGPA)
#############################################################################
#Ques 3
print("\nanswer of ques 3:")
a=56
b=10
print("a.", a&b)
print("b.", a|b)
print("c.", a^b)
print("d.", a<<2, b<<2)
print("e.", a>>2, b>>4)
#############################################################################
#Ques 4
print("\nanswer of ques 4:")
numb1=int(input("enter 1st number: "))
numb2=int(input("enter 2nd number: "))
numb3=int(input("enter 3rd number: "))
if numb1>numb2 and numb1>numb3:
    print("1st number is greatest.")
elif numb2>numb1 and numb1>numb3:
    print("2nd number is greatest.")
else:
    print("3rd number is greatest.")
##############################################################################
#Ques 5
print("\nanswer of ques 5:")
sentence=input("Type any sentence: ")
if "name" in sentence: # whether 'name' is there in typed sentence
    print("Yes,'name' is there.")
else:
    print("No,'name' is not there.")
##############################################################################    
#Ques 6
print("\nanswer of ques 6:")
side1=float(input("side 1: "))
side2=float(input("side 2: "))
side3=float(input("side 3: "))
s1=int(side1)
s2=int(side2)
s3=int(side3)
#Checking whether triangle is possible.            
if s1+s2>s3 and s2+s3>s1 and s1+s3>s2: 
    print("Yes possible")
else:
    print("No not possible")
##############################################################################    

        

    
    
    
          
