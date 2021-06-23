class User(object):

    def __init__(self, name):
        if len(name) < 3:
            raise ValueError("Error Error")

        self.name = name

    def change_name(self, change_name):

        if len(change_name) > 3:
            self.name = change_name

        return self.name


if __name__ == '__main__':
    # 엔티티는 수정을 위해 객체를 교환하지 않는다.
    #  - 엔티티를 수정하려면 객체의 행동을 통해 수정하면 된다

    # 주의
    #   엔티티는 필요에 따라 가변으로 만들 수 있는 객체일 뿐이다.

    user = User("jak")
    user.change_name("jak010")
