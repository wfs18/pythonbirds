class Person:
    olhos = 2

    def __init__(self, *children, name=None, year=0):
        self.year = year
        self.name = name
        self.children = list(children)

    def cumprimentar(self):
        return 'Hello'

    @staticmethod
    def metodo_estatico():
        return 123

    @classmethod
    def metodo_classe(cls):
        return f'{cls} - {cls.olhos}'


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
    print(p.metodo_estatico(), eu.metodo_estatico())
    print(p.metodo_classe(), eu.metodo_classe())
