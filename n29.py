nomi = []
EscursioniTermiche = []
contatore = 0
while True:
    città = input ("nome della città:    ")
    MassimoGradi = int (input ("temperatura massima prefissata:    "))
   MinimoGradi = int (input ("temperatura minima prefissata:    "))
    escursione_termica = (MassimoGradi - MinimoGradi)
    nomi.append (città)
    EscursioniTermiche.append (escursione_termica)
    if città == "0" or MassimoGradi == 0 or MinimoGradi == 0:
        for i in nomi:
            indice = nomi.index (i)
            MassimoGradi = int (input ("temperatura massima oggi:    "))
            MinimoGradi = int (input ("temperatura minima oggi:    "))
            EscursioneTermica2 = (MassimoGradi2 - MinimoGradi2)

            if EscursioneTermica2 > EscursioniTermiche [indice]:
                contatore += 1
        break
print ("le città che hanno avuto un'escursione termica maggiore rispetto alla prefissata sono", contatore)