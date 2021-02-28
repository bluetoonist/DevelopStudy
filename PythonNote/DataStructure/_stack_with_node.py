class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer


class Stack(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    def push(self, item):
        self.head = Node(item, self.head)
        # print(self.head.value)
        self.count += 1

    def pop(self):
        if self.count > 0 and self.head:
            node = self.head
            self.head = node.pointer
            self.count -= 1
        else:
            print("Stack is Empty")

    def peek(self):
        if self.count > 0 and self.head:
            return self.head.value
        else:
            print("Stack is Empty")

    def size(self):
        return self.count

    def _printList(self):
        node = self.head
        while node:
            print(node.value, node.pointer, "\n")
            node = node.pointer

        print("\n")


if __name__ == '__main__':
    stack = Stack()
    # print(f"스택이 비었음 :{stack.isEmpty()}")
    # print("스택에 0~9를 추가")
    for i in range(10):
        stack.push(i)

    # print("Current HEAD : ",stack.head)
    print("Current HEAD : ", stack._printList())

    # print(f"스택 크기 : {stack.size()}")
    # print(f"peek : {stack.peek()}")
    # print(f"pop: {stack.pop()}")
    # print(f"peek : {stack.peek()}")
    #
    # stack._printList()
