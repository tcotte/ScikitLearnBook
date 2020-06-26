from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class WealthToInt(BaseEstimator, TransformerMixin):
    def __init__(self, feature_names):
        self._feature_names = feature_names

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        for column in self._feature_names:
            X[column] = X[column].str.replace('€', '')
            X[column] = X[column].str.replace('K', '')
            X[column] = X[column].str.replace('M', '000')
            X[column] = pd.to_numeric(X[column])
        return X
