import pandas as pd
import datetime


def handleMissingValues(df):
    # print column names with missing values
    for column in df.columns:
        missing_values = df[column].isnull().sum()
        if missing_values > 0:
            print(f"Column '{column}' has {missing_values} missing values.")


    # replacing the missing values of Seats with the mode value. as it will be obvious for most of the missing values.
    mode_seats = df['Seats'].mode()[0]
    print(f"Mode of seats: {mode_seats}")
    df['Seats'].fillna(mode_seats, inplace=True)

    # dropping Mileage, Engine and Power column as the missing row count is very less to be ignored
    df = df.dropna(subset=['Mileage', 'Engine', 'Power'])

    # Keeping New_Price as it is because the missing row count is too big to drop. And choosing from mean, median or mode does not make sense for it

    return df


def removeStringSuffixFromData(df):
    df['Mileage'] = df['Mileage'].str.replace("kmpl", '').str.replace("km/kg", '')
    df['Mileage'] = pd.to_numeric(df['Mileage'], errors='coerce')

    df['Engine'] = df['Engine'].str.replace("CC", '').str.replace(",", '')
    df['Engine'] = pd.to_numeric(df['Engine'], errors='coerce')

    df['Power'] = df['Power'].str.replace("bhp", '').str.replace(",", '')
    df['Power'] = pd.to_numeric(df['Power'], errors='coerce')

    df['New_Price'] = df['New_Price'].str.replace("Lakh", '')
    df['New_Price'] = pd.to_numeric(df['New_Price'], errors='coerce')

    return df



def convertFuelTypeAndTransmissionToNumeric(df):
    # mapping Diesel => 1, Petrol => 2, Electric => 3
    df['Fuel_Type'] = df['Fuel_Type'].replace({'Diesel': 1, 'Petrol': 2, 'Electric': 3})

    # mapping Manual => 1, Automatic => 2
    df['Transmission'] = df['Transmission'].replace({'Manual': 1, 'Automatic': 2})

    return df




def cleanup():
    df = pd.read_csv('../data_raw/train.csv')
    df = handleMissingValues(df)
    df = removeStringSuffixFromData(df)
    df = convertFuelTypeAndTransmissionToNumeric(df)
    df.to_csv('../data_clean/clean_data.csv')



cleanup()