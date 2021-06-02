list = []
number = int(input("Enter The Number of elements "))
for i in range(0, number):
    element = int(input("Enter the number "))
    list.append(element)
print(max(list))
