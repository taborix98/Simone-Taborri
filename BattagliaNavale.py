'''
Nell'esercizio di battaglia navale ho creato due mappe in un file esterno da poter scegliere per giocare,
poi le ho importante nel codice del gioco e ho creato le classi per poter utilizzare due giocatori. 
Ho creato due funzioni: una che controllasse se uno dei giocatori avesse perso la partita e
l'altra per controllare se con un turno fosse stata colpita la nave avversaria.; 
ho anche creato una mappa che segnasse le caselle in cui si era già tirato, per evitare che si ripetesse un tiro 
(utilizzando uno stesso simbolo sia per i tiri andati a segno che per quelli non andati a segno, in modo da non dare indizi).
Per ultimo, ho creato una funzione che partisse con un while, 
in modo che si protraesse fino a che nessuno dei due giocatori avesse perso la partita 
e nelle righe successive viene data la possibilità ai giocatori di inserire il numero della riga e della colonna in cui colpire.
'''
mappe = [
    [
       ["O","O","O","O","O",".",".",".",".","."],
       [".",".",".",".",".","O",".",".",".","."],
       [".",".",".",".",".","O",".",".",".","."],
       [".",".",".",".",".","O",".",".","O","O"],
       [".",".",".",".",".","O",".",".",".","."],
       [".",".",".",".",".",".",".",".","O","."],
       [".","O","O","O",".",".",".",".","O","."],
       [".",".",".",".",".",".",".",".","O","."],
       [".",".",".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".",".",".","."],
    ],[
       [".",".",".",".",".",".",".",".","O","."],
       [".",".",".","O",".",".",".",".","O","."],
       [".",".",".","O",".",".",".",".","O","."],
       [".",".",".","O",".",".",".",".","O","."],
       [".",".",".",".",".",".",".",".","O","."],
       [".",".",".",".",".",".","O","O",".","."],
       [".","O","O","O",".",".",".",".",".","."],
       [".",".",".",".",".",".",".",".",".","."],
       [".",".",".",".",".","O","O","O","O","."],
       [".",".",".",".",".",".",".",".",".","."]
    ],[
       [".",".",".",".",".","O","O",".",".","."],
       [".",".",".",".",".",".",".",".",".","."],
       [".",".",".",".","O","O","O",".",".","."],
       [".",".",".",".",".",".",".","O",".","."],
       [".",".",".",".",".",".",".","O",".","."],
       [".",".",".","O","O","O",".","O",".","."],
       [".",".",".",".",".",".",".","O",".","."],
       [".",".",".",".",".",".",".","O",".","."],
       [".",".",".","O","O","O","O",".",".","."],
       [".",".",".",".",".",".",".",".",".","."]
    ],[
       [".",".",".",".",".",".",".",".",".","."],
       [".","O","O","O","O","O",".",".",".","."],
       [".",".",".",".",".",".",".",".",".","."],
       [".",".",".","O","O","O",".",".",".","."],
       [".",".",".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".","O","O",".","."],
       [".",".",".",".","O",".",".",".",".","."],
       [".",".",".",".","O",".",".",".",".","."],
       [".",".",".",".","O",".",".",".",".","."],
       [".",".",".",".",".","O","O","O","O","."]
    ],
]

class Giocatore:
    def __init__(self,griglia):
        self.griglia = griglia
       
    def check_sconfitta(self):
        for i in self.griglia:
            for x in i:
                if x == "O":
                    return False
        return True
    def check_colpito(self,riga,colonna):
        if self.griglia[riga][colonna] == "O":
            self.griglia[riga][colonna] = "X"
            return True
        else:
            self.griglia[riga][colonna] = "x"
            return False
        

    def stampa_griglia(self):
        for x in self.griglia:
            print(x)
        print()
    
    def stampa_griglia_censurata(self):
        for i in self.griglia:
            for x in i:
                if x == "X" or x =="x":
                    print(x,end= " ")
                else:
                    print(".",end=" ")
            print()
        


for i in range(0, len(mappe.mappe)):
    print(f"Mappa numero: {i+1}")
    print()
    for x in mappe.mappe[i]:
        print(x)
    print()    
while True:
    mappa_da_utilizzare = int(input("Inserire mappa da utilizzare: "))
    mappa_da_utilizzare = mappa_da_utilizzare-1
    if mappa_da_utilizzare < 0 or mappa_da_utilizzare > len(mappe.mappe):
        print("Valore inserito fuori scala. Inserire valore tra 1 e lunghezza della lista:")
    else:
        break

giocatore1 = Giocatore(mappe.mappe[mappa_da_utilizzare])
giocatore1.stampa_griglia()



while True:
    mappa_da_utilizzare2 = int(input("Inserire mappa da utilizzare: "))
    mappa_da_utilizzare2 = mappa_da_utilizzare2-1
    if mappa_da_utilizzare2 < 0 or mappa_da_utilizzare2 > len(mappe.mappe):
        print("Valore inserito fuori scala. Inserire valore tra 1 e lunghezza della lista:")
    else:
        break


giocatore2 = Giocatore(mappe.mappe[mappa_da_utilizzare2])
giocatore2.stampa_griglia()



class Battaglianavale:
    def __init__(self,giocatore1,giocatore2):
        self.giocatore1 = giocatore1
        self.giocatore2 = giocatore2

    def partita(self):
        turno = True
        while not self.giocatore1.check_sconfitta() and not self.giocatore2.check_sconfitta():
            if turno:
                print("È il turno di giocatore 1")
                self.stampa_griglia_avversario("1")
                while True:
                    attacco_riga = int(input("Inserire riga: "))
                    if attacco_riga <0 or attacco_riga >9:
                        print("Inserito valore non valido. Inserire valore tra 0 e 9")
                    else:
                        break
                while True:
                    attacco_colonna = int(input("Inserire colonna: "))
                    if attacco_colonna <0 or attacco_colonna >9:
                        print("Inserire valore non valido. Inserire valore tra 0 e 9.")
                    else:
                        break
                if self.giocatore2.check_colpito(attacco_riga,attacco_colonna):
                    print("Colpito")
                else:
                    print("Mancato")
                turno = not turno
            else:
                print("È il turno di giocatore 2")
                self.stampa_griglia_avversario("2")
                while True:
                    attacco_riga = int(input("Inserire riga: "))
                    if attacco_riga <0 or attacco_riga >9:
                        print("Inserito valore non valido. Inserire valore tra 0 e 9")
                    else:
                        break
                while True:
                    attacco_colonna = int(input("Inserire colonna: "))
                    if attacco_colonna <0 or attacco_colonna >9:
                        print("Inserire valore non valido. Inserire valore tra 0 e 9.")
                    else:
                        break
                if self.giocatore1.check_colpito(attacco_riga,attacco_colonna):
                    print("Colpito")
                else:
                    print("Mancato")
                turno = not turno
        if turno:
            print("Ha vinto giocatore 1")
        else:
            print("Ha vinto giocatore 2")
    
        
    def stampa_griglia(self,giocatore):
        if giocatore == "1":
            self.giocatore1.stampa_griglia()
        if giocatore == "2":
            self.giocatore2.stampa_griglia()
        
    def stampa_griglia_avversario(self,giocatore):
        if giocatore == "1":
            self.giocatore2.stampa_griglia_censurata()
        if giocatore == "2":
            self.giocatore1.stampa_griglia_censurata()
    
b = Battaglianavale(giocatore1,giocatore2)
b.partita()
