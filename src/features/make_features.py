def make_features():
    """Crear archivo para el pronóstico.

    Crear el archivo data_lake/business/features/precios-diarios.csv.Este
    archivo contiene la información para pronosticar los precios diarios de la
    electricidad con base en los precios de los días pasados. Las columnas
    correspoden a las variables explicativas del modelo, y debe incluir,
    adicionalmente, la fecha del precio que se desea pronosticar y el precio
    que se desea pronosticar (variable dependiente).

    """
    import shutil

    shutil.copy('data_lake/business/precios-diarios.csv',
                'data_lake/business/features/precios_diarios.csv')



if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_features()