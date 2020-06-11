import numpy as np

class LogisticRegressionClassifier():

    '''params: A dict from class-label to class-specific model parameters'''
    def __init__(self, params):
        self.params = params

    def sigmoid(self, a):
        return 1/(1 + np.exp(-a))

    def predict_single_class(self, x, class_label):
        model_params = self.params[class_label]
        a = np.dot(x.flatten(), model_params.flatten())
        return self.sigmoid(a)

    def predict_single(self, x):
        single_class_predictions = {
            cl: self.predict_single_class(x, cl)
            for cl in self.params.keys()
        }
        p_max = -1
        cl_max = ""
        for cl, p in single_class_predictions.items():
            if p > p_max:
                p_max = p
                cl_max = cl
        return cl_max

    def predict(self, X):
        y_hat = np.array([
            self.predict_single(X[ir:ir+1, :])
            for ir in range(X.shape[0])
        ])
        return y_hat
