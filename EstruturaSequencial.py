# ------------------------------------------------------- Estrutura Sequencial: # -------------------------------------------------------

# 1.1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.
'''
    print("Alo mundo")

'''

# 1.2 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
'''
    userinput = input("Informe um número: ")
    print("O número informado foi: {0}".format(userinput))

'''

# 1.3 - Faça um Programa que peça dois números e imprima a soma.
'''
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

soma = num1 + num2
print("A soma entre {0} e {1} é: {2}".format(num1, num2, soma))

'''

# 1.4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''

bim1 = float(input("Digite a nota do primeiro bimestre: "))
bim2 = float(input("Digite a nota do segundo bimestre: "))
bim3 = float(input("Digite a nota do terceiro bimestre: "))
bim4 = float(input("Digite a nota do quarto bimestre: "))

media = (bim1 + bim2 + bim3 + bim4) / 4

print("Sua média é: {:.2f}".format(media))

'''

# 1.5 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit

'''

userinput = int(input("Digite o valor em metros: "))

convert = userinput * 100

print("O valor {0} em metros é de: {1}".format(userinput, convert))

'''

# 1.6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

'''

pi = 3.14
raio = float(input("Digite o raio do círculo: "))
area = pi * (raio * raio)

print("O raio do circulo é de: {0:.3f} metros²".format(area))

'''

# 1.7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

'''

base = int(input("Digite o valor da base do quadrado em centimetros: "))
altura = int(input("Digite o valor da altura do quadrado em centimetros: "))

area = base * altura
dobroArea = area * 2

print("O dobro da area medindo {0}cm² é de: {1}cm²".format(area, dobroArea))

'''

# 1.8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

'''

SpH = float(input("Informe o valor que recebe por hora: ")) # 5 reais
horasTrabalhadas = int(input("Informe por quantas horas por mês você trabalha: ")) # 10 horas X 30 dias do mês = 300 horas total
# Trabalho 10 horas por 30 dias no mês.
# 300 horas no total
#

salariototal = (SpH * 300)

print("O total do seu salário no mês referido é de: R${:.2f}".format(salariototal))

'''

# 1.9 - Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius (C = 5 * ((F-32) / 9)).

'''

fah = int(input("Digite a temperatura em Fahrenheit: "))

celcius = 5 * (fah - 32) / 9

print("{0}°F em Celcius ficará: {1:.1f}°C".format(fah, celcius))

'''

# 1.10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

'''

celcius = int(input("Digite a temperatura em graus Celcius: "))

fah = (celcius / 5) * 9 + 32

print("{0}°C em graus Fahrenheit ficará: {1:.0f}".format(celcius, fah))

'''

# 1.11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# O produto do dobro do primeiro com metade do segundo.
# A soma do triplo do primeiro com o terceiro.
# O terceiro elevado ao cubo.

'''

num1int = int(input("Digite o primeiro valor: "))
num2int = int(input("Digite o segundo valor: "))
num3float = float(input("Digite o terceiro valor: "))

first = (num1int * num1int) + (num2int / 2)

second = (num1int * 3) + num3float

third = num3float * 3

print("O produto do dobro de {0} com metade de {1} é de: {2}".format(num1int, num2int, first))
print("A soma do triplo de {0} + {1} é de: {2}".format(num1int, num3float, second))
print("{0}³ é igual a: {1}".format(num3float, third))

'''

# 1.12 - Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

'''

altura = float(input("Digite a sua altura: "))

pesoideal = (72.7 * altura) - 58

print("O peso ideal para a sua altura é de: {0:.0f}kg".format(pesoideal))

'''

# 1.13 - Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

'''

sexo = input("Informe o seu sexo: ")
altura = float(input("Informe a sua altura: "))

if sexo == 'masculino' or 'm':
    peso = (72.7 * altura) - 58
elif sexo == 'feminino' or 'f':
    peso = (62.1 * altura) - 44.7
else:
    print("Gênero não encontrado.")

print("O seu peso ideal é de: {0:.0f}kg".format(peso))

'''

# 1.14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa
# que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.


'''
peso_peixe = float(input("Qual é o peso do peixe? "))

if peso_peixe > 50:

   print("O peso do peixe está acima do permitido você sofrera um multa de",(peso_peixe - 50)*4 , "R$")

else:

   print("O peixe está em peso permitido.")
'''


# 1.15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# 1 - Salário bruto
# 2 - Quanto pagou ao INSS.
# 3 - Quanto pagou ao sindicato
# 4 - O salário liquido

'''

SpH = float(input("Informe o valor que recebe por hora: "))  # 5 reais
horasTrabalhadas = int(input("Informe por quantas horas por dia você trabalha: "))
# valor por hora * por quantas horas trabalha * 30 dias no mes

salariobruto = (SpH * horasTrabalhadas) * 30
impostorenda = (salariobruto * 11) / 100
INSS = (salariobruto * 8) / 100
sindicato = (salariobruto * 5) / 100
salarioliq = (salariobruto - impostorenda - INSS - sindicato)

print("\nSalário bruto: " + Fore.GREEN + "R${:.2f}".format(salariobruto))
print(Fore.RESET + "- 11% de imposto de renda: " + Fore.GREEN + "R${0:.2f}".format(impostorenda))
print(Fore.RESET + "- 8% INSS: " + Fore.GREEN + "R${0:.2f}".format(INSS))
print(Fore.RESET + "- 5% sindicato: " + Fore.GREEN + "R${0:.2f}".format(sindicato))
print(Fore.RESET + "Salário liquido: " + Fore.GREEN + "R${0:.2f}".format(salarioliq))

'''

# 1.16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

'''

tamanho = int(input('Tamanho em metros quadrados: '))
litros = tamanho / 3

if tamanho % 54 == 0:
	latas = tamanho / 54
else: 
	latas = int(tamanho / 54) + 1

preco = latas * 80
print ('%d latas' %latas)
print ('R$ %.2f' %preco)

'''


# 1.17 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

'''

filesize = int(input("Informe o tamanho do arquivo: "))
speed = int(input("Informe a velcocidade da internet: "))

speedtime = filesize / (speed / 8)  # Um arquivo de 15 MB (FILESIZE) baixado a 10 Mb/s (SPEED): 15 / (10/8) = 12 segundos, ou:
                                    # speedtime = filesize / (speed / 8)

print("A velocidade de download será de aproximadamente: {0:.0f} segundos".format(speedtime))

'''
