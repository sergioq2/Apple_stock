import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras
from preprocessing import feature_engineering

def neural_network(X_train, y_train, X_test, y_test):
    window_size = 2
    model = Sequential()
    model.add(LSTM(5, activation='relu',
                input_shape=(window_size,1),
                return_sequences=False))
    model.add(Dense(1))
    optimizer = keras.optimizers.Adam(learning_rate=0.001)
    model.compile(loss='mse', optimizer=optimizer)
    model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=6, epochs=80)

    train_predict = model.predict(X_train).flatten()
    test_predict = model.predict(X_test).flatten()

    training_error = model.evaluate(X_train, y_train, verbose=0)

    testing_error = model.evaluate(X_test, y_test, verbose=0)
    return model 

def save_model(model):
    model.save('../application/trained_model.h5')
    print("Model saved successfully!")

def compile():
    X_train, y_train, X_test, y_test = feature_engineering()
    model = neural_network(X_train, y_train, X_test, y_test)
    save_model(model)

if __name__ == '__main__':
    compile()
