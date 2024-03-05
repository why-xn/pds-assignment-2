import pandas as pd
import datetime


def calculateAge(df):
    # Calculating Age of Car and creating a new column with the data
    current_year = datetime.datetime.now().year
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    df['Age'] = current_year - df['Year']
    return df


def process():
    df = pd.read_csv('../data_clean/clean_data.csv')

    df = calculateAge(df)

    # Select columns
    df_selected = df[['Name', 'Mileage', 'Engine', 'Power', 'Fuel_Type', 'Transmission', 'Age', 'Price']]
    print("Select Operation:")
    print(df_selected.head())
    print("\n")

    # Filter rows
    df_filtered = df[df['Age'] >= 10]
    print("Filter Rows:")
    print(df_filtered.head())
    print("\n")

    # Rename columns
    df_renamed = df.rename(columns={'Mileage': 'Mileage_kmpl', 'Engine': 'Engine_cc', 'Power': 'Power_bhp'})
    print("Rename columns:")
    print(df_renamed.head())
    print("\n")

    # Mutate (add new columns)
    df_mutated = df.assign(Total_Fuel_Spent=df['Kilometers_Driven'] / df['Mileage'])
    print("Mutate Column:")
    print(df_mutated.head())
    print("\n")

    # Arrange (sort)
    df_arranged = df_mutated.sort_values(by='Total_Fuel_Spent', ascending=True)
    print("Sort:")
    print(df_arranged.head())
    print("\n")

    # Summarize with group by
    df_grouped = df_renamed.groupby('Fuel_Type').agg({'Mileage_kmpl': 'mean'})
    print("Summarize with group by:")
    print(df_grouped.head())
    print("\n")



process()