# Exemplo 1 - Calculadora Simples
class Calculadora:

    def __init__(self, a, b):

        self.a = a
        self.b = b
    
    def soma(self):
        return self.a + self.b
    
    def subtracao(self):
        return self.a - self.b
    
    def multiplicacao(self):
        return self.a * self.b
    
    def divisao(self):
        return self.a / self.b

#user.py
class User:

    seq = 0
    objects = []

    def __init__(self, nome, idade):
        self.id = None
        self.nome = nome
        self.idade = idade

    def save(self):
        self.__class__.seq += 1
        self.id = self.__class__.seq
        self.__class__.objects.append(self)

    def __str__(self):
        return self.nome
    
    def __repr__(self):
        return '<{}: {} - {} - {}>\n'.format(self.__class__.__name__, self.id, self.nome, self.idade)
    
    @classmethod
    def all(cls):
        return cls.objects