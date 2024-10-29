import matplotlib.pyplot as plt
import pandas as pd 
def missing_aggregation(df):
        # Identifiera kolumner med NaN-värden
    nan_columns = df.columns[df.isna().any()].tolist()

    # Räkna antalet NaN-värden per kolumn
    nan_counts = df[nan_columns].isna().sum()

    # Skapa stapelplot
    nan_counts.plot(kind='bar')
    plt.title('Antal NaN-värden per kolumn')
    plt.xlabel('Kolumner')
    plt.ylabel('Antal NaN-värden')
    plt.show()