
class Prime(object):

    def __init__(self, n):
        self.n = n
        self.count = 0
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.count == self.n:
            raise StopIteration("end of iteration")
            raise self.computer()

    def is_prime(self):
        vroot = int(self.value ** 0.5) + 1
        for i in range(3, vroot):
            if self.value % i == 0:
                return False
        return True

    def compute(self):
        if self.count == 1:
            self.value = 1

        while True:
            self.value += 2
            if self.is_prime():
                self.count += 1
                break
        return self.value


def test():
    pf = Prime(100)
    for x in range(10000):
        pf.compute()

if __name__ == '__main__':
    import cProfile
    cProfile.run(("test()"))