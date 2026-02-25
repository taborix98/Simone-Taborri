#2. Simulatore di Combattimento a Turni
#Descrizione:
#Due o più personaggi combattono a turni, con punti vita, attacchi speciali, difesa, ecc.
#Concetti usati:
#• Classi e oggetti
#• Strutture dati (liste, dizionari)
#• Logica di gioco
# Random (solo random è ok, fa parte della standard library)
#Espandibilità:
#Sistema di livelli, nemici controllati dal computer, strategie AI semplici.

class personaggio:
    def __init__(self,nome,attacco,difesa,puntivita):
        self.nome=nome
        #attacco da 0 a 100
        self.attacco= attacco 
        #la difesa quando è 0 quando è minima e 100 quando è massima
        self.difesa= difesa  
        self.puntivita= puntivita
    def attacca (self,avversario):
        avversario.puntivita-= self.attacco * (1.0- (avversario.difesa/100))
        if avversario.puntivita < 0:
            avversario.morto()
        pass
    
    def morto(self):
        self.puntivita = 0
        self.nome = f"{self.nome} (morto)"

    def __str__(self):
        return f"{self.nome} - Attacco: {self.attacco}, Difesa: {self.difesa}, Punti Vita: {self.puntivita}"

class guerriero(personaggio):
    def __init__(self,nome):
        super().__init__(nome,20,60,100)
    def __str__(self):
        return super().__str__()
        

class arciere(personaggio):
    def __init__(self,nome):
        super().__init__(nome,70,30,100)
    
    def __str__(self):
        return super().__str__()
    
class gioco:
    def __init__(self):
        self.personaggi= []
        self.personaggi.append(guerriero("thor"))
        self.personaggi.append(arciere("robin hood"))
        self.personaggi.append(guerriero("capitan america"))
        self.personaggi.append(arciere("guglielmo tell"))
        pass
    def turno(self):
        pass
        
    def stampa_personaggi(self):
        print("thor")
        print("Dati personaggi: ")
        for x in self.personaggi:
            print(x)
        print("\n")

g = gioco()

print("Inizio gioco: ")
g.stampa_personaggi()
print("Primo turno: \n")
g.turno()
g.stampa_personaggi()
print(" Secondo turno : \n")
g.turno()
g.stampa_personaggi()
