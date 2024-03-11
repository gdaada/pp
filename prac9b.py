import pandas as pd
#data = {'Color':['Red', 'Blue', 'Green', 'Red', 'Blue', 'Green']}
data = pd.read_csv("Iris.csv")
df = pd.DataFrame(data)
df_encoded = pd.get_dummies(df, columns=['Species'])
print(data)
print("Original DataFrame: ")
print(df)
print("Dataframe after dummification: ")
print(pd.DataFrame(df_encoded))
