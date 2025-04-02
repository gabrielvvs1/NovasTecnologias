class Person:
    def __init__(self, name, age):
        self.nome = name
        self.age = age

    def pegar_nome(self):
        return self.nome
    
    def pegar_idade(self):
        return self.age
    
    def full_info(self):
        return f"{self.nome} tem {self.age} anos de idade."