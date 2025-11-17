"""Programma che chiede in input all'utente le temperature di due città per una settimana,
successivamente, calcola per ogni città quante volte fa freddo"""

milano = 7*[0]
napoli = 7*[0]
freddonapoli = 0
freddomilano = 0
for i in range (0, 7):
    milano [i] = int (input ("Inserisci la temperatura di Milano:"))
    if milano [i] < 5:
        freddomilano = freddomilano + i
for i in range (0, 7):
    napoli [i] = int (input ("Inserisci la temperatura di Napoli:"))
    if napoli [i] < 5:
        freddonapoli = freddonapoli + 1
print ("Le temperature fredde di Napoli sonO:", freddonapoli, "volte")
print ("Le temperature fredde a Milano sono:", freddomilano, "volte")


