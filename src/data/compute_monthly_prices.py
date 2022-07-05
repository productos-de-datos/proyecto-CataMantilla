"""
Módulo Computar precio promedio mensual
-------------------------------------------------------------------------------
Función compute_monthly_prices 
Usando el archivo data_lake/cleansed/precios-horarios.csv, computa el precio
promedio mensual  para cada uno de los meses. Las
columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional
"""
import pandas as pd
def compute_monthly_prices():
    """compute_monthly_prices"""

    file = 'data_lake/cleansed/precios-horarios.csv' 
    mean_price = pd.read_csv(file)
    mean_price['fecha'] = pd.to_datetime(mean_price['fecha'])
    mean_price =(
        mean_price.groupby(pd.Grouper(key='fecha', freq='M')).mean().reset_index()
    )
    mean_price[['fecha', 'precio']].to_csv(
        'data_lake/business/precios-mensuales.csv',encoding='utf-8', index=False
    )


if __name__ == "__main__":
    import doctest

    compute_monthly_prices()
    doctest.testmod()