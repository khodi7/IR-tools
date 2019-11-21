file = open("little_test.txt", "r")
a = file.readlines()
b = a[0].split()
c = []
for i in b:
    c.append(i.split("="))
    
print(c)