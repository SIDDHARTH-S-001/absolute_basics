class Stack:
    "Stack class implemented as a list"
    def __init__(self):
        self.stack = [] # stack implemented as a python list

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, element):
        "Adds new element to the top of the stack"
        self.stack.append(element)

    def pop(self):
        "Removes the last element from the stack"
        try:
            return self.stack.pop()
        except IndexError:
            print("Stack Empty!")

    def peek(self):
        "Shows the last element of the stack"
        try:
            return self.stack[-1]
        except IndexError:
            print("Stack Empty!")

    def size(self):
        return len(self.stack)

class Queue:
    """
    Queue class implemented as a list
    """
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, element):
        "Adds new element to the end of the queue"
        self.queue.append(element)

    def dequeue(self):
        "Removes the first element from the queue"
        try: 
            return self.queue.pop(0) # removes the first entry
        except IndexError:
            print("Queue Empty!")

    def peek(self):
        "Shows first element of the queue"
        try:
            return self.queue[0]
        except IndexError:
            print("Queue Empty!")

    def size(self):
        return len(self.queue)

class Node:
    """
    Node is a vertex in the LinkedList"
    A node contains its value (data), and
    pointer to the location of the next node in the LinkedList 
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def traverseAndPrint(self):
        "Traverse and print the contents of the LinkedList"
        currentNode = self.head
        
        while currentNode:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next

        print("null")

    def findLowestValue(self):
        "Traverse through the LL & return the minValue among all nodes"
        minValue = self.head.data
        currentNode = self.head.next

        while currentNode:
            if currentNode.data < minValue:
                minValue = currentNode.data
            currentNode = currentNode.next

        return minValue

    def deleteSpecificNode(self, nodeToDelete):
        "Deletes a specific node"
        # check if the head is the node to delete
        if nodeToDelete == self.head:
            # move the head to the second node
            self.head = self.head.next
            return True

        # begin searching from the head
        currentNode = self.head
        # stop when next node is the target
        while currentNode and currentNode.next is not nodeToDelete:
            currentNode = currentNode.next

        # reached the end without finding the target
        if currentNode is None:
            print(f"Couldn't find target node containing value: {nodeToDelete.data} in the LinkedList")
            return False

        # skip the target node by connecting the previous node,
        # directly to the target's next node
        currentNode.next = nodeToDelete.next
        nodeToDelete.next = None # fully detach the target node
        # Python's built-in garbage collector will remove this node from memory,
        # provided this target node is not referenced anywhere else
        return True

    def insertNodeAtPosition(self, newNode, position):
        """
        Inserts a new node at the specified position in the LinkedList, 
        using 1-based positioning
        """
        # check for illegal case
        if position < 1:
            raise IndexError("Position must be >= 1")
        
        # check if new node should become the head
        if position == 1:
            newNode.next = self.head
            # update head
            self.head = newNode
            return True

        # start from the head node
        currentNode = self.head
        if currentNode is None:
            raise IndexError("LinkedList insertion at position out of range")
        
        # move to the node before insertion position
        for _ in range(position - 2):
            currentNode = currentNode.next  
            if currentNode is None:
                raise IndexError("LinkedList insertion at position out of range")

        # new node points to the following node
        newNode.next = currentNode.next
        # previous node points to the new node
        currentNode.next = newNode
        return True        
