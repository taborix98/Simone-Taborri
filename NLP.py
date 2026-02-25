#carica il dataset
dataset = pd.read_csv("enron_spam_data.csv")

#prepara i dati
email_testo = dataset["message"].fillna() #sostituisce i nan con stringhe vuote
email_etichette = dataset["spam/ham"].apply(lambda x:1 if x=="spam" else 0) # 1= spam, 0 = non spam.

#creazione delle feature
vectorizer = TfidfVectorizer()
x_tfidf = vectorizer.fit_transform(email_testo)

#suddivisione dei dati in training e test set
x_train,y_train,x_test,y_test = train_test_split(x_tfidf, email_etichette, test_size=0.2, random_state=42)

#addestramento del modello naive bayes
model = MultinomialNB()
model.fit(x_train,y_train)

#previsione su una nuova email
nuova_email = "Ti invitiamo a una conferenza sulla sicurezza informatica."
testo_tradotto = GoogleTranslator(source="auto", target="en").translate(nuova_email)
x_nuova = vectorizer.transform([testo_tradotto])
predizione = model.predict(x_nuova)
print("Spam" if predizione[0] == 1 else "non spam")
