numero=int(input("digite un numero entero: "))

resultado=numero%3
print(f'el residuo es : {resultado}')

#condicional simple en python 
if(resultado==0):
    print("es multiplo de 3")
else:
    print("no es multiplo de 3")
print("fin del programa")