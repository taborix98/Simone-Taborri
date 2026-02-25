pd.set_option("display.max_columns",None)
data = {
    "ID" : [1,2,3,4,5,6,7,8,9,10],
    "Età" : [25,30,35,40,29,50,45,33,27,38],
    "Salario" : [3000,4500,5000,6000,7000,8000,9000,7500,6200,7200]
}
df = pd.DataFrame(data)
scaler_minmax = MinMaxScaler()
df[["Età_Norm","Salario_Norm"]] = scaler_minmax.fit_transform(df[["Età","Salario"]])
print(df)
