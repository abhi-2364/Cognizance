#printing a pattern
rows = int(input("Enter number of rows:"))
for a in range (rows) :
    for b in range(rows-a-1) :
        print(" ",end="")
    for b in range(a+1):
        print("*",end=" ")
    print()