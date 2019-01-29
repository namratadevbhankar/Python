print(list(range(1,10)))

#odd nos
print(list(range(1,10,2)))

#even nos
print(list(range(2,10,2)))

#reverese
print(list(range(10,1,-1)))

#for loop with list
alist=[10,20,30,40,50]

for val in alist:
    print(val)

#with range

for val in range(1,5):
    print(val)

#display all the keys
adict = {"chap1":10,"chap2":20,"chap3":30}
for val in adict.keys():
    print(val)

#forloop with string
name ="python programming"
for char in name:
    print(char)

aset = {10,10,10}
for val in aset:
    print(val)


adict = {"chap1":10,"chap2":20,"chap3":30}
for val in adict.keys():
    print("key:",val)
    print("Value",adict[val])
