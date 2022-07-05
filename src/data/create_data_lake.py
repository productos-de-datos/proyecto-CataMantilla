"""
Modulo Creación data_lake
---------------------------------------------
create_data_lake
crea el data lake con las siguientes capas

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```
"""
import os

def create_data_lake():
    """create_data_lake crea el datalake con las capas requeridas"""

    os.mkdir("data_lake")

    directory = [
        "landing",
        "raw",
        "cleansed",
        "business",
    ]

    for folder in directory:
        os.mkdir(os.path.join("data_lake", folder))
    dir_business = [
        "business/reports",
        "business/reports/figures",
        "business/features",
        "business/forecasts",
    ]

    for folder in dir_business:
        os.mkdir(os.path.join("data_lake", folder))


if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
    create_data_lake()