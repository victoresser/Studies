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
    
class RomanNumeralConverter:
    def __init__(self):
        self.numeral_map = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]

    def convert(self, num):
        roman_numeral = ""
        while num > 0:
            for numeral, value in self.numeral_map:
                while num >= value:
                    roman_numeral += numeral
                    num -= value
        return roman_numeral