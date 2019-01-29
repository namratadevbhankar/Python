word = input("Enter string : ")
print(word)
word = list(word)
print(word)

word.reverse()
print(word)
#convertingto string
finalword = "".join(word)
print(finalword)

#method 2

name = "python"

## string[start:stop:stop]

print(name[0:3])
print(name[::-1])


