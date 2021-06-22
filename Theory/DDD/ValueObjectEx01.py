nickName = "jak 010"

# nickName 을 분리하면 아래와 같다
firstNick, secondNick = nickName.split(" ")

print(firstNick + secondNick)

#  But,
# 다음과 같은 닉네임을 사용하게 되면 부자연스럽다.
# 의도했던 순서가 아니게 됨
nickName = "010 jak"

firstNick, secondNick = nickName.split(" ")

print(firstNick + secondNick)


# OOP에서는 다음과 같이 클래스로 정의된 객체를  사용하는데
# 시스템이 어떤 처리를 해야 하는지에 따라 값을 나타내는 적합한 표현이 정해짐
# 객체이기도하고 값이기도 하다
class NickName(object):
    def __init__(self, firstNick, secondNick):
        self._firstNick = firstNick
        self._seconNick = secondNick

    @property
    def firstNick(self):
        return self._firstNick

    @property
    def secondNick(self):
        return self._seconNick

    @property
    def nickname(self):
        return self._firstNick + self._seconNick


if __name__ == '__main__':
    user = NickName(firstNick="jak", secondNick="010")
    print(user.nickname)
