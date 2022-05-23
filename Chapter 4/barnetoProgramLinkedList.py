"""
File: barnetoProgramLinkedList.py

Add an insert and a remove function.

Tests the Node class.
"""

from barnetoProgramNode import Node


def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    probe = head
    count = 0
    while probe != None:
        count += 1
        probe = probe.next
    return count


def insert(index, newItem, head):
    """Inserts newItem at position is the linked structure
    referred to by head.  Returns a reference to the new
    structure."""

    if head == None:
        return Node(newItem)

    if length(head) <= index:
        # navigate to end of tree and append newItem
        probe = head
        while probe.next is not None:
            probe = probe.next
        probe.next = Node(newItem)
    else:
        if index == 0:
            next = head
            head = Node(newItem)
            head.next = next
        else:
            probe = head
            i = 0
            while probe.next is not None:
                if i == index - 1:
                    # save probe.next
                    next = probe.next
                    # set probe.next to new node
                    newNode = Node(newItem)
                    # set new node.next equal to saved probe.next
                    newNode.next = next
                    probe.next = newNode
                probe = probe.next
                i += 1

    return head


def remove(index, head):
    """Removes the item at index from the linked structure
    referred to by head and returns the tuple (head, item)
    Precondition: 0 <= index < length(head)"""
    if index < 0 or index > length(head):
        raise IndexError
    value = None
    if index == 0:
        # set head = head.next
        value = head.data
        head = head.next
    elif index == length(head) - 1:
        # navigate to end and set next to none
        probe = head
        prevProbe = None
        while probe.next is not None:
            prevProbe = probe
            probe = probe.next
        prevProbe.next = None
    else:
        # navigate to index - 1
        probe = head
        i = 0
        while probe is not None:
            if i == index - 1:
                probe.next = probe.next.next
                pass
            prevProbe = probe
            probe = probe.next
            i += 1

    return head, value


def printStructure(head):
    """Prints the items in the structure referred to by head."""
    probe = head
    while probe != None:
        print(probe.data, end=" ")
        probe = probe.next
    print()


def main():
    """Tests modifications."""
    head = None

    head = insert(0, "1", head)
    print("Insert 1 at index 0:", end=" ")
    printStructure(head)

    head = insert(1, "2", head)
    print("Insert 2 at index 1:", end=" ")
    printStructure(head)

    head = insert(0, "0", head)
    print("Insert 0 at index 0:", end=" ")
    printStructure(head)

    head = insert(3, "3", head)
    print("Insert 3 at index 3:", end=" ")
    printStructure(head)

    head = insert(1, "9", head)
    print("Insert 9 at index 1:", end=" ")
    printStructure(head)

    (head, item) = remove(0, head)
    print("First element removed:", end=" ")
    printStructure(head)

    (head, item) = remove(0, head)
    print("First element removed:", end=" ")
    printStructure(head)

    (head, item) = remove(length(head) - 1, head)
    print("Last element removed:", end=" ")
    printStructure(head)

    (head, item) = remove(1, head)
    print("Second element removed:", end=" ")
    printStructure(head)


if __name__ == "__main__":
    main()
