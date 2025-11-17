quantitàvoti = int (input ("Inserisci quanti voti")) 
i = 0 
insufficiente = 0
eccellenti = 0
while i<quantitàvoti:
    voti = int (input ("Inserisci il voto:"))
    if voti < 18:
        insufficiente = insufficiente + 1
    if voti > 29: 
        eccellenti = eccellenti + 1 
    i = i + 1
print ("La quantità di insufficiente è:", insufficiente)
print ("La quantità di eccellenti è:", eccellenti)
print ("La quantità di insufficienti è:", quantitàvoti - insufficiente)