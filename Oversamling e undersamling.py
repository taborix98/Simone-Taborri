data = {
    "Id" : range(1,21),
    "imp_transazione" : [50,200,150,80,90,300,500,30,700,1000,40,100,60,120,180,250,90,600,800,2000],
    "frode" : [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0]
}
df = pd.DataFrame(data)
df_frodi = df[df["frode"]==1]
df_non_frodi = df[df["frode"]==0]
df_oversampled = pd.concat([df,df_frodi.sample(n=len(df_non_frodi),replace=True,random_state=42)])
df_undersampled = pd.concat([df_non_frodi.sample(n=len(df_frodi),random_state=42),df_frodi])
