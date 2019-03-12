from tkinter import*
from projeto_IA import*

def mostra():
    try:
        dic = dicionario()
        lbresultado['text'] = dic[knn([altura.get(),peso.get()], int(k.get()))]
        lbresultado_precisao['text'] = int(teste_precisao(gerar_testes(), treinamento(carregar_arquivo('treinamento.csv')),int(k.get()))),'%'
        lbaviso['text'] = ''
    except:
        lbaviso['text'] = 'Dados invalidos!'

janela = Tk()
janela.title('Medidas')
#janela['bg'] = 'White'

lbaltura = Label(janela, text='Digite sua altura')
lbaltura.place(x=10,y=5)

btsugerir = Button(janela, width=20, text = 'Sugerir Tamanho', command=mostra)
btsugerir.place(x=345, y=120)

lbtamanho = Label(janela, text='Tamanho: ')
lbtamanho.place(x=300, y=60)

lbresultado = Label(janela, text='')
lbresultado.place(x=370, y=60)

altura = Entry(janela)
altura.place(x=10,y=25)

lbpeso = Label(janela, text='Digite seu peso: ')
lbpeso.place(x=10,y=50)

peso = Entry(janela)
peso.place(x=10,y=70)

lbk = Label(janela, text='Escolha um K (1 é o recomendado)')
lbk.place(x=10,y=90)

k = Entry(janela)
k.place(x=10, y=110)

lbprecisao = Label(janela, text='Precisão deste K:')
lbprecisao.place(x=300,y=40)

lbresultado_precisao = Label(janela, text='')
lbresultado_precisao.place(x=400, y=40)

lbaviso = Label(janela,text='')
lbaviso.place(x=200,y=25)

#larguraxaltura+distanciaesquerda+distanciatopo
janela.geometry('500x150+100+100')
janela.mainloop()
