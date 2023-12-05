'''Descrição

Vamos utilizar a função notification.notify() para criar uma função de alerta de falha de carregamento de base de dados 

Aspectos a incluir

O código a seguir gera uma janela de alerta:

#!pip install plyer 
from plyer import notification 
notification.notify(
     title='Título da notificação',
     message='Mensagem da notificação',
     app_name='Nome do aplicativo',
     timeout=10 )

     
A função precisa ter essa definição:

def alerta(nivel, base, etapa):

Sendo:
Ao chamar a função deverá gerar uma janela de alerta;
Exibir a mensagem “Falha no carregamento da base {base} na etapa {etapa}”;
Exibir a data atual;
O título “Alerta Baixo” quando nivel = 1, “Alerta Médio” quando nivel = 2 e "Alerta Alto” quando nivel = 3.
}

'''

#!pip install plyer 
from plyer import notification
from datetime import datetime

def alerta(nivel, base, etapa):
    if nivel == 1:
        titulo = 'Alerta Baixo'
    elif nivel == 2:
        titulo = 'Alerta Médio'
    elif nivel == 3:
        titulo = 'Alerta Alto'
    else:
        titulo = 'Inválido'
        

    notification.notify(
        title = titulo,
        message = f'Falha no carregamento \n da base {base} \n na etapa {etapa}\n {datetime.now()}',
        app_name = 'Windows',
        timeout = 20
    )

#Preencher para chamar a função
nivel = 3 #adicionar o nivel do alerta
base = 'CANCELAMENTOS'
etapa = 'ATUALIZAÇÃO'

alerta(nivel=nivel, base=base, etapa=etapa)
