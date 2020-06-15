import numpy as np
import pandas as pd

data_filenames = ("test-data/wine-dataowner1.csv", "test-data/wine-dataowner2.csv")

analyst_credentials = ("***REMOVED***", "***REMOVED***")
dataowner1_credentials = ("***REMOVED***", "***REMOVED***")
dataowner2_credentials = ("***REMOVED***", "***REMOVED***")

def load_data():
    Xy = np.array(
        pd.concat([
            pd.read_csv(data_filenames[0]),
            pd.read_csv(data_filenames[1])
        ])
    );
    X = Xy[:,0:-1]
    y = Xy[:,-1]
    return X, y

def compute_accuracy(classifier, X, y):

    y_hat = classifier.predict(X)
    assert len(y) == len(y_hat)
    n = len(y)
    n_eq = 0
    for yi, yi_hat in zip(y, y_hat):
        if float(yi) == float(yi_hat):
            n_eq = n_eq + 1
    accuracy = float(n_eq)/n
    return accuracy