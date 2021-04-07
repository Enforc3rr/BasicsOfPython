first = int(input("First "))
second = int(input("Second "))
third = int(input("Third "))

if (first > second) & (first > third):
    print("First ", first)
elif(second > third):
    print("second is Largest ", second)
else:
    print("Third ", third)
