import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import FeatureUnion, Pipeline


class FeatureDropper(BaseEstimator, TransformerMixin):
    def __init__(self, features_names):
        self._features_names = features_names

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = X.drop(self._features_names, axis=1)
        return X


# Custom Transformer that extracts columns passed as argument to its constructor
class FeatureSelector(BaseEstimator, TransformerMixin):
    # Class Constructor
    def __init__(self, feature_names):
        self._feature_names = feature_names

        # Return self nothing else to do here

    def fit(self, X, y=None):
        return self

        # Method that describes what we need this transformer to do

    def transform(self, X, y=None):
        return X[self._feature_names]


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
