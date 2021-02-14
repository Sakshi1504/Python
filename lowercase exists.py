str="hjahJDHJHJ"

for i in str:
    if i.islower():
        print("Exists.")
        break
    else:
        print("Do not exists.")

print(any(c.islower for c in str))