import pandas as pd
import numpy as np

batting = pd.read_csv("data/lahman_data/Batting.csv")

batting = batting[batting["yearID"] >= 2000]
batting = batting[batting["AB"] >= 1]
drop_cols = ["stint", "lgID", "IBB", "SH", "CS", "G", "GIDP", "G_batting", "G_old"]
batting.drop(columns=drop_cols, inplace=True)
batting.reset_index(drop=True, inplace=True)

batting["1B"] = batting["H"]-batting["2B"]-batting["3B"]-batting["HR"]
batting["AVG"] = (batting["H"]/batting["AB"]).round(3)
batting["OBP"] = ((batting["H"]+batting["BB"]+batting["HBP"])/(batting["AB"]+batting["BB"]+batting["HBP"]+batting["SF"])).round(3)
batting["SLG"] = ((batting["1B"]+2*batting["2B"]+3*batting["3B"]+4*batting["HR"])/batting["AB"]).round(3)
batting["BABIP"] = ((batting["H"]-batting["HR"])/(batting["AB"]-batting["SO"]-batting["HR"]+batting["SF"])).round(3)
batting["ISO"] = (batting["SLG"]-batting["AVG"]).round(3)
batting['BB_pct'] = (batting['BB'] / batting['AB']).round(3)
batting['K_pct'] = (batting['SO'] / batting['AB']).round(3)
batting['XBH_pct'] = ((batting['2B'] + batting['3B'] + batting['HR']) / batting['H']).round(3)

batting["RBI"] = batting["RBI"].astype(int)
batting["SB"] = batting["SB"].astype(int)
batting["SO"] = batting["SO"].astype(int)
batting["HBP"] = batting["HBP"].astype(int)
batting["SF"] = batting["SF"].astype(int)

batting = batting.dropna(subset=["AB", "H", "HR", "2B", "3B", "BB", "SF"])
batting["BABIP"] = batting["BABIP"].fillna(0).astype(float)
batting["HBP"] = batting["HBP"].fillna(0).astype(int)
batting["SB"] = batting["SB"].fillna(0).astype(int)
batting["RBI"] = batting["RBI"].fillna(0).astype(int)
batting["R"] = batting["R"].fillna(0).astype(int)
batting["ISO"] = batting["ISO"].fillna(0).astype(float)
batting["BB_pct"] = batting["BB_pct"].fillna(0).astype(float)
batting["K_pct"] = batting["K_pct"].fillna(0).astype(float)
batting["XBH_pct"] = batting["XBH_pct"].fillna(0).astype(float)

batting.to_csv("data/lahman_data/batting_clean.csv", index=False, float_format="%.3f")
