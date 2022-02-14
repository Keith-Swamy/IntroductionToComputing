print("         QUESTION 1       ")
#Taking input
str_in = input("Enter the sentence or the word to count the occurrences for : ")
#Storing the elements in a list
list= str_in.split()
if(len(list) ==1):
	#Case when input is a single word
        dict={}
        str = str_in.lower()
	#Looping through all alphabets
        for i in range(97,123):
                count=0       #Counter to find occurrences of the characters
                for j in str:
                        if(j==chr(i)):
                                count+=1
                if(count>0):
                        dict[chr(i)]=count
        print(dict)
else :  
	#Case when input is a sentence
        dict={}
        set1= set()
        for i in list:
                set1.add(i.lower())
        for i in set1:
                count=0       #Counter to find occurrences of the words
                for j in list:
                        if(j.lower()==i):
                                count+=1
                dict[i]=count
        print(dict)        
        


        
        
        
print("        QUESTION 2        ")
#creating a list to store number of days in the particular months
days_in_a_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
def leap_year():
	#condition for leap year
        if(((year%4==0) and not(year%100==0)) or ((year%4==0) and (year%400==0))):
           return True
        else :
           return False
#Taking input from user
day= int(input("Enter day between 1 and 31 : "))
month= int(input("Enter month between 1 and 12 : "))
year= int(input("Enter year between 1800 and 2025 : "))
#Checking for wrong inputs
if(31<day<1 or 12<month<1 or 2025<year<1800):
          print("Error! Kindly imply with the input constraints")
elif(month==2 and leap_year and day>29):
        print("Error! The month of February has only 29 days in a leap year")
elif(month==2 and not(leap_year) and day>28):
        print("Error! The month of February has only 28 days in a non-leap year")        
else:
        if(leap_year()):
           days_in_a_month[2]= 29  #changed 28 days in february to 29 days
        else :
           days_in_a_month[2]= 28
        if(day>days_in_a_month[month]):
                day=1
                month+=1
                if(month > 12):
                        month=1
                        year+=1
                else :
                        month+=1
        else:
                day+=1
        print("Next Date (in day/month/year format) is: %d/%d/%d" %(day,month,year))



   
                        
         
print("     QUESTION 3     ")
list_in = []
n= int(input("Enter number of elements in the list : "))
if(n>0):
	#filling the list
        for i in range (0,n):
        	t= int(input("Enter a non-negative integer %d :" %(i+1)))
        	list_in.append(t)
	list_out=[]
	for i in list_in :
    		tuple=(i,i**2)  #filling the tuple with squares of the elements
     		list_out.append(tuple)
	print("The List of tuples is : ", list_out)
else:
	print("Error! Number of elements cannot be a non-positive number")





print("     QUESTION 4     ")
grade_in = int(input("Enter the grade between between 4 and 10 : "))
if(3<grade_in<11):
	#Creating lists for grades and performance
	list_grade=['A+','A','B+','B','C+','C','D']
	list_performance = ["Outstanding", "Excellent", "Very Good", "Good", "Average", "Below Average", "Poor"]
	print("Your Grade is '%s' and %s" %(list_grade[(10-grade_in)],list_performance[(10-grade_in)]))
else:
	print("Error! Please imply with the input constraints")
      


      

print("      QUESTION 5      ")
print("The pattern is as follows :")
s = "ABCDEFGHIJK"
k=0           #iterating element for inner loop
n=11	      #element for producing  substrings of the pattern
for i in range(6):
        print()
	#Loop for creating white spaces
        for j in range(k):
                print(' ',end='')
        print (s[0:n], end='')
	#updating variables so that a pyramid may be formed
        n=n-2
        k=k+1




print("       Question 6      ")
dict= {}
while True:
	#Asking choice from the user
        choice= input("Enter 'Y' if you want to add details otherwise enter 'N' : ")
        if (choice.upper() == 'Y'):
                name= input("Enter name of the student : ")
                SID= int(input("Enter SID of the student : "))
		#Storing the input in a dictionary
                dict[SID]=name
        else:
                break
#Printing details of the students
print()
print ("Part A : ")
print("Following are the details of the students : ")
dict_items= dict.items()
for sid,name in dict_items:
        print("Name = %s  SID = %s " %(name,sid))

#Printing sorted dictionary using student names
print()
print ("Part B : ")
dict2= sorted(dict.values())
print("The sorted dictionary using student names is : ", dict2)

#Printing sorted dictionary using SID
print()
print ("Part C : ")
dict2=sorted(dict.keys())
print("The sorted dictionary using SID is : ", dict2)

#Searching for the student
print()
print("Part D : ")
search_ele = int(input("Enter SID of the student whose name is to be found : "))
if search_ele in dict.keys():
        print("Name of the student having %d as SID is : %s" %(search_ele,dict[search_ele]))
else :
        print("No student was found with the SID %d" %(search_ele))
        
  
        
        

        

              
print("       QUESTION 7       ")
n= int(input("Enter number of elements you want in the Fabonacci sequence : "))
if(n<=0):
        print ("Error! Number of elements cannot be negative or zero")
elif (n==1):
        print ("The Fibonacci sequence is : ",0)
        print("Average of the resultant Fibonacci sequence is : ",0)
elif (n==2):
        print ("The Fibonacci sequence is : %d  %d" %(0,1))
        print("Average of the resultant Fibonacci sequence is : ",0.50)
else:
        first_ele= 0        #First element of the fibonacci series
        second_ele=1	    #Second element of the fibonacci series
        print ("The Fibonacci sequence is : ")
	#Printing the first two elements of the Fibonacci series
        print("0  1  ", end='')      
        sum=1    #variable to store the sum of the series
        temp_var= 0    #temperoray variable to store the sum temporarily
        for i in range(0,(n-2)):
                temp_var= first_ele + second_ele
		#Updating values of first_ele and second_ele
                first_ele = second_ele
                second_ele = temp_var
                sum+= temp_var  #Sum being stored
                print(temp_var, end="  ")
	#Calculating average
        avg= sum/n;
        print("\nAverage of the resultant Fibonacci sequence is : %.2f" %(avg))



print("        QUESTON 8        ")
#Declaring and printing the sets
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
print ("Given sets -- ")
print ("Set1= {1, 2, 3, 4, 5}")
print ("Set2= {2, 4, 6, 8}")
print ("Set3= {1, 5, 9, 13, 17}")
       
       
print()
print("Part (a) : ")
new_set_a= Set1^Set2   #using the symmetric difference operator
print("The new set of all elements that are in Set1 and Set2 but not both is : ")
print(new_set_a)

print()
print("Part (b) : ")
new_set_b= Set1^Set2^Set3
print("The new set of all elements that are in only one of the three sets Set1,Set2 and Set3 is : ")
print(new_set_b)

print()
print("Part (c) : ")
new_set_c= (Set1|Set2|Set3)-(Set1^Set2^Set3)-(Set1&Set2&Set3)
print("The new set of elements that are exactly in two of the sets Set1, Set2 and Set3 is : ")
print(new_set_c)

print()
print("Part (d) : ")
Set4 = {1,2,3,4,5,6,7,8,9,10}
new_set_d= Set4 - Set1
print("The new set of all integers in the range 1 to 10 that are not in Set1 is : ")
print(new_set_d)

print()
print("Part (e) : ")
Set4 = {1,2,3,4,5,6,7,8,9,10}
new_set_e= Set4 - Set1 - Set2- Set3
print("The new set of all integers in the range 1 to 10 that are not in Set1,Set2 and Set3 is : ")
print(new_set_e)

        
                
                
        
        
        
        
        

        


   
        
