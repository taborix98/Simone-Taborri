x = np.array ([
    [15,39],
    [16,81],
    [17,6],
    [18,77],
    [19,40],
    [20,76],
    [21,6],
    [22,94],
    [23,3],
    [24,72],
    ])
kmeans = KMeans(n_clusters=3,random_state=42)
kmeans.fit(x)
labels= kmeans.labels_
plt.scatter(x[:,0],x[:,1], c=labels, cmap="viridis",s=100) 
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], color="red",marker="x",s=200,label= "Centroidi")
plt.xlabel("Reddito(€)")
plt.ylabel("Spesa(€)")
plt.legend()
plt.show()
