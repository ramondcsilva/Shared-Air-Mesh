# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 23:03:51 2021

@author: Ramon Silva
"""

import sqlite3

def createDatabase():    
    #inicia a escrito no documento JSON  
    
    con = sqlite3.connect('dbVoo.db')
    cur = con.cursor()
    
    cur.execute("drop table if exists viajem")
    
    cur.execute('''Create table viajem 
                   (id int unique, destino, vagas)''')
    
    cur.execute("insert or ignore into viajem values (1,'Aracajú', '09')")
    cur.execute("insert or ignore into viajem values (2,'Fortaleza', '10')")
    cur.execute("insert or ignore into viajem values (3,'João Pessoa', '30')")
    cur.execute("insert or ignore into viajem values (4,'Maceió', '45')")
    cur.execute("insert or ignore into viajem values (5,'Natal', '80')")
    cur.execute("insert or ignore into viajem values (6,'Recife', '80')")
    cur.execute("insert or ignore into viajem values (7,'Salvador', '60')")
    cur.execute("insert or ignore into viajem values (8,'São Luis', '50')")
    cur.execute("insert or ignore into viajem values (9,'Teresina', '00')")
    
    con.commit()
    con.close()
    
def buyTicket(data):
    # variavel que salva o id do paciente
    
    dataSave = data.split(",")
    
    if int(dataSave[1]) <= 0:
        return "Número de passagens inválido!"
    
    #inicia a escrita no Banco de dados  
    con = sqlite3.connect('dbVoo.db')
    cur = con.cursor()
    try:
        cur.execute("select vagas from viajem where destino = '"+dataSave[0]+"'")
    
        vagas = cur.fetchall()
        
        con.commit()
        
        if len(vagas) <= 0:
            return "Não existe viajem para este destino!"
        
    except:
        con.close()
        return "Não existe viajem para este destino!"
        
    con.close()
    
    for vaga in vagas:
        vagas = vaga
    
    vaga = str(int(vagas[0]) - int(dataSave[1]))

    if int(vaga) < 0:
        return "Não temos passagem suficiente! Temos apenas "+int(vagas[0])+" passagens!"
    elif int(vaga) == 0:
        return "As passagens para "+dataSave[0]+" estam esgotadas!"
    #inicia a escrita no Banco de dados  
    con = sqlite3.connect('dbVoo.db')
    cur = con.cursor()
    try:
        cur.execute("update viajem set vagas = '"+vaga+"' where destino = '"+dataSave[0]+"'")
            
        con.commit()
    
    
    except:
        con.close()
        return "Error na busca por destino!"
        
    con.close()
    
    
    if int(dataSave[1]) > 1:
        return "Passagens adquiridas com sucesso!"
    else:
        return "Passagem adquirida com sucesso!"
    
if __name__ == '__main__':
    createDatabase()