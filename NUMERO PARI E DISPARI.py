# Programma che chiede in input un numero, ne fa la divisione intera e vede se il numero è pari o dispari
numero = int (input ("Inserisci un numero intero:")) #qui chiedo in input all'utente un numero intero
resto = numero % 2 #inserisco nella variabile resto il risultato del modulo 2
if resto == 0:
    print ("Numero pari")
else:
    print ("Numero dispari")