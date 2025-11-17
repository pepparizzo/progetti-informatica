"""Programma che chiede in input numeri sommare e ne restituisce la somma"""

numero = int (input ("Inserisci quanti numeri vuoi sommare:"))
somma = 0
i = 0
while i < numero:
    numeri = int (input ("Inserisci i numeri da sommare:")) 
    somma = somma + numeri 
    i = i + 1 
print ("La somma vale:", somma)