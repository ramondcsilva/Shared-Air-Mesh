# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 23:03:51 2021

@author: Ramon Silva
"""

import socket, time

#18.188.134.59
class client:
    def __init__(self,port):
        # Create a TCP/IP socket 
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect the socket to the server 
        server_address = ('localhost', port) 
        print ("\nConectando ao endereco %s:%s" % server_address) 
        self.sock.connect(server_address)
    
    def send(self,message):
        # Send data 
        try: 
            while True:
                # Send data 
                # Local de viajem / Valor / Quantidade
                self.sock.sendall(message.encode('utf-8'))
                message = self.sock.recv(2048) 
                print(message.decode('utf-8'))
                time.sleep(0.2)
                self.disconnect()
                
        except socket.error as e: 
            print ("Socket error: %s" %str(e)) 
            
        except Exception as e:         
            #print ("Other exception: %s" %str(e))
            str(e)
        finally: 
            self.sock.close() 
            print ("Fechando a conexao com o server...")
        
    def disconnect(socket):
         socket.close() 
         print ("Fechando a conexao com o server...")    