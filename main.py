# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 23:03:51 2021

@author: Ramon Silva
"""

from clientePassageiro import client
from bully import bully
import numpy as np


def menu():
    opcao = 0
    portPriority = [43000,42000,41000]
    serverPriotity = 43000
    while(opcao != '2'):
        print('''
                MENU:
    
                [1] - Comprar Passagem
                [2] - Sair
            ''')
        opcao = str(input('Escolha uma opção: '))
        serverPriotity = servico(opcao, portPriority, serverPriotity)
        
def servico(i,portPriority,server):
    if(i == "1"):
        quantidade = "00"
        serverElected = portPriority
        destino = str(input('Destino do passagem: '))
        
        while len(quantidade) > 1:
            quantidade = str(input('Quantidade de passagens (até 9): '))
            
            if len(quantidade) > 1: 
                print("Quantidade de passagens não permitida!! \n")
                
        
        message = destino+','+quantidade
        
        serverAlive = bully.getAlive(server)
        
        if not serverAlive:
            serverElected = bully.election(serverElected)
            
            #Ordena servers a partir da eleição
            serverElected = np.array(serverElected)
            serverElected = selection_sort(serverElected)
            server = serverElected[0]    
            
        #Verifica a existencia de algum server, caso não tenha server ele retorna messagem de error
        if server > 0:
            s = client(server)
            s.send(message)
            
        else:
            print("\nTodos servidores estão desconectados!!")
        
        
        return server
        
    if (i == "2"):
        print ('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print ('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print ('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAté outro dia!\n\n')
        
        return server

def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmax(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x

if __name__ == "__main__":
    menu()