# Print multiplication table of a number input by the user.
number = int(input ("Enter the number of print the multiplication table: "))             
print ("The Multiplication Table of: ", number)    
for count in range(1, 11):      
   print (number, 'x', count, '=', number * count)    