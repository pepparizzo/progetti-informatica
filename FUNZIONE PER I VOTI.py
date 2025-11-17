# Programma che prende in input i voti di 3 materie (storia, italiano, matematica) e mi dice se ci sono dei 10

def CreaArray ():
    n = int (input ("Inserisci la dimensione dell'array"))
    vett = n * [0]
    for i in range (0, n): 
        vett [i] = int (input ("Inserisci un valore dell'array"))
    return vett

def CercaInArray (vett, x): 
    for i in range (0, len (vett)):
        if vett [i]== x: 
            return True
    else: 
        return False 
    





print ("Scrivimi i voti di storia")
storia = CreaArray
risultatoStoria = CercaInArray (storia, 10)
print ("Scrivimi i voti di matematica")
matematica = CreaArray
risultatoMatematica = CercaInArray (matematica, 10)
print ("Scrivimi i voti di Italiano")
italiano = CreaArray
risultatoItaliano = CercaInArray (italiano, 10)
if risultatoStoria == True:
    print ("Ci sono 10 in Storia")
else: 
    print ("Non ci sono 10 in storia")
if risultatoItaliano == True: 
    print ("Ci sono 10 in italiano")
else: 
    print ("Non ci sono 10 in italiano")
if risultatoMatematica == 10:
    print ("Ci sono 10 in matematica")
else:
    print ("Non ci sono 10 in matematica")