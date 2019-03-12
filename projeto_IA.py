import csv
from math import sqrt


#Recebe uma string e carrega o arquivo com este nome
def carregar_arquivo(nome_do_arquivo):
    return open(nome_do_arquivo, 'r').readlines()

#Gera uma lista com sublistas que representam uma posição em um plano cartesiano
def treinamento(dados):
    plano = []
    for i in range(1,len(dados)):
        plano.append(dados[i].replace('\n', '').split(';'))
    return plano

#Metodo usado na ordenação com o sorted
def ordenar(t):
    return t[3]

#Recebe o plano com as posições das flores, e uma flor a ser classificada
#e calcula a distancia heuristica dessa nova flor ao resto das flores
def calcula_distancia(dados, entrada):
    for i in range(len(dados)):
        #print(dados[i])
        dados[i].append(sqrt(((float(dados[i][0]) - float(entrada[0]))**2)+((float(dados[i][1]) - float(entrada[1]))**2)))

#Recebe um lista com as 3 flores mais proximas e retorna a que mais se repetiu
def achar_classe(kprimeiros):
    tipos = [0,0,0,0,0]
    for i in range(len(kprimeiros)):
        tipos[0] = kprimeiros.count('PP')
        tipos[1] = kprimeiros.count('P')
        tipos[2] = kprimeiros.count('M')
        tipos[3] = kprimeiros.count('G')
        tipos[4] = kprimeiros.count('GG')
    return tipos.index(max(tipos))

#Escreve no arquivo.txt resultado o texto recebido
def escrever(texto):
    arquivo = open('resultado.txt', 'w')
    arquivo.write(texto)
    arquivo.close()
#O knn em si, resebe um teste e retorna qual o tipo que mais se repete entre os
#3 pontos mais proximos
def knn(teste,k):
    plano = treinamento(carregar_arquivo('treinamento.csv'))
    planotemp = plano
    calcula_distancia(planotemp, teste)
    planotemp = sorted(planotemp, key = ordenar)
    proximos = []
    for i in range(0,k):
        proximos.append(planotemp[i][2])
    #print(proximos)
    classe = achar_classe(proximos)
    return classe

#Carrega a lista de teste e a formata para ser usada no sistema
def gerar_testes():
    teste = carregar_arquivo('teste.csv')
    testef = []
    for i in range(1, len(teste)):
        testef.append(teste[i].replace('\n', '').split(';')) 
    return testef

def teste_precisao(testes, amostra_correta, k):
    dic = {0:'PP',1:'P',2:'M',3:'G',4:'GG'}
    cont = 0
    for i in testes:
        #print(i)
        i.append(dic[knn(i, k)])
    for e in range(len(amostra_correta)):
        #print(amostra_correta[e][2],'x',testes[e][2])
        if amostra_correta[e][2] == testes[e][2]:
            cont+=1
    return (cont/len(amostra_correta))*100

def dicionario():
    return {0:'PP',1:'P',2:'M',3:'G',4:'GG'}
#testes = gerar_testes()
#precisao = teste_precisao(testes, treinamento(carregar_arquivo('treinamento.csv')),3)
