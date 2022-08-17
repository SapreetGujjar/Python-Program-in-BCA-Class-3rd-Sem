# Compute and print roots of quadratic equation ax2+bx+c=0, where the values of a, b, and c are input by the user.
 
 import math
 a = int(input("Enter the coefficient of x square : "))
 b = int(input("Enter the coefficient of x : "))
 c = int(input("Enter constant: "))
 disc =b*b - 4*b*c 
 print("Discriminant = ",disc)
 if disc == 0:
    print("Roots are Real and Equal")
    r1 = (-b)/(2*a)
    r2 = (-b)/(2/a)
    print("First Root :",r1)
    print("second Root :",r2)
elif disc > 0 :
    print("Roots are Real and Unequal")
    r1 = ((-b)+(math.sqrt(disc)))/(2*a)
    r2 = ((-b)-(math.sqrt(disc)))/(2*a)
    print("First Root :",r1)
    print("second Root :",r2)
else:
    print("Roots are imginary")    