dati= []
while true:
    nome= input ("Nome dello studente:")
    punteggio= int(input("inserisci i punti:"))
    if punteggio == 0:
        break
    valori.append(punteggio)
print (max(valori))