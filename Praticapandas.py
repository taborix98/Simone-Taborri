import pandas as pd
import numpy as np
#esercizio9
exam_data = pd.DataFrame(
    {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']},
index = ["a","b", "c", "d", "e", "f", "g", "h","i", "j"]
)
#esercizi 5-6, selezione colonne "name" e "score" nelle righe 1,3,5,6.
colonne_e_righe = exam_data.iloc[[1,3,5,6],[0,1]]
#esercizio7, selezionare colonne dove il numero di "attempts" sia superiore a 2.
attempts = exam_data[exam_data["attempts"]>2]
#esercizio8, contare numero colonne e righe.
numero_righe = exam_data.shape
#esercizio9, selezionare colonne di valore di "score" è Nan.
valori_mancanti = exam_data[exam_data["score"].isnull()]
#esercizio10, selezionare colonne dove "score" sia tra 15 e 20.
valori = exam_data[exam_data["score"].between(15,20)]
#esercizio11, selezionare colonne dove "attempts" sia inferiore a 2 e "score" sia maggiore di 15.
nuovi_valori = exam_data[(exam_data["attempts"]<2) & (exam_data["score"]>15)]
#esercizio12, cambiare il valore di "score" nella riga "d".
exam_data.loc["d","score"] = 11.5
#esercizio13, somma totale di valori di "attempts"
colonna = exam_data["attempts"].sum()
#esercizio14, calcolare la media di "score".
media = exam_data["score"].mean()
#esercizio15, aggiungere una nuova riga con valori indicati, poi eliminarla.
exam_data.loc["k"] = {"name" : "Suresh", "score": 15.5, "attempts": 1, "qualify": "yes"}
x = exam_data.drop("k")
#esercizio16, ordinare prima per nome in ordine descrescente e poi "score" in ordine crescente.
ordine = exam_data.sort_values(["name","score"],ascending=[False,True])
#esercizio17, sostituire "yes" e "no" nella colonna "qualify" con "true" o "false"
exam_data.replace({"yes": "True", "no": "False"}, inplace=True)
#esercizio18, sostiuire "James" con "Suresh".
exam_data.replace("James","Suresh",inplace=True)
exam_data.loc["d","name"] = "Suresh" #In questo modo gli dò la cella esatta dove fare la modifica.
#Si può fare sia indicando la colonna che senza. Io l'ho fatto senza, ma indicare la colonna può aiutare la precisione.
#esercizio19, eliminare colonna "attempts"
exam_data.drop("attempts",axis=1,inplace=True)
#exam_data.drop(columns=["attempts"], inplace=True)
#esercizio20, creare colonna "colori" con valori indicati
exam_data["color"]= "red","blue","green","brown","yellow","black","orange","blue","red","black","yellow"
#esercizio21, stampare una riga per volta.
for riga in exam_data.iterrows():
    print(riga)
    print()
#esercizio22, ottenere una lista con i nomi delle colonne.
print(list(exam_data.columns.values))
#esercizio23, rinominare i nomi delle colonne con la traduzione in italiano
exam_data.rename(columns={"name":"nome","score":"punteggio","attempts":"tentativi","qualify":"qualificati","color":"colori"},inplace=True)
#esercizio24, selezionare colonne dove "qualificati" è true.
filtrata = exam_data["qualificati"] == "True"
print(exam_data[filtrata])
#esercizio25, cambiare ordine colonne
print(exam_data.reindex(columns=["punteggio","nome","colori","qualificati"])) #si sceglie l'ordine delle colonne
#esercizio26, #aggiungere una colonna
nuovo_dataframe = pd.DataFrame (
    {"col a" : [1,2,3],
     "col b" : [4,5,6],
    "col c": [7,8,9]
    })
nuovo_dataframe.loc["3"] = 10,11,12
#esercizio28, quante persone provengono da ogni città.
df1 = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'city': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles']})
g1 = df1.groupby(["city"]).size().reset_index(name='Number of people')
#esercizio31, selezionare una precisa colonna
riga_da_selezionare = exam_data.iloc[1]
#esercizio32, sostituire il valore nullo con lo 0 in una specifica colonna.
exam_data["punteggio"] = exam_data["punteggio"].fillna(0)
#esercizio33, creare colonna con indici
exam_data["index"] = exam_data.index #crea una colonna con i valori degli indici
#esercizio34, modificare una cella specifica.
exam_data.loc["e","punteggio"] = 10
#esercizio35, contare quanti valori nulli ci sono nel dataframe.
conteggio = exam_data.isna().sum()
#esercizio36, eliminare specifiche righe.
exam_data = exam_data.drop(["a","e"])
