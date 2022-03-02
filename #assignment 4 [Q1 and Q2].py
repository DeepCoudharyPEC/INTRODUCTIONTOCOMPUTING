#ques 1
print("Solution for first ques:")
count = 0
def towerofhanoi(n, initial_rod, final_rod, extra_rod):
    global count
    if n == 0:                                                                                          #Base case
        return
    count += 1
    towerofhanoi(n-1, initial_rod, extra_rod, final_rod)                                                #Recursive call
    print("Move disk",n,"from rod",initial_rod,"to rod",final_rod)
    towerofhanoi(n-1, extra_rod, final_rod, initial_rod)

no_of_discs = int(input("Number of discs: "))
print("\nA is the initial rod\nB is the extra rod\nC is the final rod\n\nSteps:")
towerofhanoi(no_of_discs, 'A', 'C', 'B')
print("\nNumber of steps will be: %d" % (count))

#ques 2
print("\nSolution for second ques:")
from math import comb
while True:                                                                                             #Loop for preventing -ve input of no. of rows (because they can't be -ve)
    n = int(input("Enter the number of rows you want to print: "))                                      #Asking the user the number of rows he/she wants
    if n >= 0:
        break
    else:
        print("Number of rows must be positive, please enter the value again!")

#RECURSION
print("The Pascal's Triangle using recursion is:")
def pascaltriangle(num):
    if num == 0:
        return [[0]]
    elif num == 1:                                                                                      #Base case
        return [[1]]
    else:
        result = pascaltriangle(num-1)                                                                  #Recursive call
        current_row = [1]                                                                               #The first element of each row, i.e. 1
        previous_row = result[-1]                                                                       #Taking the last row from the data of all rows
        for i in range(len(previous_row)-1):
            current_row.append(previous_row[i] + previous_row[i+1])
        current_row += [1]                                                                              #The last element of each row, i.e. 1
        result.append(current_row)                                                                      #Adding the computed row to the data of all rows
    return result
for i in pascaltriangle(n):
    print((n-len(i))*" ",end="")                                                                        #This print() adds space before printing each row
    for j in i:
        if j != 0:
            print(j, end =" ")
    print()

#ITERATION
print("The Pascal's Triangle using iteration is:")
for i in range(n):                                                                                      #Outer loop is for the rows
    print((n-i-1)*" ",end="")                                                                           #This print() adds space before printing each row
    for j in range(n):                                                                                  #Inner loop is for the individual elements to be printed
        if comb(i,j) != 0:                                                                              #Condition to ignore the cases when combination = 0 (when j>i)
            print(comb(i,j),end=" ")                                                                    #This print() prints each element and adds space after printing each value
    print()                                                                                             #This print() is for changing line for next row
