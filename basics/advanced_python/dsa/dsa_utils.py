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
    