#QUESTION-1
print("Solution to Question-1 \n")
Str = "Python is a case sensitive language"
print("The length of the string is : ",len(Str))                     #finding and printing length of string
Reversed_Str = Str[ : : -1]
print("The reversed string is : ",Reversed_Str)                      #printing the reversed string
new_Str = Str[10:26]
print("The new string is : ",new_Str)
replaced_str= Str.replace( 'a case sensitive','object oriented')     #using replace function to produce new string
print ("The replaced string will be : ",replaced_str)
index=Str.find('a')  
if (index == -1):
    print("Sorry, the String dosen't contain the substring 'a'")
else :                                               
    print("The index of 'a' in the given String is : ",index)            #printing index of substring "a"
Str_withoutspace= Str.replace(" ","")
print("The given input without white spaces is : ",Str_withoutspace)    #printing the string without white spaces



#QUESTION-2
print("Solution to Question-2 \n")
#TAKING INPUTS
name = input("Enter your name : ")
sid = int(input("Enter SID : "))
DeptName=input("Enter department name : ")
cgpa= float(input("Enter CGPA : "))
#PRINTING THE OUTPUT
print("\nHey, %s Here!\nMy SID is %d\nI am from %s department and my CGPA is %.1f" %(name,sid,DeptName,cgpa))



#QUESTION-3
print("Solution to Question-3 \n")
a=56
b=10
print("Value of a & b is : %d" %(a & b))						#part a
print("Value of a | b is : %d" %(a | b))						#part b
print("Value of a ^ b is : %d" %(a ^ b))						#part c
print("Left shift both a and b with 2 bits : a= %d, b=%d" %(a <<2, b<<2))		#part d
print("Right shift a with 2 bits and b with 4 bits : a= %d, b=%d" %(a >>2, b>>4))	#part e



#QUESTION-4
print("Solution to Question-4 \n")
#Taking input from the user
Numb1= int(input("Enter first number : "))
Numb2= int(input("Enter second number : "))
Numb3= int(input("Enter third number : "))
#Process
if ((Numb1 >= Numb2) and (Numb1 >= Numb3)):
    print("The greatest of the three numbers is : %d " %Numb1)
elif ((Numb2 >= Numb1) and (Numb2 >= Numb3)) :
    print("The greatest of the three numbers is : %d" %Numb2)
else :
    print("The greatest of the three numbers is : %d" %Numb3)   #If above conditions dosen't satisfy then it's clear that numb3 must be greatest



#QUESTION-5
print("Solution to Question-5 \n")
str= input("Enter String : ")           #Input taken
if "name" in str :			#Checking the condition	
	print("Yes")
else :
	print("No")



#QUESTION-6
print("Solution to Question-6 \n")
#TAKING INPUT FROM USER
len1 =float(input("Enter length of first side of the triangle : "))
len2 =float(input("Enter length of second side of the triangle : "))
len3 =float(input("Enter length of third side of the triangle : "))
#CONVERTING THE LENGTHS INTO INTEGER
len1=int(len1)
len2=int(len2)
len3=int(len3)
if ( (len1 > len2+len3) or (len2 > len1+len3) or (len3 > len2+len1)) :  #Checking through condition
	print ("No")
else :
	print ("Yes")











