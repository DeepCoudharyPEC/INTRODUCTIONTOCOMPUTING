                                                #ASSIGNMENT 3
#Ques 1:
#checking number of different words or character entered by user
print("answer of ques 1:")
c=input("enter text:")
d=dict()
for character in c:
    if character not in d:
        d[character]=1
    else:
        d[character]=d[character]+1
d.pop(" ")
print("number of different characters:",d)
e=c.split()
f=dict()
for word in e:
    if word not in f:
        f[word]=1
    else:
        f[word]=f[word]+1
print("number of different words:",f)
#######################################################################################
#Ques 2
#to check next date of the date entered by user
print("\nanswer of ques 2")
print("please enter date,month,year & 1800<=year<=2025")
date=int(input("enter date:"))
month=int(input("enter month:"))
year=int(input("enter year:"))
if 1800<=year<=2025 and month in (1,3,4,5,6,7,8,9,10,11,12) and date<30:
    date+=1
    print("next date of above date")    
    print("%d"%date + "/%d"%month + "/%d"%year)
elif 1800<=year<=2025 and month in (1,3,5,7,8,10) and date==30:
    date+=1
    print("next date of above date")    
    print("%d"%date + "/%d"%month + "/%d"%year)
elif 1800<=year<=2025 and month in (1,3,5,7,8,10) and date==31:
    date=1
    month=month+1
    print("next date of above date")    
    print("%d"%date + "/%d"%month + "/%d"%year)
elif 1800<=year<=2025 and month==12 and date==30:
    date+=1
    print("next date of above date")    
    print("%d"%date + "/%d"%month + "/%d"%year)
elif 1800<=year<=2025 and month==12 and date==31:
    date=1
    month=1
    year+=1
    print("next date of above date")    
    print("%d"%date + "/%d"%month + "/%d"%year)
elif 1800<=year<=2025 and year%4==0 and month==2 and date<29:
    date+=1
    print("next date of above date")    
    print("%d"%date + "/%d"%month + "/%d"%year)
elif 1800<=year<=2025 and year%4==0 and month==2 and date==29:
    date=1
    month+=1
    print("next date of above date")    
    print("%d"%date + "/%d"%month + "/%d"%year)
elif 1800<=year<=2025 and year%4 in (1,2,3) and month==2  and date<28:
    date+=1
    print("next date of above date")    
    print("%d"%date + "/%d"%month + "/%d"%year)
elif 1800<=year<=2025 and year%4 in (1,2,3) and month==2  and date==28:
    date=1
    month+=1
    print("next date of above date")    
    print("%d"%date + "/%d"%month + "/%d"%year)
else:
    print("Please recheck what had been entered!!")    
########################################################################################
#Ques 3
#to check the square of three numbers entered by user
print("\nanswer of ques 3:")
print("enter three number to be squared")
x=int(input("enter no.1:"))
y=int(input("enter no.2:"))
z=int(input("enter no.3:"))
a=[x,y,z]
b=list()
for no in a:
    b.append(no**2)
zip(a,b)
print(list(zip(a,b)))
########################################################################################
#Ques 4
#to check the performance of candidate on the basis of their respective grade
print("\nanswer of ques 4")
print("enter your grade to check performance")
print("*should be in between(4 to 10)")
gr=int(input("your grade [integer]:"))
while gr<4 or gr>10:
    print("Not in range, please check entered grade.")
    gr=int(input("your grade[integer]:"))
    if 4<=gr<=10:
        break
if gr==4:
    print("Your grade is 'D' and poor performance.")
elif gr==5:
    print("Your grade is 'C' and below average performance.")
elif gr==6:
    print("Your grade is 'C+' and average performance.")
elif gr==7:
    print("Your grade is 'B' and good performance.")
elif gr==8:
    print("Your grade is 'B+' and very good performance.")
elif gr==9:
    print("Your grade is 'A' and excellent performance.")
elif gr==10:
    print("Your grade is 'A+' and outstanding performance.")
#################################################################################
#Ques 5
#to show pyramid of alphabets
print("\nanswer of ques 5:")
print("<Showing magic pyramid of alphabets>")
blocks="ABCDEFGHIJK"
i,j=11,0
while i>=0 and j<6:
    print((" "*j) + blocks[0:i])
    i=i-2
    j=j+1 
#################################################################################
#Ques 6
#to make list of names and SID entered by candidate
print("\nanswer of ques 6:")
print("Please specify your respective name and SID.")
print("When completed press enter.")
d=dict()
while True:
    a=input("Enter name:")
    b=input("Enter SID:")
    d[a]=b
    if a=="" or b=="":
        d.pop("")
        break
print(d)
print("Done!")
#####################################################################################################
#Ques 7
#to make fibonacci sequence of entered number
print("\nanswer of ques 7:")
n=int(input("For Fibonnaci sequence, enter 1st number:"))
print("Fibonacci sequence for given 'n':")
i=0
n1=n+n
l=[n,n,n1]
while n>0 and n1>0:
    n=n+n1
    l.append(n)
    n1=n+n1
    l.append(n1)
    i=i+1
    if i==50:
        break
print(l)  
############################################################################################################
#Ques 8
#regarding sets
print("\nanswer of ques 8:")
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}
print("a.",Set1^Set2)
Set4=Set1-((Set1&Set2)|(Set1&Set3)) #exactly in Set1
Set5=Set2-Set1 
Set6=Set3-Set1 
print("b. i.exactly in Set1:",Set4,"\nii.exactly in Set2:",Set5,"\niii.exactly in Set3:",Set6)
Set7=Set1&Set2
Set8=Set1&Set3
print("c. i.exactly in Set1 and Set2:",Set7,"\nii.exactly in Set1 and Set3:",Set8)
l=list()
i=1
while i<11:
    l.append(i)
    i=i+1
Set9=set(l)
Set10=Set9-Set1
print("d.",Set10)
Set11=Set9-(Set1|Set2|Set3)
print("e.",Set11)
#################################################################################################################

    
