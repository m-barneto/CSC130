def selectionSortDescend(lyst):
    for i in range(len(lyst) - 1):
        min_index = i
        for j in range(i + 1, len(lyst)):
            if lyst[min_index] < lyst[j]:
                min_index = j

        temp = lyst[i]
        lyst[i] = lyst[min_index]
        lyst[min_index] = temp

def main():
    lyst1 = [7, 2, 5, 9, 0, 1]
    print("Original list:", lyst1)
    selectionSortDescend(lyst1)
    print("Sorted in descending order:", lyst1)


if __name__ == "__main__":
    main()
