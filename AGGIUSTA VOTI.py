"""programma che chiede in input n punteggi e aggiusta il punteggio
 se le insufficienze sono il 50% dell'esame: in questo caso si alza il voto di 3 a tutti:"""

quantità = int (input ("Inserisci la quantità di voti:"))
voti = quantità * [0]
insufficiente = 0
for i in range (0, quantità):
    voti [i] = int (input ("Inserisci voti:"))
    if voti [i ] < 18:
        insufficiente = insufficiente + 1
if insufficiente > quantità / 2:
        for i in range (0, quantità):
             voti [i] = voti [i] + 3 
             print ("Il voto è:", voti [i] )
print (voti)