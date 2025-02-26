course_name = "Python Programming"

print(len(course_name)) # len() contagem de caracteres da string
print(course_name[0]) # [] acessa o caractere na opção 0, que retorna P
print(course_name[-1]) # [] acessa a ultima letra da string
print(course_name[0:3]) # [ : ] acessa o intervalo de caracter -- retorna 'pyt'
print(course_name[3:])  # [ : ] acessa o terciero caracter e vai até o ultimo -- retorna 'hon Programming'


#Caracteres de escape
course_name = "Python \"Programming\"" # \"\"coloca aspas duplas na palavra desejada


#Concatenacao 
first = "Gabriel"
last = "Sales"
full_name = f"{first} {last}" #concatenação de string

print(full_name)


#Metodos para String
course = "Python Programming"

print(course.upper()) #coloca  a string com todas as letra maiusculas
print(course.lower()) #coloca  a string com todas as letras minusculas
print(course.title()) # a primeira letras de cada palavra ficam maiusculas
print(course.strip())# remove os espaços em branco de cada lado da string, caso tenha
print(course.lstrip())# remove os espaços em branco do lado esquerdo da string, caso tenha
print(course.rstrip())# remove os espaços em branco do lado direito da string, caso tenha
print(course.find("P")) #retorna o indice da letra desejada da  string -- vai retornar o 0
print(course.replace("Python", "Django")) #trocca a palavra python pela django
print(course.replace("P", "j")) #troca as letras P pela letra J
print("Pro" in course) # procura se a o trecho 'Pro" no nome do curso -- retorna true se tiver


