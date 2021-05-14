class Person:
    olhos = 2

    def __init__(self, *children, name=None, year=0):
        self.year = year
        self.name = name
        self.children = list(children)

    def cumprimentar(self):
        return 'Hello'


if __name__ == '__main__':
    p = Person()
    eu = Person(name='marcio')
    wes = Person(eu, name='Wesley')
    print(p.cumprimentar())
    print(p.year)  # Atributo de instancia
    print(p.name)  # Atributo de dados
    for filhos in wes.children:
        print(filhos.year)
    p.sobre = 'eu'
    print(p.sobre)
    del p.sobre
    print(p.__dict__)
    print(p.olhos)
    print(eu.olhos)