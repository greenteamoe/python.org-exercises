# ------------------------------------------------------- Estrutura de Decisão: # -------------------------------------------------------

# 2.1 - Faça um Programa que peça dois números e imprima o maior deles.

'''

num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))

if num1 > num2:
    print("O número {0} é maior que o número {1}".format(num1, num2))
else:
    print("O número {0} é maior que o número {1}".format(num2, num1))

'''

# 2.2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

'''

num1 = int(input("Primeiro valor: "))

if num1 > 0:
    print("O valor {0} é positivo".format(num1))
else:
    print("O valor {0} é negativo".format(num1))

'''

# 2.3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

'''

genero = input("Informe o seu gênero: ")

if genero == 'm' or genero == 'M':
    print("Masculino")
elif genero == 'f' or genero == 'F':
    print("Feminino")
else:
    print("Gênero inválido.")

'''

# 2.4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

'''

vogal = ['A', 'E', 'I', 'O', 'U']
consoante = ['B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']



userinput = input("Digite uma letra: ")
userinput = userinput.upper()

if userinput in vogal:
    print("A letra {} é uma vogal.".format(userinput))
elif userinput in consoante:
    print("A letra {} é uma consoante.".format(userinput))
else:
    print("Caractére inválido.")

'''

# 2.5 - Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# 1 - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# 2 - A mensagem "Reprovado", se a média for menor do que sete;
# 3 - A mensagem "Aprovado com Distinção", se a média for igual a dez.

'''

bim1 = float(input("Informe a primeira nota: "))
bim2 = float(input("Informe a segunda nota: "))

media = (bim1 + bim2) / 2

if 7 <= media <= 9:
    print("Aprovado. {0}".format(media))
elif media == 10:
    print("Aprovado com Distinção. {0}".format(media))
else:
    print("Reprovado. {0}".format(media))

'''

# 2.6 - Faça um Programa que leia três números e mostre o maior deles.

'''

num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
num3 = int(input("Terceiro valor: "))

if num1 > num2 and num1 > num3:
    print("O primeiro valor, '{0}' é o maior.".format(num1))
elif num2 > num1 and num2 > num3:
    print("O segundo valor valor, '{0}' é o maior.".format(num2))
else:
    print("O terceiro valor, '{0}' é o maior.'".format(num3))

'''

# 2.7 - Faça um Programa que leia três números e mostre o maior e o menor deles.

'''

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

maior = n1
menor = n1

if maior < n2:
    maior = n2

if maior < n3:
    maior = n3

if menor > n2:
    menor = n2

if menor > n3:
    menor = n3

print('Maior:  {0} '.format(maior))
print('Menor:  {0} '.format(menor))

'''

# 2.8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

'''

precoProduto1 = float(input("Digite o preço do primeiro produto: "))
precoProduto2 = float(input("Digite o preço do segundo produto: "))
precoProduto3 = float(input("Digite o preço do terceiro produto: "))

if precoProduto1 < precoProduto2 and precoProduto1 < precoProduto3:
    print("\nVocê deve comprar o primeiro produto, valor: R${0:.2f}".format(precoProduto1))
if precoProduto2 < precoProduto3 and precoProduto2 < precoProduto1:
    print("\nVocê deve comprar o segundo produto, valor: R${0:.2f}".format(precoProduto2))
if precoProduto3 < precoProduto2 and precoProduto3 < precoProduto1:
    print("\nVocê deve comprar o terceiro produto, valor: R${0:.2f}".format(precoProduto3))

'''

# 2.9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

# 2.10 - Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
# ou "Valor Inválido!", conforme o caso.

'''

turno = input("Informe o turno: ")

if turno == 'M' or turno == 'matutino':
    turno.upper()
    print("Bom Dia!")
elif turno == 'V' or turno == 'vespertino':
    turno.upper()
    print("Boa tarde!")
elif turno == 'N' or turno == 'noturno':
    turno.upper()
    print("Boa noite!")
else:
    print("Valor inválido!")

'''

# 2.11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus
# colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# - salários até R$ 280,00 (incluindo) : aumento de 20%
# - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# - salários de R$ 1500,00 em diante : aumento de 5%
# Após o aumento ser realizado, informe na tela:
# - o salário antes do reajuste;
# - o percentual de aumento aplicado;
# - o valor do aumento;
# - o novo salário, após o aumento.

'''

salario = float(input("Informe o salário: "))

print("\nSalário antes do ajuste: R${0:.2f}".format(salario))

if salario <= 280:
    salario1 = (salario * 20) / 100
    print("Valor do aumento: R${0}".format(salario1))
    print("Novo salário, após o aumento: R${0:.2f}".format(salario1 + salario))
    print("Percentual de aumento aplicado: 20%")
elif 280 <= salario < 700:
    salario2 = (salario * 15) / 100
    print("Valor do aumento: R${0}".format(salario2))
    print("Novo salário, após o aumento: R${0:.2f}".format(salario2 + salario))
    print("Percentual de aumento aplicado: 15%")
elif 700 <= salario < 1500:
    salario3 = (salario * 10) / 100
    print("Valor do aumento: R${0}".format(salario3))
    print("Novo salário, após o aumento: R${0:.2f}".format(salario3 + salario))
    print("Percentual de aumento aplicado: 10%")
elif salario >= 1500:
    salario4 = (salario * 5) / 100
    print("Valor do aumento: R${0}".format(salario4))
    print("Novo salário, após o aumento: R${0:.2f}".format(salario4 + salario))
    print("Percentual de aumento aplicado: 5%")

'''

# 2.12 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.


# 2.13 - Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

'''

dia = 0

count = [1, 2, 3, 4, 5, 6, 7]

while dia != count:
    dia = int(input("Digite um dia da semana (1-7): "))

    if dia == 1:
        print("Domingo")
    elif dia == 2:
        print("Segunda")
    elif dia == 3:
        print("Terça")
    elif dia == 4:
        print("Quarta")
    elif dia == 5:
        print("Quinta")
    elif dia == 6:
        print("Sexta")
    elif dia == 7:
        print("Sábado")
    else:
        print("Valor inválido.")

'''

# 2.14 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento      Conceito
#  Entre 9.0 e 10.0                A
#  Entre 7.5 e 9.0                 B
#  Entre 6.0 e 7.5                 C
#  Entre 4.0 e 6.0                 D
#  Entre 4.0 e zero                E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
# se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

'''

bim1 = float(input("Nota do primeiro bimestre: "))
bim2 = float(input("Nota do segundo bimestre: "))

media = (bim1 + bim2) / 2

if media >= 9:
    print("Notas:\n Primeiro bimestre: {0}\n Segundo bimestre: {1}".format(bim1, bim2))
    print(" Média: {0}".format(media))
    print(" Conceito: 'A'")
    print(" APROVADO!")
elif 7.5 <= media < 9:
    print("Notas:\n Primeiro bimestre: {0}\n Segundo bimestre: {1}".format(bim1, bim2))
    print(" Média: {0}".format(media))
    print(" Conceito: 'B'")
    print(" APROVADO!")
elif 6 <= media < 7.5:
    print("Notas:\n Primeiro bimestre: {0}\n Segundo bimestre: {1}".format(bim1, bim2))
    print(" Média: {0}".format(media))
    print(" Conceito: 'C'")
    print(" APROVADO!")
elif 4 <= media < 6:
    print("Notas:\n Primeiro bimestre: {0}\n Segundo bimestre: {1}".format(bim1, bim2))
    print(" Média: {0}".format(media))
    print(" Conceito: 'D'")
    print(" Reprovado.")
elif media < 4:
    print("Notas:\n Primeiro bimestre: {0}\n Segundo bimestre: {1}".format(bim1, bim2))
    print(" Média: {0}".format(media))
    print(" Conceito: 'E'")
    print(" Reprovado.")

'''

# 2.15 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# - Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# - Triângulo Equilátero: três lados iguais;
# - Triângulo Isósceles: quaisquer dois lados iguais;
# - Triângulo Escaleno: três lados diferentes;

'''

lado1 = int(input("Informe o primeiro lado em centímetros: "))
lado2 = int(input("Informe o segundo lado em centímetros: "))
lado3 = int(input("Informe o terceiro lado em centímetros: "))

if lado1 + lado2 > lado3 or lado2 + lado3 or lado1 + lado3:
    if lado1 == lado2 and lado2 == lado3:
        print("Triângulo Equilátero: três lados iguais")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado1 or lado2 == lado3 or lado3 == lado1 or lado3 == lado2:
        print("Triângulo Isósceles: quaisquer dois lados iguais")
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("Triângulo Escaleno: três lados diferentes")
else:
    print("Não é possivel formar um triângulo.")

'''

# 2.16 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;


# 2.17 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

'''

ano = int(input("Informe um ano: "))

bis1 = (ano % 4)
bis2 = (ano % 100)
naobis1 = bis1
naobis2 = (ano % 400)

if bis1 == 0 and bis2 != 0:
    print("\nO ano de {0} é um ano bissexto.\nFevereiro contém 29 dias.".format(ano))
elif naobis1 != 0 and naobis2 != 0:
    print("\nO ano de {0} não é um ano bissexto.\nFevereiro contém 28 dias.".format(ano))

'''

# 2.18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

'''

dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))

if dia <= 31 and mes <= 12:
    print("\ndata válida.\n{0}/{1}/{2}".format(dia, mes, ano))
else:
    print("\ndata inválida.")

'''

# 2.19 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
# dezenas e unidades do mesmo, observando os termos no plural a colocação do "e", da vírgula entre outros.

'''

numero = int(input('Digite um numero inteiro positivo: '))

# Extraindo a unidade
unidade = numero % 10

# Eliminando a unidade de nosso número
numero = (numero - unidade) / 10

# Extraindo a dezena
dezena = numero % 10

# Eliminando a dezena do número original, fica a centena
numero = (numero - dezena) / 10
centena = numero

# Fazendo ser inteiros
dezena = int(dezena)
centena = int(centena)

print("{0} centena(s), {1} dezena(s) e {2} unidade(s)".format(centena, dezena, unidade))

'''

# 2.20 - Faça um Programa para leitura de três notas parciais de um aluno... "SAME AS 2.5"

'''

bim1 = float(input("Informe a primeira nota: "))
bim2 = float(input("Informe a segunda nota: "))

media = (bim1 + bim2) / 2

if 7 <= media <= 9:
    print("Aprovado. Média: {0}".format(media))
elif media == 10:
    print("Aprovado com Distinção. Média: {0}".format(media))
else:
    print("Reprovado. Média: {0}".format(media))

'''

# 2.21 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
# quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de
# 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.


# 2.22 - Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).

'''

num1 = int(input("Informe um número: "))

form = (num1 % 2)

if form == 1:
    print("Número ímpar.")
elif form == 0:
    print("Número par.")
else:
    print("valor inválido.")

'''

# 2.23 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.

'''

num = float(input('Numero original: '))

if num == round(num):
    print("Inteiro")
else:
    print("Decimal")
    print("Arredondado pra baixo: ", round(num - 0.5))
    print("Arredondado pra cima : ", round(num + 0.5))

'''

# 2.24 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

'''

num1 = float(input("Informe o primeiro valor: "))
num2 = float(input("Informe o segundo valor: "))

print("-=-" * 10)
print("\n1 - Par ou Impar\n2 - Positivou ou negativo\n3 - Inteiro ou decimal\n")
print("-=-" * 10)
choice = int(input("\nInforme a operação: "))


par1 = (num1 % 2)
par2 = (num2 % 2)
impar1 = (num1 % 2)
impar2 = (num2 % 2)

if choice == 1:
    if par1 == 0:
        print("o numero {0:.0f} é par".format(num1))
    elif impar1 != 0:
        print("o numero {0:.0f} é impar".format(num1))
if choice == 1:
    if par2 == 0:
        print("o numero {0:.0f} é par".format(num2))
    elif impar2 != 0:
        print("o numero {0:.0f} é impar".format(num2))

if choice == 2:
    if num1 > 0:
        print("{0:.0f} é um valor positivo.".format(num1))
    if num2 > 0:
        print("{0:.0f} é um valor positivo.".format(num2))
    if num1 < 0:
        print("{0:.0f} é um valor negativo.".format(num1))
    if num2 < 0:
        print("{0:.0f} é um valor negativo.".format(num2))

if choice == 3:
    if num1 == round(num1):
        print("{0:.0f} é um número inteiro.".format(num1))
    if num2 == round(num2):
        print("{0:.0f} é um número inteiro.".format(num2))
    if num1 != round(num1):
        print("{0} é um número decimal.".format(num1))
    if num2 != round(num2):
        print("{0} é um número decimal.".format(num2))

'''

# 2.25 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.

'''

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]
resposta = 0
for qual in perguntas:
    resposta += (input(qual) == "sim")

if resposta == 5:
    print("Assassino")
elif resposta >= 3:
    print("Cúmplice")
elif resposta == 2:
    print("Suspeito")
else:
    print("Inocente")

'''

# 2.26 Um posto está vendendo combustíveis com a seguinte tabela de descontos...

'''

clientecombustivel = input("Informe o tipo de combustível (A-álcool, G-gasolina): ")
clientequantidade = float(input("Informe a quantidade de combustível em litros: "))

gasolina = 2.50
alcool = 1.90
preco = (clientequantidade * alcool)

if clientecombustivel == 'A' or clientecombustivel == 'a':  # alcool - 1,90 por litro
    if clientequantidade <= 20:
        desconto = (preco * 3) / 100
        total = (preco - desconto)
    elif clientequantidade > 20:
        desconto = (preco * 5) / 100
        total = (preco - desconto)
elif clientecombustivel == 'G' or clientecombustivel == 'g':
    if clientequantidade <= 20:
        desconto = (preco * 4) / 100
        total = (preco - desconto)
    elif clientequantidade > 20:
        desconto = (preco * 6) / 100
        total = (preco - desconto)

print("\nDesconto total de: R${0:.2f}\nPreço total: R${1:.2f}".format(desconto, total))

'''

# 2.27 - Uma fruteira está vendendo frutas com a seguinte tabela de preços...

'''

qtmorango = int(input("Informe a quantidade de morangos: "))
qtmaca = int(input("Informe a quantidade de maçãs: "))

morango = 2.50
maca = 1.80
preco1 = (morango * qtmorango)
preco2 = (maca * qtmaca)
total = (preco1 + preco2)

if qtmorango + qtmaca <= 5:
    if qtmorango + qtmaca > 8 or preco1 + preco2 > 25.00:
        desconto = (total * 10) / 100
        total = (preco1 + preco2) - desconto
elif qtmorango + qtmaca > 5:
    morango = 2.20
    maca = 1.50
    if qtmorango + qtmaca > 8 or preco1 + preco2 > 25.00:
        desconto = (total * 10) / 100
        total = (preco1 + preco2) - desconto

print("\nTotal a ser pago: {0:.2f}".format(total))

'''

# 2.28 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira...