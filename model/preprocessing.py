import numpy as np 

#! git clone https://bitbucket.org/botiaio/campusparty_applestock.git

dataset = np.loadtxt('../campusparty_applestock/normalized_apple_prices.csv')

def window_transform_series(series,window_size):
    X = []
    y = []
    for a,_ in enumerate(series):
      if len(series) - a > window_size:
        b = a + window_size
        X.append(series[a:b])
        y.append(series[b])

    X = np.array(X)
    y = np.array(y)
    return X,y

def feature_engineering():
    test_series = dataset
    window_size = 2
    X,y = window_transform_series(test_series,window_size)

    train_test_split = round(len(X)*(2/3))

    X_train = X[:train_test_split]
    y_train = y[:train_test_split]

    X_test = X[train_test_split:]
    y_test = y[train_test_split:]

    X_train = np.asarray(np.reshape(X_train, (X_train.shape[0], window_size, 1)))
    X_test = np.asarray(np.reshape(X_test, (X_test.shape[0], window_size, 1)))
    return X_train, y_train, X_test, y_test


if __name__ == '__main__':
    feature_engineering()
   
   

