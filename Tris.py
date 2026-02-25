scacchiera = [[".",".","."],[".",".","."], [".",".","."]]
pallino = "O"
croce = "X"
def vittoria(scacchiera):
    if scacchiera[0][0] == croce and scacchiera [0][1] == croce and scacchiera[0][2] == croce:
        return True
    elif scacchiera[0][0] == pallino and scacchiera [0][1] == pallino and scacchiera[0][2] == pallino:
        return True
    elif scacchiera[1][0] == croce and scacchiera [1][1] == croce and scacchiera[1][2] == croce:
        return True
    elif scacchiera[1][0] == pallino and scacchiera [1][1] == pallino and scacchiera[1][2] == pallino:
        return True
    elif scacchiera[2][0] == croce and scacchiera [2][1] == croce and scacchiera[2][2] == croce:
        return True
    elif scacchiera[2][0] == pallino and scacchiera [2][1] == pallino and scacchiera[2][2] == pallino:
        return True
    elif scacchiera [0][0] == pallino and scacchiera [1][0] == pallino and scacchiera[2][0] == pallino:
        return True
    elif scacchiera [0][0] == croce and scacchiera [1][0] == croce and scacchiera[2][0] == croce:
        return True
    elif scacchiera [0][1] == croce and scacchiera [1][1] == croce and scacchiera [2][1] == croce:
        return True
    elif scacchiera [0][1] == pallino and scacchiera [1][1] == pallino and scacchiera [2][1] == pallino:
        return True
    elif scacchiera [0][2] == croce and scacchiera [1][2] == croce and scacchiera [2][2] == croce:
        return True
    elif scacchiera [0][2] == pallino and scacchiera [1][2] == pallino and scacchiera [2][2] == pallino:
        return True
    elif scacchiera [0][0] == croce and scacchiera [1][1] == croce and scacchiera [2][2] == croce:
        return True
    elif scacchiera [0][0] == pallino and scacchiera [1][1] == pallino and scacchiera [2][2] == pallino:
        return True
    elif scacchiera [0][2] == croce and scacchiera [1][1] == croce and scacchiera [2][0] == croce:
        return True
    elif scacchiera [0][2] == pallino and scacchiera [1][1] == pallino and scacchiera [2][0] == pallino:
        return True
    else:
        pareggio = True
        for riga in scacchiera:
            for colonna in riga:
                if colonna == ".":
                    pareggio = False
                    break
        return pareggio

def stampa_scacchiera(scacchiera):
    for riga in range(0,3):
        print("\n")
        for colonna in range(0,3):
            print(scacchiera[riga][colonna] , " ", end="")
turno = True
while not vittoria(scacchiera):
    stampa_scacchiera(scacchiera)
    if turno:
        print("Sta giocando croce")
        cella = input("Inserire riga e colonna separate da una virgola: ").split(",")
        riga = int(cella[0])
        colonna = int(cella[1])
        if scacchiera [riga][colonna] == ".":
            scacchiera[riga][colonna] = croce
            turno = not turno
        else:
            print("Scelta non valida.")
    else:
        print("Sta giocando pallino")
        cella = input("Inserire riga e colonna separate da una virgola: ").split(",")
        riga = int(cella[0])
        colonna = int(cella[1])
        if scacchiera [riga][colonna] == ".":
            scacchiera[riga][colonna] = pallino
            turno = not turno
        else:
            print("Scelta non valida.")
stampa_scacchiera(scacchiera)
if not turno:
    print("Ha vinto X")
else:
    print("Ha vinto O")
'''




