import pandas as pd

df = pd.read_csv("athlete_events.csv")

""" Tabell på antal medaljer per individ i tyskland """
ger_df = df[df["NOC"] == "GER"]
ger_df1 = pd.concat([ger_df,pd.get_dummies(df["Medal"])],axis = 1)
ger_indv_medals = ger_df1.groupby("NOC").sum()[["Gold","Silver","Bronze"]].sort_values("Gold",ascending=False).reset_index()

