#1. Read a number and check if it is divisible by 7
n=int(input("enter number"))
if n%7==0:
    print("Yes, it is divisible by 7")
else:
    print("No, it is not divisible by 7")



#2. WAP to check if the last digit is 4

n=int(input("enter number"))
if n[-1]==4:
    print("Yes, the last digit is 4")
else:
    print("No, the last digit is not 4")



#3. WAP to check if the number is divisible by 3 and the last digit is 4.

n=int(input("enter number"))
if n%3==0 and n[-1]==4:
    print("Yes,  the number is divisible by 3 and the last digit is 4. ")
else:
    print("No, the number is not divisible by 3 and the last digit is 4. ")



#4. WAP to check if the number is divisible by 7 or if the last digit is 5

n=int(input("enter number"))
if n%7==0 and n[-1]==5:
    print("Yes,  the number is divisible by 7 and the last digit is 5. ")
else:
    print("No, the number is not divisible by 7 and the last digit is 5. ")



#5. Take an integer A as input. You have to tell whether A is divisible by both 5 and 11 or not.

a=int(input("enter number"))
if a%5==0 and a%11==0:
    print("Yes,  the number is both divisible by 3 and 11 ")
else:
    print("No, the number is not divisible by 3 and 11 ")



#6. Read three integers and print their maximum.

a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if a>b and a>c:
    print("Max :",a)
elif b>a and b>c:
    print("Max :",b)
else:
    print("Max :",c)



#7. Read three angles of triangles and determine their types(Right triangle, Obtuse triangle, Acute triangle).

a=int(input("enter angle 1"))
b=int(input("enter angle 2"))
c=int(input("enter angle 3"))
if a+b+c==180:
    if a==90 or b==90 or c==90:
        print("Right triangle")
    elif a<90 and b<90 or c<90:
        print("Acute triangle")
    elif a>90 or b>90 or c>90:
        print("Obtuse triangle")
else:
    print("It is not a triangle")



#8. WAP to check whether a person is eligible to vote or not.

a=int(input("enter age of person"))
if a>=18 :
    print("Yes, person is eligible to vote ")
else:
    print("No, person is not eligible to vote ")

#9. WAP to check whether a year is a leap year or not.

a=int(input("enter year"))
if a%4==0 and a%100!=0:
    print("Leap Year")
else:
    print("Not a Leap Year")



#10.  WAP to accept a number from 1 to 7 and display the name of the day, like 1 for Sunday, 2 for Monday, etc.

n=int(input("enter day no."))
if n>1 and n<=7:
    if n==1:
        print("Sunday")
    elif n==2:
        print("Monday")
    elif n==3:
        print("Tuesday")
    elif n==4:
        print("Wednesday")
    elif n==5:
        print("Thursday")
    elif n==6:
        print("Friday")
    elif n==7:
        print("Saturday")
else:
    print("Invalid Day No.")



#11. Given 5 numbers A, B, C, D, E as input. Print the average of these 5 numbers.

a=int(input("enter number 1"))
b=int(input("enter number 2"))
c=int(input("enter number 3"))
d=int(input("enter number 4"))
e=int(input("enter number 5"))
sum=a+b+c+d+e
print("Avg :",sum/5)



#12. You are given 3 integer angles(in degrees), A, B, and C, of a triangle. You have to tell whether the triangle is valid or not. A triangle is valid if the sum of its angles equals 180.

a=int(input("enter angle 1"))
b=int(input("enter angle 2"))
c=int(input("enter angle 3"))
if a+b+c==180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")


#13. Write a program to input two numbers(A & B) from the user and print the maximum element among A & B.

a=int(input("enter number 1"))
b=int(input("enter number 2"))
if a>b:
    print("Maximum element is A")
elif a<b:
    print("Maximum element is B")
else:
    print("A and B are equal")


#14. Write a program to input three numbers(A, B & C) from the user and print the minimum element among A, B & C.

a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if a<b and a<c:
    print("Min :",a)
elif b<a and b<c:
    print("Mix :",b)
else:
    print("Mix :",c)


"""
15. Accept the percentage from the user and display the grade according to the following 
criteria. 
● 
Below 25 – D 
● 
25 to 45 – C 
● 
45 to 65 – B 
● 
65 to 85 – A 
● 
Above 85 – A+

"""

n=float(input("enter percentage"))
if n>=0 and n<25:
    print("D Grade")
elif n>=25 and n<45:
    print("C Grade")
elif n>=45 and n<65:
    print("B Grade")
elif n>=65 and n<85:
    print("A Grade")
elif n>=85 and n<=100:
    print("A+ Grade)
else:
    print("Error")
    
