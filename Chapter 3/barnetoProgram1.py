def linearSearchSorted(list, num):
    visited = []
    ind = -1
    for i in range(len(list)):
        visited.append(list[i])
        if list[i] == num:
            ind = i
            return visited, ind
        elif list[i] > num:
            return visited, ind
    return visited, ind


nums = [2, 5, 7, 9, 14, 27]
print("List:", nums)
while True:
    find = int(input("Search target: "))
    vis, index = linearSearchSorted(nums, find)

    visStr = ""
    for i in vis:
        visStr += str(i) + " "
    print("Elements visited:", visStr)

    if index != -1:
        print("Target found at position", index)
    else:
        print("Target not found")
