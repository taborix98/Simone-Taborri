'''
#Array 50×3: [sku, pezzi, priorità] (priorità 1=alta, 3=bassa).
#Estrai tutte le spedizioni priorità alta.
#Ordina per priorità poi per pezzi (stabile).
#Aumenta di +1 pezzo tutti gli ordini con pezzi < 3 (broadcasting).
array= np.array ([
    ["SKU001", 1, 1],
    ["SKU002", 32, 2],
    ["SKU003", 278, 3],
    ["SKU004", 410, 1],
    ["SKU005", 95, 2],
    ["SKU006", 366, 3],
    ["SKU007", 57, 1],
    ["SKU008", 220, 2],
    ["SKU009", 489, 1],
    ["SKU010", 134, 3],
    ["SKU011", 261, 1],
    ["SKU012", 80, 2],
    ["SKU013", 390, 3],
    ["SKU014", 174, 2],
    ["SKU015", 472, 1],
    ["SKU016", 204, 3],
    ["SKU017", 98, 1],
    ["SKU018", 352, 2],
    ["SKU019", 289, 3],
    ["SKU020", 440, 1],
    ["SKU021", 118, 2],
    ["SKU022", 330, 3],
    ["SKU023", 259, 1],
    ["SKU024", 475, 2],
    ["SKU025", 147, 3],
    ["SKU026", 305, 1],
    ["SKU027", 410, 2],
    ["SKU028", 76, 3],
    ["SKU029", 221, 1],
    ["SKU030", 182, 2],
    ["SKU031", 492, 1],
    ["SKU032", 314, 3],
    ["SKU033", 266, 2],
    ["SKU034", 89, 1],
    ["SKU035", 370, 2],
    ["SKU036", 128, 3],
    ["SKU037", 410, 1],
    ["SKU038", 271, 2],
    ["SKU039", 349, 3],
    ["SKU040", 55, 1],
    ["SKU041", 385, 2],
    ["SKU042", 470, 1],
    ["SKU043", 243, 3],
    ["SKU044", 377, 2],
    ["SKU045", 162, 1],
    ["SKU046", 301, 3],
    ["SKU047", 409, 2],
    ["SKU048", 230, 1],
    ["SKU049", 488, 3],
    ["SKU050", 195, 2],
])
mask = array[:,2] == "1"
priorita = array[mask]
#print(priorita)
pezzi = array[:, 1].astype(int)
priorita2 = array[:, 2].astype(int)
idx = np.lexsort((pezzi,priorita))
ordinato = array[idx]
#print(ordinato)
pezzi = array[:, 1].astype(int)
mask = pezzi < 3
pezzi[mask] += 1
array[:, 1] = pezzi.astype(str)
print(array)
'''



'''
#Array 15×2: [id_piatto, prezzo_cent] (prezzo in centesimi).
#Trova gli indici dei piatti con prezzo compreso tra 8€ e 12€.
#Sconta del 10% i piatti con id_piatto pari (arrotonda per difetto).
#Concatena in coda 3 nuovi piatti e ri-ordina per prezzo.
piatti = np.array([
    [101, 1250],
    [102, 980],
    [103, 1430],
    [104, 1110],
    [105, 890],
    [106, 1990],
    [107, 1350],
    [108, 1270],
    [109, 1500],
    [110, 950],
    [111, 870],
    [112, 1550],
    [113, 2200],
    [114, 1760],
    [115, 990]
])
array = piatti[:,1] >=800
array2 = piatti[:,1] <=1200
prezzi = piatti[array * array2]
#print(prezzi[:,0])
mask = piatti[:,0] % 2==0
id_pari = piatti[mask]
sconti = (id_pari[:,1] *0.9).astype(int)
print(sconti)
piatti2 = np.array ([
    [116,1000],
    [117,1100],
    [118,950]
])
concatenato = np.concatenate([piatti,piatti2])
ordinato = concatenato[concatenato[:, 1].argsort()]
print(ordinato)
'''


'''
#array 6×3: [città_id, durata_volo_min, scalo(0/1)].
#Estrai gli itinerari senza scalo e prendi solo città_id.
#Ordina per durata_volo_min e prendi i primi 3.
#Aggiungi una colonna 6×1 con un flag “selezionato” (tutti 0), poi imposta a 1 i 3 più brevi.
'''
voli = np.array([
    [1, 120, 0],   # Città 1, 2 ore, diretto
    [5, 300, 1],   # Città 5, 5 ore, con scalo
    [12, 180, 0],  # Città 12, 3 ore, diretto
    [7, 240, 1],   # Città 7, 4 ore, con scalo
    [20, 90, 0],   # Città 20, 1.5 ore, diretto
    [3, 360, 1]    # Città 3, 6 ore, con scalo
])
mask = voli[::,2] ==0
senza_scalo = voli[mask][::,0]
#print(senza_scalo)
durata = voli[voli[:, 1].argsort()]
durata_3 = durata[:3]
#print(durata_3)
voli_2 = np.zeros((6,1))
concatenato = np.concatenate([voli,voli_2],axis=1)
#print(concatenato)
concatenato[np.argsort(concatenato[:,1]) [:3]][:,3]=1
print(concatenato)
'''
