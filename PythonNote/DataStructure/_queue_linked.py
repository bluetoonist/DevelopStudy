class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer


class LinkedQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.pointer
            self.count -= 1
            return value
        else:
            print("Queue is Empty")

    def enqueue(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            if self.tail:
                self.tail.pointer = node
            self.tail = node
        self.count += 1

    def size(self):
        return self.count

    def peek(self):
        return self.head.value

    def print(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()

if __name__ == '__main__':
    queue = LinkedQueue()
    print(f"큐가 비었음 {queue.isEmpty()}")
    print("데이터 추가")
    for i in range(10):
        queue.enqueue(i)
    print(f"큐가 비었음 {queue.isEmpty()}")
    queue.print()

    queue.dequeue()
    queue.print()

