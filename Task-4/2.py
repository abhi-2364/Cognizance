#displaying characters that are present at even index number
string = input("Enter a string:")
index = 0
while(len(string) > index):
    print(string[index], end ="")
    index = index + 2