"""
Modulo de entrenamiento del modelo
----------------------------------------
Entrena el modelo de pronóstico de precios diarios usando
 'Random Forest Regression' los resultados son
salvados en la siguiente ruta:  models/precios-diarios.pkl
los datos para este entrenamiento se encuentran en la ruta:
data_lake/business/features/precios_diarios.csv
"""
def load_data():
    import pandas as pd

    in_path = 'data_lake/business/features/precios_diarios.csv'
    data = pd.read_csv(in_path, sep = ',')
    
    return data

def transform_data(data):
    import pandas as pd

    df = data.copy()
    df['fecha'] =pd.to_datetime(df['fecha'], format = '%Y-%m-%d')
    df['year'], df['month'], df['day'] = df['fecha'].dt.year, df['fecha'].dt.month, df['fecha'].dt.day
    
    y = df['precio']
    X = df.copy()
    X.pop('precio')
    X.pop('fecha')
    return X, y

def make_train_test_set(X, y):
    from sklearn.model_selection import train_test_split

    (X_train, X_test, y_train, y_test) = train_test_split(
        X,
        y,
        test_size = 0.30,
        random_state = 12345,
    )
    return X_train, X_test, y_train, y_test 

def train_model(X_train, X_test):
    from sklearn.preprocessing import StandardScaler
    from sklearn.ensemble import RandomForestRegressor

    """Normalitation StandardScaler"""
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.fit_transform(X_test)

    """Crear modelo"""
    model = RandomForestRegressor(n_jobs=-1)
    return model

def save_model(model):

    import pickle

    with open("src/models/precios-diarios.pickle", "wb") as file:
        pickle.dump(model, file,  pickle.HIGHEST_PROTOCOL)

def train_daily_model():
    try:
        data = load_data()
        X, y = transform_data(data)
        X_train, X_test, y_train, y_test = make_train_test_set(X, y)
        model = train_model(X_train, X_test)
        save_model(model)
    except:
        raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    train_daily_model()