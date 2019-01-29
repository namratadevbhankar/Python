#prog to display if string is short or long

str=input("Enter string");
print(str)

if len(str) < 5:
    print("String too short")

elif len(str) > 10:
    print("String too long")

else:
    print("String length okay")
