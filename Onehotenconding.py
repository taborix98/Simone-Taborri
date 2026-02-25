data = {
    "ID" : [1,2,3,4,5,6,7,8,9,10],
    "Categoria" : ["A","B","A","B","C","A","B","C","C","A"]
}
df = pd.DataFrame(data)
one_hot_encoder = OneHotEncoder(sparse_output=False)
encoded_columns = one_hot_encoder.fit_transform(df[["Categoria"]])
encoded_df = pd.DataFrame(encoded_columns,columns=one_hot_encoder.get_feature_names_out(["Categoria"]))
df = pd.concat([df,encoded_df],axis=1)
print(df)
