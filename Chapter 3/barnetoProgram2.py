def reverse(lyst, start, end):
    if start < 0:
        print("Starting index cannot be smaller than 0")
        return -1

    if end > len(lyst):
        print("Ending index cannot be larger than length of list")
        return -1

    if start >= end:
        print("Starting index must be smaller than ending index")
        return -1

    reversed = []

    # Beginning of list, before reverse
    for i in range(start):
        reversed.append(lyst[i])

    # Reversed portion of list
    for i in range(end - 1, start - 1, -1):
        reversed.append(lyst[i])

    # End of list, after reversed portion
    for i in range(end, len(lyst)):
        reversed.append(lyst[i])

    # make lyst = reversed
    # need to edit it this way to carry over the reference to the main function
    # would prefer to make this function return the reversed list, but template was given so I'll make do
    for i in range(len(lyst)):
        lyst[i] = reversed[i]


def main():
    lyst = [7, 2, 5, 9, 0, 1]
    print("Original list:", lyst)
    reverse(lyst, 0, len(lyst))
    print("Reverse whole list:", lyst)
    lyst = [7, 2, 5, 9, 0, 1]
    reverse(lyst, 0, 3)
    print("Reverse first 3 elements only:", lyst)
    lyst = [7, 2, 5, 9, 0, 1]
    reverse(lyst, 1, 5)
    print("Reverse middle 4 elements only:", lyst)
    print("Try to reverse list with starting index = -1 ")
    reverse(lyst, -1, 2)
    print("Try to reverse list with ending index = 7 ")
    reverse(lyst, 0, 7)
    print("Try to reverse list with starting index >= ending index ")
    reverse(lyst, 4, 4)


if __name__ == "__main__":
    main()
