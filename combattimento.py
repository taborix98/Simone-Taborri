#Simulatore di Combattimento a Turni
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
    def attacca (self,avversario, personaggi, sono_io = False, io = None):
        avversario.puntivita-= self.attacco * (1.0- (avversario.difesa/100))
        if avversario.puntivita <= 0:
            avversario.morto(personaggi)
            if sono_io:
                return False, -1
        try:
            return True , personaggi.index(io)
        except:
            return True, -1
    
    def morto(self, personaggi):        
        self.puntivita = 0

        personaggi.remove(self)  # Rimuove il personaggio dalla lista dei personaggi
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
    
class fragile(personaggio):
    def __init__(self,nome):
        super().__init__(nome,20,60,5)
    def __str__(self):
        return super().__str__()
    
class gioco:
    def __init__(self, io = 0):
        self.personaggi= []
        self.personaggi.append(guerriero("thor"))
        self.personaggi.append(arciere("robin hood"))
        self.personaggi.append(guerriero("capitan america"))
        self.personaggi.append(arciere("guglielmo tell"))
        self.personaggi.append(fragile("fabio"))
        self.io = io
        self.sono_vivo = True
        pass
    def decidi_giocatore(self, io):
        self.io = io

    def turno(self):
        
        for x in self.personaggi:

            # Se il personaggio è lo stesso del giocatore            
            if self.sono_vivo and (x == self.personaggi[io]):
                # Gestisci il personaggio del giocatore
                print(f"{x.nome}, è il tuo turno! Scegli un avversario da attaccare:")
                avversario = int(input ())
                while (avversario < 0 or avversario >= len(self.personaggi)) or (avversario == io):
                    print("Avversario non valido, riprova.")
                    print(f"{x.nome}, è il tuo turno! Scegli un avversario da attaccare:")
                    avversario = int(input())
                
                print(f"{x.nome} attacca {self.personaggi[avversario].nome}!")
                self.io = x.attacca(self.personaggi[avversario], self.personaggi, False, self.personaggi[io])[1]

                self.stampa_personaggi()
                    
            else:
                # Altrimenti gestisci il personaggio dal computer
                import random 
                avv = random.choice(self.personaggi)

                while avv == x:
                    print(x.nome, "ha provato ad attaccare se stesso, riprova.")
                    avv = random.choice(self.personaggi) 
                if (self.io != -1):
                    temp = x.attacca(avv, self.personaggi, avv == self.personaggi[self.io], self.personaggi[self.io])
                    self.sono_vivo = temp[0]
                    self.io = temp[1]
                    print(temp)
                else:
                    x.attacca(avv, self.personaggi)
                
                print(f"{x.nome} attacca {avv.nome}!")
                self.stampa_personaggi()
                
                

    def stampa_personaggi(self):
        print("Dati personaggi: ")
        for x in self.personaggi:
            print(self.personaggi.index(x), end=": ")
            print(x)
        print("\n")


g = gioco ()
print ("Simulatore di Combattimento a Turni")
print ("=====================================")
print ("Personaggi disponibili: ")
g.stampa_personaggi()
print("=====================================")
print("Seleziona un personaggio per iniziare il combattimento: ")
io = int(input())

g.decidi_giocatore (io)

while len(g.personaggi) > 1:
    g.turno()

print (g.personaggi[0].nome, "è il vincitore!")

print("Il combattimento è terminato!")

