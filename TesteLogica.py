#1- Dada as idades I, J, K, X, Y. Faça um algoritmo para calcular a média das idades.

i = int(input("Digite a idade 01: "))
j = int(input("Digite a idade 02: "))
k = int(input("Digite a idade 03: "))
x = int(input("Digite a idade 04: "))
y = int(input("Digite a idade 05: "))

resultado = (i+j+k+x+y)/5 

print("A média das idades é: ",resultado)

#########################################################################################################################

#2- Dada a distância A e o combustível gasto B, faça um algoritmo para calcular o consumo médio.

distancia = float(input("Digite a distancia percorrida em KM (Ex.: 600.00): "))
combustivel = float(input("Digite o combustivel gasto em litros (Ex.: 40.00): "))

cosumoMedio = distancia/combustivel

print('O consumo médio foi: ',cosumoMedio,"Km/l.")

#########################################################################################################################

#3 - Dados três números (a, b, c), faça um algoritmo para mostrar o menor número.

print("Qual é o menor número digitado!!!")
print("")
a = float(input("Digite um numero 01: "))
b = float(input("Digite um numero 02: "))
c = float(input("Digite um numero 03: "))

if a<b and a<c:
    menor = a 
if b<a and b<a:
    menor = b
if c<a and c<b:
    menor = c

print('O menor número digitado foi {}'.format(menor))

#########################################################################################################################

#4- Faça um algoritmo que converta a temperatura de C para F.

print("Conversor de Celsius para Fahrenheit")
print("")

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = ((9*celsius) / 5) + 32

print('A temperatura {}ºC para Fahrenheit é: {}ºF'.format(celsius, fahrenheit))

#########################################################################################################################

#5 - Faça um algoritmo para apresentar se dois números são múltiplos.

print("Teste de números multiplos")
print("")

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))

if (num1>num2) and (num1 % num2 == 0):
    print('Os numeros {} e {} são multiplos'.format(num1, num2))
else:
    print('Os numeros {} e {} não são multiplos'.format(num1, num2))

#########################################################################################################################

#6 - Uma partida de futebol iniciou na hora A e terminou na hora B. Faça um algoritmo que calcule o tempo que durou a partida.

print("Calcule o tempo da partida de futebol")
print("")

from datetime import datetime
horaInicial = (input('Digite a Hora incial da Partida (HH:MM:SS)'))
horaFinal = (input('Digite a Hora Final da Partida (HH:MM:SS)'))

FMT = '%H:%M:%S'

duracao = datetime.strptime(horaFinal, FMT) - datetime.strptime(horaInicial, FMT)

print('A duração do jogo foi de {} hora(s)'.format(duracao))

#########################################################################################################################

#7 - Dada uma lista de números A[1,2,3,…], faça um algoritmo que retorne uma lista somente com os números pares.

print("Apresentação dos números pares de uma lista de 5 números")
print("")

listaPar = []
contador = 0
while contador < 5:
    num1 = float(input("Digite um número: "))
    if num1 % 2 == 0:
        listaPar.append(num1)
    contador = contador + 1

print('O(s) número(s) par(es) da lista: {}'.format(listaPar))

#########################################################################################################################

#8 - Faça um algoritmo que receba um número e retorne se o número é primo ou não

print("Teste do Número Primo")
print("")

numero = int(input("Digite um número: "))
contador = 0
for i in range(1, numero + 1):
    if numero % i ==0:
        contador += 1

if contador ==2:
    print('o número {} é primo'.format(numero))
else:
    print('o número {} não é primo'.format(numero))

#########################################################################################################################

# 9 - Faça um algoritmo que receba um número e retorne a tabuada desse número.

print("Tabuada")
print("")

numero = int(input("Digite um número: "))

for i in range(0,11):
    print('{} x {} = {}'.format(numero, i, numero*i))

#########################################################################################################################

# 10 - Faça um algoritmo que receba um número e retorne o Fatorial desse número.

print("Fatorial do número")
print("")

numero = int(input("Digite um número: "))

contador = numero
fatorial = 1

while contador > 0:
    fatorial *= contador
    contador -= 1

print('O Fatorial do número {} é {}.'.format(numero, fatorial))

#########################################################################################################################

# 11 - Dada duas lista de números A[1,2,3,4] e B[1,2,5,8], faça um algoritmo que retorne a intersecção das listas.

print("Intersecção das Listas A e B")
print("")

listaA = [1,2,3,4]
listaB = [1,2,5,8]
listaC = []

for i in listaA:
    for j in listaB:
        if i == j:
            listaC.append(i)
print('A intersecção das listas dadas A ({}) e B ({}) é: {}.'.format(listaA, listaB, listaC))

#########################################################################################################################

# 12 - Dada duas lista de números A[1,2,3,4] e B[1,2,5,8], faça um algoritmo que retorne a concatenação das listas.

print("Concatenação das Listas A e B")
print("")

listaA = [1,2,3,4]
listaB = [1,2,5,8]
listaC = []

for item in listaA:
    listaC.append(item)

for item in listaB:
    if item not in listaC:
        listaC.append(item)
            
print('A concatenação das listas dadas A ({}) e B ({}) é: {}.'.format(listaA, listaB, listaC))

#########################################################################################################################

# 13 - Faça um algoritmo que receba uma matriz[i,z] como parâmetro e imprima todos os valores dessa matriz.


print("Imprimir os valores de uma Matriz")
print("")

matriz = [[0,0]]

for linha in range(0,1):
    for coluna in range(0,2):
        matriz[linha][coluna] = int(input('Digite um valor da linha {} e Coluna {}:'. format(linha, coluna)))

print('Os valores da Matriz é : {}'.format(matriz))

#########################################################################################################################

#14 - Faça um algoritmo que recebe uma palavra e retorne se a palavra é palíndromo. 
#(Palavra que se pode ler, indiferentemente, da esquerda para direita ou vice-versa. Ex: osso, 
#Ana e etc).



print("Verificação Palíndromo")
print("")

palavra = str(input('Escreva uma palavra: ')).strip().upper()
palavraInverso = palavra[::-1]

if palavra == palavraInverso:
    print('A palavra {} é um palíndromo'.format(palavra))
else:
    print('A palavra {} não é um palíndromo'.format(palavra))
