x = input("Enter string: ")

str = ""

# for i in range((len(x)-1),-1,-1):
# str=x[i]+str
for i in x:
    str = i+str
if x.lower() == str.lower():
    print("Palindrome")
else:
    print("Not a palindrome")