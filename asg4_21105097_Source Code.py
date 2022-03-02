print("      QUESTION 1") 
#Defining tower of Hanoi function
def tower_of_hanoi(n , source, destination, auxiliary): 
    if n==1: 							#base case condition
         print (f"Move disk 1 from {source} to {destination}") 
         return
    tower_of_hanoi(n-1, source, auxiliary, destination)  #recursive call
    print (f"Move disk {n} from {source} {destination}") 
    tower_of_hanoi(n-1, auxiliary, destination, source)
#taking input from the user
numb_disk=int(input("Enter number of disk in tower of Hanoi: "))
print("Procedure to place all disks from Source Tower to Destination Tower is given below : ") 
#Calling the recursive function of tower of hanoi
tower_of_hanoi(numb_disk,"Source Tower","Destination","Auxiliary")



print("      QUESTION 2")
print("PASCAL'S TRIANGLE USING RECURSION")
#USING RECURSION
def pascal_triangle(n):
    if n == 1:         # Base case condition written
        return [[1]] 
    else:
        final_list = pascal_triangle(n-1) # Recursive call
        # Calculating current row using previous row
        current_row = [1]
        prev_row = final_list[-1] # Take from end of final_list
        for ele in range(len(prev_row)-1):
            current_row.append(prev_row[ele] + prev_row[ele+1])
        current_row += [1]
        final_list.append(current_row)
        return final_list

#Taking input from user
no_of_row=int(input("Enter number of rows in the Pascal's Triangle : "))
triangle = pascal_triangle(no_of_row)
#Converting the list of lists to the printing pattern
counter=0
for row in triangle:
        counter+=1
        for i in range((5-counter),0,-1):   #Iteration for white spaces
            print(" ",end="")      
        for ele in row:
            print(ele,end=" ")       #Iteration of elements
        print() 


#USING ITERATION
print("PASCAL'S TRIANGLE USING ITERATION")
#Asking for input
no_of_row=int(input("Enter number of rows: "))
list1=[]    #Creating list for help in process
for i in range(no_of_row):
    list1.append([])
    list1[i].append(1)
    for j in range(1,i):
        list1[i].append(list1[i-1][j-1]+list1[i-1][j])
    if(no_of_row!=0):
        list1[i].append(1)
#Printing the pattern
for i in range(n):
    print("   "*(no_of_row-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(list1[i][j]),end=" ",sep=" ")
    print()



                             

print("       Question3") 
#Taking input from the user
n1=int(input("Enter first Integer: "))
n2=int(input("Enter second Integer: "))
def remmod( a, b):   #function to return quotient and remainder
    quo = a%b
    rem = a//b
    return rem,quo

#Making a list of the returned values
list1= list(remmod(n1,n2))
#Storing quotient in q
q=list1[0]
#Storing Remainder in r
r=list1[1]
#printing the quotient and remainder
print("The quotient when %d is divided by %d is %d" %(n1,n2,q))
print("The remainder when %d is divided by %d is %d" %(n1,n2,r))

#Question 3(a)
print("Part A :")
result=callable(remmod(n1,n2))
if result==True:
    print("Function is callable")
if result==False:
    print("Function is not callable")

#Question 3(b)
print("Part B :")
if (n1==0 and n2==0 and q==0 and r==0):
    print("Some values are zero")
else:
    print("All the values are non zero") 
   

#Question 3(c)
print("Part C :")
#Creating new list
list_new=[q,r]
for i in range (4,7):
    list_new.append(i)
list_res=[]
#adding number > 4 from list_new to list_res
for i in list_new:
    if i>4:
        list_res.append(i)
print("Values greater than 4 are : " )
print(list_res)

#Question 3(d)
print("Part D :")
set1=set()
#adding above result in set1
for ele in list_res:
    set1.add(ele)
print("Above result is shown below: ")
print(set1)

#Question 3(e)
print("Part E :")
#Making set1 immutable
frozenset(set1)
print("The set is now immutable.")

#Question 3(f)
print("Part F :")
print(f"Max value from set is {max(set1)}")
#using hash function
hash_value=hash(max(set1))
print(f"Hash value of {max(set1)} is {hash_value}")



print("       QUESTION 4")
#forming the class Student
class student:
    #Creating constructor to create class objects
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    #defining print function
    def print_func(self):
        print(f"Name is {self.name} and "
              f"roll no. is {self.roll_no}")
    #calling destructor
    def __del__(self):
        print("Object has been deleted")
#makin an object of class student
keith_student=student("Keith",21105097)
keith_student.pfun()
del keith_student



print("      QUESTION 5")
#forming class employees
class employees:
    #Defining constructor
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def print_func(self):
        print(f"Employee Name is {self.name} and Salary is {self.salary} ")
#Creating objects for employees
emp1=employees("Mehak",40000)
emp2=employees("Ashok",50000)
emp3=employees("Viren",60000)
#printing details of employees
emp1.print_func()
emp2.print_func()
emp3.print_func()
#Updating salary of Mehak to 70000
print()
print("Part A :")
emp1.salary=70000
print("Mehak salary Updated to 70000")
emp1.print_func()
#Deleting Viren's data
print()
print("Part B :")
del emp3
print("Employee Viren's data has been removed.")



print("       Question 6")
#definig anagram function for the game
def anagram(str):
	if str=="":
		return [str]
	else:
		result=[]
		for w in anagram(str[1:]):
			for pos in range(len(w)+1):
				result.append(w[:pos]+str[0]+w[pos:])
		return result	
	
#taking names as inputs
name1=input("Enter name of first friend : ")
name2=input("Enter name of second friend : ")
#taking words spoken by written
word1=str(input("Enter Word spoken by %s : ",%(name1)))
word2=str(input("Enter Word spoken by %s : ",%(name2))
#calling anagram function
result=anagram(word1.lower())
#Printing the final result
if word2.lower() in result:
    print(f"Friendship of {name1} and {name2} is REAL")
else:
    print(f"Friendship of {name1} and {name2} is FAKE")


