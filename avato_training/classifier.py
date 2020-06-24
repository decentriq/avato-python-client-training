import numpy as np


class LogisticRegressionClassifier():

    """params: A dict from class-label to class-specific model parameters"""
    def __init__(self, params):
        self.params = params

    def _sigmoid(self, a):
        a = max(-100, min(100, a))  # bound exponential to avoid overflow
        return 1/(1 + np.exp(-a))

    """Compute the probability of x belonging to class_label."""
    def _predict_single_class(self, x, class_label):
        model_params = self.params[class_label]
        a = np.dot(x.flatten(), model_params.flatten())
        return self._sigmoid(a)

    """Compute the class label of x"""
    def predict_single(self, x):
        single_class_predictions = {
            cl: self._predict_single_class(x, cl)
            for cl in self.params.keys()
        }
        p_max = -1
        cl_max = ""
        for cl, p in single_class_predictions.items():
            if p > p_max:
                p_max = p
                cl_max = cl
        return cl_max

    """Compute all class labels of X"""
    def predict(self, X):
        return np.array([
            self.predict_single(X[ir:ir+1, :])
            for ir in range(X.shape[0])
        ])

