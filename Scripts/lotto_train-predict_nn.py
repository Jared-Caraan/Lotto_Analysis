import pandas as pd
import numpy as np
import logging
import joblib

from sklearn.preprocessing import MinMaxScaler, LabelEncoder, OneHotEncoder
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, InputLayer
from keras.optimizers import Adadelta, SGD
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.preprocessing import LabelEncoder
from config import *

## LOGGER CONFIG
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(train_log)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def train(df, col, out):
    
    # X and Y
    X = df.drop([col, 'Day_Name'], axis = 1)
    y = df[col]
    y = y.to_numpy()
    
    encoder = LabelEncoder()
    encoded_Y = encoder.fit_transform(y)
    dummy_y = np_utils.to_categorical(encoded_Y)
    
    # DATA SPLIT
    X_train, X_test, y_train, y_test = train_test_split(X, dummy_y, test_size = test_size, random_state = rand_state)

    # SCALER
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test  = scaler.transform(X_test)
    
    # MODEL
    model = Sequential()
    model.add(InputLayer(input_shape=(X_train.shape[1], )))
    model.add(Dense(100, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(out, activation='softmax'))
    optimizer = Adadelta(learning_rate = lr_nn, rho = rho_nn, epsilon = eps_nn)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    history = model.fit(X_train, y_train, epochs = epoch_nn, batch_size = batch_nn, validation_data = (X_test, y_test))
    
    # SCORE
    scores = model.evaluate(X_test, y_test, batch_size = batch_nn)
    acc_nn  = scores[1] * 100
    logger.debug("Loss" + " (" + col + ")" + ": " + str(scores[0]))
    logger.debug("Accuracy" + " (" + col + ")" + ": " + str(acc_nn))
    
    scaler_file = scaler_num + "_{}.pkl".format(col)
    model_file  = model_num + "_{}.pkl".format(col)
    le_y_file   = le_y + "_{}.pkl".format(col)
    
    # PICKLES
    try:
        joblib.dump(scaler, scaler_file)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug("Saving scaler" + " (" + col + ")")
    
    try:
        model.save(model_num)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug("Saving model" + " (" + col + ")")
        
    try:
        joblib.dump(encoder ,le_y_file)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug("Saving label encoder for Y" + " (" + col + ")")

def main():
    
    for i in range(0, len(col_list)):
    
        logger.debug("Training " + str(col_list[i]))
        
        # DATA
        try:
            df = pd.read_excel(filename_all)
        except Exception as e:
            logger.critical("Exception: " + str(e))
        
        # FEATURES
        df['Date']  = pd.to_datetime(df['Date'], format = '%d/%m/%Y')

        df['Month'] = df['Date'].dt.strftime('%m')
        df['Month'] = df['Month'].apply(lambda x: int(x))
        
        df['Day'] = df['Date'].dt.strftime('%d')
        df['Day'] = df['Day'].apply(lambda x: int(x))

        df['Week'] = df['Date'].dt.isocalendar().week
        df['Week'] = df['Week'].apply(lambda x: int(x))

        df['week_cos'] = np.cos(2 * np.pi * df['Week'] / 7)
        df['week_sin'] = np.sin(2 * np.pi * df['Week'] / 7)

        df['month_cos'] = np.cos(2 * np.pi * df['Month'] / 12)
        df['month_sin'] = np.sin(2 * np.pi * df['Month'] / 12)

        df['day_cos'] = np.cos(2 * np.pi * df['Day'] / 31)
        df['day_sin'] = np.sin(2 * np.pi * df['Day'] / 31)
        
        df = df[['Day_Name', 'week_cos', 'week_sin', col_list[i]]]
        
        labelencoder = LabelEncoder()
        df['Day_Name'] = labelencoder.fit_transform(df['Day_Name'])

        ohe = OneHotEncoder()
        ohe_df = pd.DataFrame(ohe.fit_transform(df[['Day_Name']]).toarray())
        ohe_df.columns = ohe.get_feature_names()
        ohe_df = ohe_df.astype(int)

        df = df.join(ohe_df)

        output_neuron = len(df[col_list[i]].unique())
        
        le_day_file = le_day + "_{}.pkl".format(col_list[i])
        ohe_file    = ohe_num + "_{}.pkl".format(col_list[i])
        
        try:
            joblib.dump(labelencoder, le_day_file)
        except Exception as e:
            logger.critical("Exception: " + str(e))
        else:
            logger.debug("Saving label encoder for day name" + " (" + str(col_list[i]) + ")")
        
        try:
            joblib.dump(ohe, ohe_file)
        except Exception as e:
            logger.critical("Exception: " + str(e))
        else:
            logger.debug("Saving one hot encoder" + " (" + str(col_list[i]) + ")")
        
        train(df, str(col_list[i]), output_neuron)
    
if __name__ == "__main__":
    main()