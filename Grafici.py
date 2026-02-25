'''
data = pd.DataFrame({
    "altezza": [150,160,170,180,190,200],
    "peso": [50,60,70,80,90,100]
})
sns.scatterplot(x="altezza",y="peso",data= data,color="blue")
plt.title("Relazione tra altezza e peso")
plt.show()
'''

'''
data = pd.DataFrame({
    "Categoria": ["A","A","A","B","B","B"],
    "Valore": [10,12,15,30,35,80]
})
sns.boxplot(x="Categoria",y="Valore",data=data,palette="Set2")
plt.title("Box Plot - Individuazione Outlier")
plt.show()
'''

'''
df = pd.DataFrame(np.random.randn(5,5),columns=list("ABCDE"))
correlation_matrix= df.corr()
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm",linewidths=0.5)
plt.title("Mappa di correlazione tra variabili")
plt.show()
'''

'''
df = pd.DataFrame ({
    "Altezza": np.random.randint(150,200,100),
    "Peso" : np.random.randint(50,100,100)
})
sns.scatterplot(x="Altezza",y="Peso",data=df)
plt.title("Relazione tra Altezza e Peso")
plt.show()
'''
'''
