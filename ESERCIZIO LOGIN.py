"""Creare un programma in cui viene chiesto all'utente di decidere Username e Password di un sito. Dopo aver deciso le credenziali,
il programma chiede all'utente di effettuare un tentativo di login inserendo Username e password. Se le informazioni 
inserite sono corrette il programma stampa benvenuto altrimenti il programma stampa un messaggio di errore"""

nomeutente = str (input ("Inserisci il nome utente:"))
password = str (input ("inserisci password:"))
print ("LOGIN")
verifica1 = str (input("inserisci nome utente"))
verifica2 = str (input ("inserisci password"))
if (verifica1 == nomeutente) and (verifica2 == password):
    print ("BENVENUTO")
else:
    print ("INFORMAZIONI ERRATE")