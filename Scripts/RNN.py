import pandas as pd
import numpy as np
import keras
import logging
import plotly.graph_objects as go

from keras.preprocessing.sequence import TimeseriesGenerator
from keras.models import Sequential
from keras.layers import LSTM, Dense
from config import filename_excel, predict_log, look_back, epoch, num_prediction

## LOGGER CONFIG
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(predict_log)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def rnn_model(look_back, epoch, train, test):
    train_generator = TimeseriesGenerator(train, train, length=look_back, batch_size=20)
    
    model = Sequential()
    model.add(
        LSTM(10,
            activation='sigmoid',
            input_shape=(look_back,1))
    )
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse', metrics=['acc'])

    model.fit_generator(train_generator, epochs=epoch, verbose=1)
    
    return model
    
def predict(num_prediction, model, lotto_data):
    prediction_list = lotto_data[-look_back:]
    
    for _ in range(num_prediction):
        x = prediction_list[-look_back:]
        x = x.reshape((1, look_back, 1))
        out = model.predict(x)[0][0]
        prediction_list = np.append(prediction_list, out)
    prediction_list = prediction_list[look_back-1:]
    
    return prediction_list

def predict_dates(num_prediction):
    last_date = df['Date'].values[-1]
    prediction_dates = pd.date_range(last_date, periods=num_prediction+1).tolist()
    return prediction_dates


def main():
    cols = [ 'first', 'second', 'third', 'fourth', 'fifth', 'sixth' ]
    combination = []
    
    try:
        df = pd.read_excel(filename_excel)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug("Reading historical data")
    
    ## DATA TRANSFORMATION
    df.drop(columns=['Unnamed: 0'], inplace=True)
    df.drop(columns=['Winning Numbers'], inplace=True)
    
    df['Date'] = pd.to_datetime(df['Date'], format = '%d/%m/%Y')
    
    filt = df['Date'] >= df['Date'].max() - pd.DateOffset(months=6)
    df_year = df[filt]
    df = df_year.copy()
    
    df = df.sort_values(by=['Date']).reset_index(drop=True)
    df.set_axis(df['Date'], inplace=True)
    
    for i in cols:
        col_num = df[i].values
        col_num = col_num.reshape((-1,1))

        split = int(0.75*len(col_num))

        col_train = col_num[:split]
        col_test  = col_num[split:]
        
        try:
            model = rnn_model(look_back, epoch, col_train, col_test)
        except Exception as e:
            logger.critical("Exception: " + str(e))
        else:
            logger.debug("Training column " + str(i))
        
        col_num = col_num.reshape((-1))
        
        try:
            forecast = predict(num_prediction, model, col_num)
        except Exception as e:
            logger.critical("Exception: " + str(e))
        else:
            logger.debug("Predicting " + str(i) + " number")
            
        forecast = [ int(round(x)) for x in forecast ]
        
        combination.append(forecast[1])
    
    logger.debug("New winning numbers")
    logger.debug(combination)
    print(combination)
    
if __name__ == "__main__":
    main()
