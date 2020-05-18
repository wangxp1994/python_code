# property的简单例子

class Student(object):
    def __init__(self, _score):
        self._score = _score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


if __name__ == "__main__":
    a = Student(100)
    a.score = 90
    print(a.score)
