"""
Modulo Limpieza de datos
-----------------------------------
La función clean_data
Usa los archivos data_lake/raw/*.csv, crea el archivo
data_lake/cleansed/precios-horarios.csv. el contiene 
lo siguiente:
    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional
El archivo contiene la información del rango comprendido
entre 1995 2021

"""
import os
import pandas as pd
import glob

def clean_data():
    
    cleansed_df = []

    for f in range(1995, 2022):
        df_read = pd.read_csv(
            'data_lake/raw/{}.csv'.format(f),
        )
        cleansed_df.append(df_read)
    
    frame = pd.concat(cleansed_df, axis=0, ignore_index=True)
    old_columns = frame.columns
    new_columns = ['fecha'] + ['{0:0=2d}'.format(int(i)) for i in old_columns[1:]]
    frame.columns = new_columns

    frame['fecha'] = pd.to_datetime(frame['fecha'], format = '%Y-%m-%d')
    unpivoted_table = frame.melt(
        id_vars = ['fecha'],
        value_vars = new_columns[1:],
        var_name = 'hora',
        value_name = 'precio',
    )
    unpivoted_table['precio'] = unpivoted_table['precio'].fillna(
        unpivoted_table.groupby('fecha')['precio'].transform('mean')
    )
    unpivoted_table.to_csv(
        'data_lake/cleansed/precios-horarios.csv', encoding='utf-8', index=False
    )

if __name__ == "__main__":
    import doctest
    
    clean_data()
    doctest.testmod()
