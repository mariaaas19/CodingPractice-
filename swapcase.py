# swapcase
a = "MariA"
new = []
for i in a:
    if i.islower() == True:
        new.append(i.upper())
    else:
        new.append(i.lower())
    print(new)
    result = "".join(new)
    print("result:",result, type(result))

print("swapcase", a.swapcase())
        
