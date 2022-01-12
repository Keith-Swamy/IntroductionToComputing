#Question 1
Numb1= int(input("Enter first number : "))
Numb2= int(input("Enter second number : "))
Numb3= int(input("Enter third number : "))
avg = (Numb1 + Numb2 + Numb3)/3
print("Average of the numbers is : ",avg)


#Question 2
GI= int(input("Enter Gross Income to the nearest penny : "))
Deps= int(input("Enter number of dependents : "))
TaxableIncome = GI - 10000 - (Deps*3000)
tax= TaxableIncome*(0.2)
print("Your income tax is : ",tax)


#Question 3
Student = [21105097, 'Keith Swamy','M','ECE',9.3]
print(Student)


#Question 4
Mks1 = float(input("Enter marks of student 1 : "))
Mks2 = float(input("Enter marks of student 2 : "))
Mks3 = float(input("Enter marks of student 3 : "))
Mks4 = float(input("Enter marks of student 4 : "))
Mks5 = float(input("Enter marks of student 5 : "))
MarksList = [Mks1,Mks2,Mks3,Mks4,Mks5]
print("List before sorting : ",MarksList)
MarksList.sort()
print("List after sorting : ",Markslist)


#Question 5 (a)
color= ['Red','Green','White','Black','Pink','Yellow']
color.pop(3)
print(color)


#Question 5 (b)
color= ['Red','Green','White','Black','Pink','Yellow']
color[3:5]=["Purple"]
print(color)