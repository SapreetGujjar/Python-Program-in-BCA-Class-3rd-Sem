# Print numbers up to N which are not divisible by 3, 6, 9,, e.g., 1, 2, 4, 5, 7,….

n = int(input("Enter N : "))
print("the numbers form 1 to",n)
print("not div by 3,6,9.....")
for i in range(1,n+1):
    if i%3!=0:
        print(i,end =",")