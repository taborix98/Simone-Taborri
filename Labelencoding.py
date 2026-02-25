pd.set_option("Display.max_columns",None)
data = {
    "ID" : [1,2,3,4,5,6,7,8,9,10],
    "Categoria" : ["A","B","A","B","C","A","B","C","C","A"]
}
df = pd.DataFrame(data)
label_encoder = LabelEncoder()
df["Categoria_LabelEncoded"] = label_encoder.fit_transform(df["Categoria"])
print(df)
