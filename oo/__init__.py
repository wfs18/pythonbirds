class Person:
    def __init__(self, name=None, year=0):
        self.year = year
        self.name = name

    def cumprimentar(self):
        return 'Hello'


if __name__ == '__main__':
    p = Person()
    print(p.cumprimentar())
    print(p.year)
    print(p.name)
