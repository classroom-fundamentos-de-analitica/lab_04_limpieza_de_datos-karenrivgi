"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import datetime as dt
import numpy as np

# /-----------------------------------------------------------------------------------------
# Funciones de limpieza para cada columna
# /-----------------------------------------------------------------------------------------

def clean_sexo_column(df): 
    df = df.copy()
    df.sexo = (df.sexo
               .str.lower()
               .str.capitalize())
    return df


def clean_tipo_de_emprendimiento_column(df):
    df = df.copy()
    df.tipo_de_emprendimiento = (df.tipo_de_emprendimiento
                                 .str.lower()
                                 .str.capitalize())
    return df


def clean_idea_negocio_column(df):
    df = df.copy()
    df.idea_negocio = (df.idea_negocio
                       .str.lower()
                       .str.capitalize()
                       .str.replace('_', ' ')
                       .str.replace('-', ' ')
                       .str.replace('.', ''))
    return df


def clean_barrio_column(df):
    df = df.copy()
    df.barrio = (df.barrio
                 .str.lower()
                 .str.capitalize()
                 .str.replace('_', ' ')
                 .str.replace('-', ' '))
    return df


def clean_estrato_column(df):
    df = df.copy()
    df.estrato = df.estrato.astype('category')
    return df


def clean_comuna_ciudadano_column(df):
    df = df.copy()
    df.comuna_ciudadano = df.comuna_ciudadano.astype(int)
    df.comuna_ciudadano = df.comuna_ciudadano.astype('category')
    return df


def clean_fecha_de_beneficio_column(df):
    df = df.copy()
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, format='mixed', dayfirst=True)
    return df


def clean_monto_del_credito_column(df):
    df = df.copy()
    df['monto_del_credito'] = (df['monto_del_credito']
                               .str.replace('$', '')
                               .str.replace(',', '')
                               .str.replace(' ', '').astype(float))
    return df


def clean_linea_credito_column(df):
    df = df.copy()
    df.línea_credito = (df.línea_credito
                        .str.lower()
                        .str.capitalize()
                        .str.replace('_', ' ')
                        .str.replace('-', ' ')
                        .str.replace('.', ''))
    return df

# /-----------------------------------------------------------------------------------------


# /-----------------------------------------------------------------------------------------
# Funcion de limpieza general
# /-----------------------------------------------------------------------------------------
def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    clean_df = df.copy()

    # Limpieza de datos
    clean_df = clean_sexo_column(clean_df)
    clean_df = clean_tipo_de_emprendimiento_column(clean_df)
    clean_df = clean_idea_negocio_column(clean_df)
    clean_df = clean_barrio_column(clean_df)
    clean_df = clean_estrato_column(clean_df)
    clean_df = clean_comuna_ciudadano_column(clean_df)
    clean_df = clean_fecha_de_beneficio_column(clean_df)
    clean_df = clean_monto_del_credito_column(clean_df)
    clean_df = clean_linea_credito_column(clean_df)

    # Eliminar duplicados
    clean_df = clean_df.drop_duplicates()

    # Eliminar filas con datos faltantes
    clean_df = clean_df.dropna()

    return clean_df
# /------------------------------------------------------------------------------------------