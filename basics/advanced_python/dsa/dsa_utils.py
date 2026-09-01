class Stack:
    """
    Implementing Stack as a custom python class gives better encapsulation. 
    Notes covered in `data_structures.ipynb`. 
    """
    def __init__(self):
        self.stack = [] # stack implemented as a python list

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        try:
            self.stack.pop()
        except IndexError:
            print("Stack Empty!")

    def peek(self):
        try:
            return self.stack[-1]
        except IndexError:
            print("Stack Empty!")

    def size(self):
        return len(self.stack)

    
            
    



    