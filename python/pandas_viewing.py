import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mlb = pd.read_csv("batting.csv")
mlb.dropna()
#print(mlb.shape)
mlb.drop(["AVG", "OBP", "SLG"], axis=1,inplace=True)
#print(mlb.shape)

mlb["AVG"] = mlb["H"]/mlb["AB"]
mlb["OBP"] = (mlb["H"]+mlb["BB"]+mlb["HBP"])/(mlb["AB"]+mlb["BB"]+mlb["HBP"]+mlb["SF"])
mlb["SLG"] = (mlb["1B"]+2*mlb["2B"]+3*mlb["3B"]+4*mlb["HR"])/mlb["AB"]

#print(mlb.shape)

top_avg = mlb.sort_values("AVG",ascending=False).head(10)
top_obp = mlb.sort_values("OBP",ascending=False).head(10)
top_slg = mlb.sort_values("SLG",ascending=False).head(10)

# print(top_avg[["Name","AVG"]])
# print(top_obp[["Name","OBP"]])
# print(top_slg[["Name","SLG"]])

sns.lineplot(x=top_slg["Name"],y=top_slg["SLG"])
plt.title("Top 10 players in SLG 2023")
plt.show()
