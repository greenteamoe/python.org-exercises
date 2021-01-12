# ------------------------------------------------------- Estrutura de Repetição: -------------------------------------------------------

# 3.1 - Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

'''
nota = float(input("informe um numero de 0 a 10: "))

while (nota > 10) or (nota < 0):
    nota = float(input("informe um numero de 0 a 10: "))

'''

# 3.2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

'''

user = input("Usuário: ")
pw = input("Senha: ")

while user == pw:
    print("Erro\n")
    user = input("Usuário: ")
    pw = input("Senha: ")
else:
    print("Registered")

'''

# 3.3 - Faça um programa que leia e valide as seguintes informações...

'''

nome = ''
idade = 0
salario = 0
sexo = ''
estado_civil = ''

while len(nome) <= 3:
    nome = input('Nome: (com mais de 3 letras) ')

while idade < 0 or idade > 150:
    idade = input('Idade:(entre 0 e 150) ')

while salario <= 0:
    salario = int(input('Salário: (maior que 0) '))

while sexo != 'f' and sexo != 'm':
    sexo = input('Sexo: [m/f]')

while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    estado_civil = input('Estado Civil: [s/c/v/d]')
    
'''

# 3.4 - Supondo que a população de um país A seja da ordem ...








# 3.5 - Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.






# 3.6 - Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro.

'''

#vertical
for i in range(1, 21):
    print(i)
#horizontal
for i in range(1, 21):
    print(i, end=' ')

'''



# 3.7 - Faça um programa que leia 5 números e informe a soma e a média dos números.

'''

n1 = float(input("n1: "))
n2 = float(input("n2: "))
n3 = float(input("n3: "))
n4 = float(input("n4: "))
n5 = float(input("n5: "))

soma = n1 + n2 + n3 + n4 + n5
media = (soma / 5)

print("\nsoma: {0}\nmedia: {1}".format(soma, media))

'''

# 3.8 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

'''

for x in range(1, 51, 2):
    print(x)

'''

# 3.9 - Desenvolva um gerador de tabuada...

'''

tabuada = int(input("Tabuada do numero: "))

for count in range(10):
    print("%d x %d = %d" % (tabuada, count + 1, tabuada * (count + 1)))

'''

# 3.10 - Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.

'''
print("base ^ expoente:")
base = int(input("valor da base: "))
expo = int(input("valor do expoente: "))

potencia = 1
x = 0

while x < expo:
    potencia = potencia * base
    x = x + 1
print("o valor de {0} elevado a {1} é: {2}".format(base, expo, potencia))

# or simply potencia = (base ** expo)

'''

# 3.11 - Faça um programa que peça 10 números inteiros,
# calcule e mostre a quantidade de números pares e a quantidade de números impares.

# 1st method:

'''

n1 = int(input("\nDigite o número: "))
n2 = int(input("Digite o número: "))
n3 = int(input("Digite o número: "))
n4 = int(input("Digite o número: "))
n5 = int(input("Digite o número: "))
n6 = int(input("Digite o número: "))
n7 = int(input("Digite o número: "))
n8 = int(input("Digite o número: "))
n9 = int(input("Digite o número: "))
n10 = int(input("Digite o número: "))
list1 = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

par = 0
impar = 0

for value in list1:
    if value % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print("Par: ", par, "\nImpar: ", impar)

#2nd method:

n = 1
P = 0
I = 0
while n <= 10:
    a = int(input())
    n = n + 1
    if a % 2 == 0:
        P = P + 1
    else:
        I = I + 1

print("A qtd de números pares é: ", P)
print("A qtd de números ímpares é: ", P) 

'''

# 3.12 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo.

'''

quantos = int(input("Quantos fibonacci vai querer? "))
anterior = 0
seguinte = 1
fibo = []
for i in range(quantos):
    fibo.append( anterior )
    anterior , seguinte  = seguinte, anterior + seguinte

print(fibo)

'''

# 3.13 - A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa que gere a série até que o valor seja maior que 500.


# 3.14 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120


# 3.15 - Faça um programa que, dado um conjunto de N números, 
# determine o menor valor, o maior valor e a soma dos valores.

'''

lista = []
count = 0

quant = int(input("Digite a quantiade de número que deseja digitar: "))
while quant != count:
    numero = lista.append(float(input("Digite um número: ")))
    count += 1

print("Lista: ", lista, "\nMaior: ", max(lista), "\nMenor: ", min(lista))
print("Soma: ", max(lista) + min(lista))

'''

# 3.16 - Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

'''

lista = []
count = 0

quant = int(input("Digite a quantiade de números que deseja digitar: "))
while quant != count:
    numero = int(input("Digite um número: "))

    while numero > 1000 or numero < 0:
        numero = int(input("Digite um número[erro]: "))
        
    lista.append(numero)
    count += 1

print("Lista: ", lista, "\nMaior: ", max(lista), "\nMenor: ", min(lista))
print("Soma: ", max(lista) + min(lista))

'''

# 3.17 - Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes 
# e limitando o fatorial a números inteiros positivos e menores que 16.


# 3.18 - Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
#  Um número primo é aquele que é divisível somente por ele mesmo e por 1.


# 3.19 - Altere o programa de cálculo dos números primos, 
# informando, caso o número não seja primo, por quais número ele é divisível.


# 3.20 - Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
#  O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.


# 3.21 - Faça um programa que calcule o mostre a média aritmética de N notas.


# 3.22 - Faça um programa que peça para n pessoas a sua idade,
#  ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
#  e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.


# 3.23 - Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.


# 3.24 - Faça um programa que calcule o número médio de alunos por turma. 
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
# As turmas não podem ter mais de 40 alunos.


# 3.25 - Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
# e o valor médio gasto em cada um deles. 
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.


# 3.26 - ...
