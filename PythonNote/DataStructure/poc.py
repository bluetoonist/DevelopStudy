class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer


class moduleStack(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, item):
        self.head = Node(item, self.head)
        self.count += 1
        print(self.head.value, " ", self.head.pointer)

    def showStack(self):
        node = self.head  # stack의 맨 끝
        while node:
            print("Before Node:", node, node.pointer)
            node = node.pointer  # 현재 노드를 node에 저장
            print("After Node:", node, node.pointer)
            print("=" * 20)


if __name__ == '__main__':
    stack = moduleStack()

    for i in range(9):
        stack.push(i)

    print("=" * 10)
    print(stack.showStack())
