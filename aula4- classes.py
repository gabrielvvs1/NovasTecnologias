#CLASSE
class Person: 
    nome = ""
    idade = 0

    def get_info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

p = Person() #instanciando a classe pessoa
p.nome = 'Victor' #atribuindo valor ao atributo nome
p.idade = 19 #atribuindo valor ao atributo idade

p.get_info() #chama o metodo get_info



def __init__(self, nome, idade): # construtor
    self.nome = nome
    self.idade = idade


def display_info(self):
    print('f{self.nome} tem {self.idade} anos')


# def __str__(self): #metodo to string
#     return f'{self.nome} tem {self.idade} anos'


#HERANÇA
class Student(Person):#classe filha
    def __inti__(self, nome, idade, matricula):#add o atributo matricula dentro da classe student
        super().__init__(nome, idade) #pega os atributos da classe pai que eh a Person e coloca na student (classe filha)
        self.matricula = matricula
    def display_info(self):
        print(f'{self.nome} tem {self.idade} anos e sua matricula e {self.matricula}')

p = Person('Victor', 19)
p.display_info()

s = Student('Yasmin', 20, '123456')
s.display_info()




