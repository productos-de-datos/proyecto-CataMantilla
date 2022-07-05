"""
Modulo de entrenamiento del modelo
----------------------------------------
Entrena el modelo de pronóstico de precios diarios usando
 'Random Forest Regression' los resultados son
salvados en la siguiente ruta:  models/precios-diarios.pkl
los datos para este entrenamiento se encuentran en la ruta:
data_lake/business/features/precios_diarios.csv
Funciones usadas
"""
def load_data():
    """funcion load_data carga los datos"""
    
    import pandas as pd

    in_path = 'data_lake/business/features/precios_diarios.csv'
    data = pd.read_csv(in_path, sep = ',')
    return data

def transform_data(data):
    """función transform_data le da formato a los datos"""
    import pandas as pd

    df = data.copy()
    df['fecha'] =pd.to_datetime(df['fecha'], format = '%Y-%m-%d')
    df['year'], df['month'], df['day'] = df['fecha'].dt.year, df['fecha'].dt.month, df['fecha'].dt.day
    
    y = df['precio']
    x = df.copy()
    x.pop('precio')
    x.pop('fecha')
    return x, y

def make_train_test_set(x, y):
    """Función make_train_test_set hace partición de datos"""
    from sklearn.model_selection import train_test_split

    (x_train, x_test, y_train, y_test) = train_test_split(
        x,
        y,
        test_size = 0.30,
        random_state = 12345,
    )
    return x_train, x_test, y_train, y_test 

def train_model(x_train, x_test):
    """train_model escala  los datos u crea el modelo"""
    from sklearn.preprocessing import StandardScaler
    from sklearn.ensemble import RandomForestRegressor

    
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.fit_transform(x_test)

    model = RandomForestRegressor(n_jobs=-1)
    return model

def save_model(model):
    """save_model guarda el modelo en el formato pickle"""

    import pickle

    with open("src/models/precios-diarios.pickle", "wb") as file:
        pickle.dump(model, file,  pickle.HIGHEST_PROTOCOL)

def train_daily_model():
    """train_daily_model"""
    try:
        data = load_data()
        x, y = transform_data(data)
        x_train, x_test, y_train, y_test = make_train_test_set(x, y)
        model = train_model(x_train, x_test)
        save_model(model)
    except:
        raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    train_daily_model()