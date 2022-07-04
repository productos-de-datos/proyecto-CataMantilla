"""
Modulo Creación data_lake

Se crea el data lake con las siguientes capas

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

def create_data_lake():
    
    import os

    os.mkdir("data_lake")

    directory = [
        "landing",
        "raw",
        "cleansed",
        "business",
    ]

    for carpet in directory:
        os.mkdir(os.path.join("data_lake", carpet))
    
    dir_business = [
        "business/reports",
        "business/reports/figures",
        "business/features",
        "business/forecasts",
    ]

    for carpet in dir_business:
        os.mkdir(os.path.join("data_lake", carpet))


if __name__ == "__main__":
    import doctest

    create_data_lake()
    doctest.testmod()
