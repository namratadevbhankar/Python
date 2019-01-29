print("Hello gm")

alist=[10,20,30]
print("Elements are :",alist)
print("Second element is :",alist[1])

blist=["unix","oracle","perl"]
print("Languages are :", blist)

clist=[10,20,"python",40,"java"]
print("List items are :",clist)

clist[2]=70

print("Now List items are :",clist)
print(alist)


dlist = [10,20,30,40]
print(dlist)

dlist.append(50)

dlist.insert(3,5)
#3 shows position
print(dlist);

#clearing the list
#dlist.clear()

removed=dlist.pop(0)

print(removed)
print(dlist)

#reversing happens inplace
dlist.reverse()
print("After reversing :",dlist)
