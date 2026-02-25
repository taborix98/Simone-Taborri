x = np.array([50,60,70,80,90,100]).reshape(-1,1) #superficie in metri quadrati.
y = np.array([150000,180000,210000,240000,270000,300000]) #prezzi delle case
model = LinearRegression()
model.fit(x,y)
#print("Coefficiente (m):", model.coef_[0])
#print("Intercetta (b):", model.intercept_)
superficie_nuova = np.array([[75]]) #casa di 75 metri quadrati
prezzo_previsto = model.predict(superficie_nuova)
print(f"Prezzo previsto per 75 metri quadrati: {prezzo_previsto[0]:.2f}€")

plt.scatter(x,y,color="blue")
plt.plot(x,model.predict(x),color="red")
plt.xlabel("Superficie(metri quadrati)")
plt.ylabel("Prezzo(€)")
plt.show()
