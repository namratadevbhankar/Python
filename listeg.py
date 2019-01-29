alist = ["google.com","unix.com","facebook.com","google.com","linkedin.com"]
print(alist)





alist=list(set(alist))
print(alist)
listlen=[]
for val in alist:
    listlen.append(len(val))

print(listlen)
print("Length of full list:",len(alist))
