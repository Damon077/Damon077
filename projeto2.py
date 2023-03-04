# Projeto - Chute o número

''''
1 - Quais são os dados de e entrada necessários?
Valor aleatório de 1 a 10
2 - O que devo fazer com estes dados?
Eu devo comparar o chute do usuário com o valor aleatório que foi gerado e dizer se o chute foi maior, menor ou igual ao valor que foi gerado no início do progama
3 - Quais são as restrições deste problema?
O valor deve ser entre 1 a 10
4 - Qual o resultado esperado?
O programa deverá informar se o chute foi acima, abaixo, ou igual ao valor aleatório no início do programa.
5 - Qual a sequência de passos a serem feitos para chegar ao resultado esperado?
input chute
if chute > valor_aleatorio:
  print "chute foi maior que o valor gerado"
if chute < valor_aleatorio:
  print "chute foi menor que o valor gerado"
else
  print "chute foi igual a valor aleatório
 
'''
import random

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input('Chute um valor de 1 a 10'))
    if chute > valor_aleatorio:
        print('Chute foi maior que o valor gerado')
    elif chute < valor_aleatorio:
        print('Chute foi menor que o valor gerado')
    elif chute == valor_aleatorio:
        acertou = True
        print('Você acertou!')