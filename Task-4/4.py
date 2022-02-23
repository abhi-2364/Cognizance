#checking if given number is a palindrome number

i = int(input("Enter number:"))
x = i
reverse = 0
while (i>0) :
    reverse = (reverse*10) + i % 10
    i = i // 10
if (x == reverse):
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")