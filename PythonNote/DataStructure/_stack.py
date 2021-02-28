class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self, value):
        value = self.items.pop(value)

        if value is not None:
            return value
        else:
            print("Stack is Empty")

    def size(self):
        return len(self.items)

    def peek(self): # 스택의 맨 마지막 데이터
        if self.items:
            return self.items[-1]
        else:
            print("Stack is Empty")

    def __repr__(self):
        return repr(self.items)


if __name__ == '__main__':
    stack = Stack()

    print(f"스택이 비었음 :{stack.isEmpty()}")
    print("스택에 0~9를 추가")
    for i in range(10):
        stack.push(i)

    print(f"스택 크기 : {stack.size()}")
    print(f"peek : {stack.peek()}")
    print(f"pop: {stack.pop(9)}")
    print(f"peek : {stack.peek()}")

    