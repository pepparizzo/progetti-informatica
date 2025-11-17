"""Scrivere un programma che chiede all'utente di inserire le temperatura di due città per 5 giorni, e ne restituisce 
le differenze tra queste, stampando la differenza massima"""
 
tempNapoli= 5 * [0]
tempMilano = 5 * [0]
for i in range (0, len (tempNapoli)):
    tempNapoli [i] = int (input ("Inserisci la temperatura di Napoli:")) # faccio riempire l'Array contenente le temp. di Napoli dall'utente
for i in range (0, len (tempMilano)):
    tempMilano [i] = int (input ("Inserisci la temperatura di Milano:")) # faccio riempire l'Array contenente le temp. di Milano dall'utente
differenze = 5 * [0]
for i in range (0, 5):
    differenze [i] = tempMilano [i] - tempNapoli [i]
    if differenze [i] < 0:
        differenze [i] = differenze [i] * (-1)
    # print ("Le differenze tra le due città sono le seguenti:", differenze [i])
massimo = differenze [0]
posizionemassimo = 0
for i in range (0,5):
    if differenze [i] > massimo:
        massimo = differenze [i]
        posizionemassimo = i
print ("le differenze massime sono:", massimo,"rilevata il giorno", posizionemassimo+1)
