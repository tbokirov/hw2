class Human:
    head = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def running(self):
        print(f'{self.name} умеет ходить')


hum = Human('Султан', 17)


class Student(Human):
    def __init__(self, name, age, status=True):
        super().__init__(name, age)
        Human.__init__(self, name, age)
        self.status = status

    def running(self):
        print(f'{self.name} теперь умеет бегать')


student1 = Student('Барсбек', 61, False)
student1.running()
hum.running()
print(student1.status)


class Tefal:
    def fire(self=True):
        print('нагрел воду')

    def _on(self=True):
        print('включить тефаль')

    def __woter(self):
        print('налить воду')

    def __run(self=True):
        print('запустить')

    def _off(self=1):
        print('экстренное выключение')


t = Tefal





