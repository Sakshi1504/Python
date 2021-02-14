#program to concatenate N strings
N=int(input("Enter number of strings:"))
res=""
for i in range(N):
    str1=input("Enter String:")
    res+=str1
print("Concatenated String: ", res)

listofsiblings=['Dolli','Juli', 'Mukul', 'Munmun', 'Ikchha', 'Dhruv']
siblings='*'.join(listofsiblings)
print(siblings)