def my_function():
    print("hello funcao")

my_function()#chama a funcao


#funcao com parametro
def my_function(param1, param2):
    print (param1 + param2)

my_function("Hello ", "world")


#funcao com parametro e retorno
def my_function(param1, param2):
    return (param1 + param2)

texto = my_function("Hello", "World!")
print(texto)


