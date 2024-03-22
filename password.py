newpassword = input("Enter new password: ")

result = {}

if len(newpassword) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in newpassword:
    if i.isdigit():
        digit = True
result["digits"] = digit

uppercase = False
for i in newpassword:
    if i.isupper():
        uppercase = True

result["uppercase"] = uppercase

print(result)
if all(result.values()):
    print("strong Password")
else:
    print("Weak Pqssword")