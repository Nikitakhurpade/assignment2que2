#Write a Python program to print a dictionary whose keys should be the alphabet
#  from a-z and the value should be corresponding ASCII values
x=dict()
alphabate=range(97,123)
for i in alphabate :
    x[str(i)]=chr(i)
print(x)    