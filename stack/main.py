class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack contents:", self.stack)

# Example usage
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.display()  # Output: Stack contents: [10, 20, 30]

my_stack.pop()
my_stack.display()  # Output: Stack contents: [10, 20]
