# Sua solução aqui
a = int(input("Digite o valor de a: "))
b = int ( input("Digite o valor de b: "))
c = int (input ("Digite o valor de c: "))

#Verificar se forma um triângulo e qual tipo de triângulo

if a < (b+c) and b < (a+c) and c < (a+b):
    if a == b and b == c :
        print("equilátero")
    elif a == b or b == c or a == c :
        print("isósceles")
    else :
        print ("escaleno")

else : 
    print("Não forma triângulo")