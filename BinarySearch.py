list = [5, 2, 1, 3, 4, 6]
list.sort()

numberToSearch = 2


def function(list, numberToSearch):
    length = len(list)
    print(int(length/2))
    if int(length/2) == 0:
        return "Not Found"
    if list[int(length/2)] == numberToSearch:
        return "Number Found"
    if list[int(length/2)] > numberToSearch:
        return function(list[0:int(length/2)], numberToSearch)
    if list[int(length/2)] < numberToSearch:
        return function(list[int(length/2)+1:length], numberToSearch)


print(function(list, numberToSearch))
