"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------
Descarga los archivos de precios de bolsa nacional en los formatos xls y xlsx a
la capa data_lake/landing de la siguiente ruta:
    https://github.com/jdvelasq/datalabs/tree/master/datasets/precio_bolsa_nacional/


"""
def ingest_data():
    
    import requests
    from bs4 import BeautifulSoup
    import re
    
    url = 'https://github.com/jdvelasq/datalabs/tree/master/datasets/precio_bolsa_nacional/xls'

    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, features='html.parser')
    a_tags = soup.find_all('a')
    urls_xlsx = [
        'https://raw.githubusercontent.com' + re.sub('/blob', '', link.get('href'))
        for link in a_tags
        if '.xlsx' in link.get('href')
    ]

    for i in urls_xlsx:
        file = requests.get(i)
        open('data_lake/landing/{}'.format(i.split('/')[-1]), 'wb').write(file.content)
    
    for i in range(2016, 2018):
        url_xls = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xls?raw=true'.format(
            i
        )
        file = requests.get(url_xls, allow_redirects=True )
        open('data_lake/landing/{}.xls'.format(i), 'wb').write(file.content)


if __name__ == "__main__":
    import doctest

    ingest_data()
    doctest.testmod()
