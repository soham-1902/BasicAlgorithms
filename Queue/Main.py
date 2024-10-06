class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)  # Add item to the end of the queue

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)  # Remove the item from the front of the queue

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]  # Peek at the front of the queue

    def size(self):
        return len(self.queue)

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue contents:", self.queue)

# Example usage
my_queue = Queue()
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.display()  # Output: Queue contents: [10, 20, 30]

print("Front of the queue:", my_queue.peek())  # Output: 10
my_queue.dequeue()
my_queue.display()  # Output: Queue contents: [20, 30]
