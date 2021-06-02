length = int(input("Enter Size :"))
list = []
for i in range(0, length):
    element = int(input("Enter The Number : "))
    list.append(element)
numberToSearch = int(input("Enter Number To Search : "))
for i in range(0, length):
    if list[i] == numberToSearch:
        print(str(numberToSearch) + " Found at " + str(i+1))
        break
