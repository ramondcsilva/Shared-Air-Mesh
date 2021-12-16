# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 23:03:51 2021

@author: Ramon Silva
"""

import socket

class bully():
    def getAlive(*port):
        #server_port = port[0]
        input_s = str(port[0]).encode('utf8')
        
        # Create a TCP/IP socket 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect the socket to the server 
        server_address = ('localhost', port[0])
        print ("\nConectando ao endereco %s:%s" % server_address) 
        try:    
            sock.connect(server_address)
            
        
            #sent_time = time() # time immediately before sending
            sock.sendall(input_s)
            sock.recv(2048)
            #recv_time = time() # time after received response
            sock.close()
            print("Alive!")
            #elapsed_time = recv_time - sent_time
            #print('[CLIENT] Response from server {}, is: "{}"'.format(server_address, test.decode('utf8')))
            #print("elapsed time =", elapsed_time , 'seconds')
            
        except Exception as e:         
            #e = "Nenhuma conexão pôde ser feita porque a máquina de destino está desconectada!"
            e = "Not Alive!"
            print ("%s" %str(e))
            
            return False
            
        except socket.error as e: 
            print ("Socket error: %s" %str(e))
            
        
        return True
            
    def election(port):
        idt = []
        rows = len(port)
        
        for i in range(rows):
            idt.append(bully.getInd(port[i]))
            #print(idt)
        
        return idt
            
    def getInd(porta):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect the socket to the server 
        server_address = ('localhost', porta)
        print ("\nConectando ao endereco %s:%s" % server_address) 
        try:    
            sock.connect(server_address)
            
            
            #sent_time = time() # time immediately before sending
            sock.sendall(str(porta).encode('utf8'))
            idServer = sock.recv(2048)
            #recv_time = time() # time after received response
            sock.close()
            
            #elapsed_time = recv_time - sent_time
            print('[CLIENT] Response from server {}, is: "{}"'.format(server_address, idServer.decode('utf8')))
            #print("elapsed time =", elapsed_time , 'seconds')
            
        except Exception as e:         
            e = "Nenhuma conexão pôde ser feita porque a máquina de destino está desconectada!"
            print ("%s" %str(e))
            
            return 0
            
        except socket.error as e: 
            print ("Socket error: %s" %str(e))
            
        
        return int(idServer.decode('utf8'))