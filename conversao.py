#Criado por Ivrna Maria Costa Soares - 2024

import os #biblioteca para limpeza do CMD

#PROGRAMA PARA CONVERSAO

def leitura_numero():
    #leitura do numero que sera convertido
    numero = input("Digite o numero a ser convertido: ")
    return numero

def leitura_base_numero():
    #leitura da base do numero que sera convertido
    base_numero = int(input("Digite a base (de 1 a 40) do numero digitado: "))
    return base_numero
    
def leitura_base_conversao():
    #leitura da base que o numero sera convertido
    base_conversao = int(input("Digite a base (de 1 a 40) que deseja converter: "))
    return base_conversao

#verificacao dos caracteres, se eles estao dentro das 40 bases
def verifica_num(n, caracter):
    tam = len(n)
    for i in range(tam):
        if (str(n[i]) not in caracter):
            return False
    return True

#Verifica se a base digitada esta entre 1 e 40
def verifica_base(n):
    if n >= 2 and n <= 40:
        return True
    else:
        return False

#converter os digitos de 0 a 9 de string para inteiros
def conversao_inteiro(n, caracter):
    tam = len(n)
    convertido = []
    for i in range(tam):
        #a funcao isdigit() verifica se aquele caracter e um digito
        if str(n[i]).isdigit():
            #adiciona no novo vetor na posicao i o valor de [i] no tipo inteiro
            #a funcao .append serve para adiconar um elemento na lista
            convertido.append(int(n[i]))
        else: 
            #.index procura a posicao no vetor
            convertido.append(caracter.index(str(n[i])))
    return convertido

#converter o numero decimal para a base desejada
def conversao_decimal(n, base_n):
    tam = len(n)
    resultado = 0
    for i in range(tam):
        resultado += n[i] * (base_n ** (tam - 1 - i))
    return resultado
    
#funcao para converter o numero decimal na base pedida
def conversao_final(n, base_con):
    resultado = []
    #divisao para a conversao
    while n > 0:
        resultado.append(int(n % base_con))
        n = n // base_con
    
    #mudando/revertendo as posicoes
    resultado.reverse()
    return resultado


#converte os valores finais inteiros maiores que 9 para caracteres
def conversao_caracter(n, caracter):
    tam = len(n)
    convertido = []
    for i in range(tam):
        #adiciona no novo vetor na posicao i o valor de n[i] no tipo string
        #a funcao .append serve para adiconar um elemento na lista
        convertido.append(caracter[n[i]])
    return convertido

#limpeza do CMD
def limpeza():
    sistem = os.name
    #caso o SO seja windows
    if sistem == "nt": 
        os.system("cls")
    else: #caso seja outro SO
        os.system("clear")

#main

#vetor dos caracter 
caracter = [str(i) for i in range(10)] + [chr(i) for i in range(65, 91)] + ['!', '@', '#', '$']

# Chama a funcao para leitura do numero e verifica se esta dentro das 40 bases disponiveis
while True:
    numero = leitura_numero()
    base_numero = leitura_base_numero()
    base_conversao = leitura_base_conversao()
    
    if verifica_num(numero, caracter) is True and verifica_base(base_numero) is True and verifica_base(base_conversao) is True:
        #com tudo verificado corretamente, saira do loop
        break
    else:
        #limpeza do CMD
        limpeza()
        #retornara uma mensagem diferente para cada tipo de erro
        if verifica_num(numero, caracter) is False:
            print("Os digitos nao condiz com a sequencia para caracteres 0-9, A-Z, !, @, #, $, por favor tente novamente:")
        elif verifica_base(base_numero) is False:
            print("A base do numero digitada nao condiz com a que disponibilizamos, digite uma base de 2 a 40 positivo, por favor tente novamente:")
        else:
            print("A base para conversao digitada nao condiz com a que disponibilizamos, digite uma base de 2 a 40 positivo, por favor tente novamente:")

#recebe a conversao dos digitos em string para inteiro
num_inteiro = conversao_inteiro(numero, caracter)
#recebe a conversao dos numeros inteiros para decimal
num_decimal = conversao_decimal(num_inteiro, base_numero) 
#recebe a conversao do decimal para a base pedida
resul_preliminar = conversao_final(num_decimal, base_conversao)
#faz a convbersoa dos inteiros para caracteres
resul_final = conversao_caracter(resul_preliminar, caracter)

#limpeza do CMD
limpeza()
#prints de todas as informacoes necessarias para saida
print("O numero para conversao: ", numero)
print("A base do numero digitado: ", base_numero)
print("A base a ser convertida: ", base_conversao)
print("Caractres localizados e convertidos para decimal: ", num_decimal)
#.join faz com que o resultado seja mostrado como string e nao como vetor
print("Numero", numero,"convertido da base", base_numero, "para base", base_conversao, ": ", "".join(resul_final))



"""
Referencias utilizadas
1. https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
2. http://devfuria.com.br/python/listas/#:~:text=index(),o%20index%20de%20determinado%20elemento.&text=Se%20voc%C3%AA%20procurar%20por%20um,existe%20um%20erro%20ser%C3%A1%20lan%C3%A7ado.&text=Por%20tanto%2C%20se%20o%20seu,de%20teste%20de%20inlclus%C3%A3o%20in%20.
3. https://www.ic.unicamp.br/~wainer/cursos/1s2020/102/aula09.html
"""