import matplotlib.pyplot as plt
import pandas as pd 
def missing_aggregation(df):
        # Identifiera kolumner med NaN-värden
    nan_columns = df.columns[df.isna().any()].tolist()

    # Räkna antalet NaN-värden per kolumn
    nan_counts = df[nan_columns].isna().sum()

    # Skapa stapelplot
    for i, value in enumerate(nan_counts.values):
        plt.text(i, value - 1, str(value), ha='center')

    nan_counts.plot(kind='bar')
    plt.title('Antal NaN-värden per kolumn')
    plt.xlabel('Kolumner')
    plt.ylabel('Antal NaN-värden')
    plt.show()