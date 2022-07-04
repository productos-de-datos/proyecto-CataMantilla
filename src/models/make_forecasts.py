""" 
Modulo de pronósticos
-------------------------------------------------------------------------------
Contruye los pronósticos con el modelo entrenado(Random Forest Regression)
Crear el archivo data_lake/business/forecasts/precios-diarios.csv  de acuerdo
con la siguiente estructura:
    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.

funciones creadas
load_pkl, score, best_score
trein_model_with_best_estimator
forecasts
save_forecasts
make_forecasts
"""
import numpy as np
import pandas as pd
import pickle
from train_daily_model import load_data, transform_data, make_train_test_set

def load_pkl(infile):
    """load_pkl"""
    with open(infile, "rb") as file:
        model = pickle.load(file)
    return model


def score(x_train, y_train, x_test, y_test, model):
    """score"""
    estimators = np.arange(10, 200, 10)
    scores = []
    for n in estimators:
        model.set_params(n_estimators=n)
        model.fit(x_train, y_train)
        scores.append(model.score(x_test, y_test))
    return scores


def best_score(scores):
    """best_score"""
    estimador_n = pd.DataFrame(scores)
    estimador_n.reset_index(inplace=True)
    estimador_n = estimador_n.rename(columns={0: 'scores'})
    estimador_n = estimador_n[estimador_n['scores']
                              == estimador_n['scores'].max()]
    estimador_n['index'] = (estimador_n['index']+1)*10
    estimador_n = estimador_n['index'].iloc[0]
    return estimador_n

def trein_model_with_best_estimator(estimador_n, x_train, y_train):
    """trein_model_with_best_estimator"""
    from sklearn.ensemble import RandomForestRegressor

    model = RandomForestRegressor(
        n_estimators=estimador_n, random_state=12345)
    model.fit(x_train, y_train)
    return model


def prediction_test_model(model, x_test):
    """prediction_test_model"""
    y_pred_RF_testeo = model.predict(x_test)
    return y_pred_RF_testeo


def forecasts(y_pred_RF_testeo, y_test, data):
    """forecasts"""
    df_model = pd.DataFrame(y_test).reset_index(drop=True)
    df_model['pronostico'] = y_pred_RF_testeo

    np.random.seed(0)

    df_series = pd.Series(y_test)
    df_series = df_series.to_frame()
    df_series.reset_index(inplace=True)
    df_series = df_series[['index']]
   

    df_model = pd.concat([df_model, df_series], axis=1)

    data = data[['fecha']]
    data.reset_index(inplace=True)

    df_model = pd.merge(df_model, data, on='index', how='left')
    df_model = df_model[['fecha', 'precio', 'pronostico']]
    return df_model


def save_forecasts(df_model, outfile):
    """"save_forecasts"""
    df_model.to_csv(outfile, index=None)


def make_forecasts():
    """make_forecasts"""
    try:
        infile = "src/models/precios-diarios.pickle"
        outfile = 'data_lake/business/forecasts/precios-diarios.csv'
        data = load_data()
        x, y = transform_data(data)
        x_train, x_test, y_train, y_test = make_train_test_set(x, y)
        model = load_pkl(infile)
        scores = score(x_train, y_train, x_test, y_test, model)
        estimador_n = best_score(scores)
        model = trein_model_with_best_estimator(
            estimador_n, x_train, y_train)
        y_pred_RF_testeo = prediction_test_model(model, x_test)
        df_model = forecasts(y_pred_RF_testeo, y_test, data)
        save_forecasts(df_model, outfile)
    except:
        raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_forecasts()
    
