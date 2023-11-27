import pandas as pd
import numpy as np
import sys 
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
import plotly.express as px
import itertools
from lightgbm import LGBMClassifier

from joblib import Parallel, delayed

import pickle

from abc import abstractmethod, ABC




with open('test_tuple.pkl', 'rb') as file:
    loaded_tuple = pickle.load(file)

class TestingSampler(ABC):
    def __init__(self):

        self.testing_data = loaded_tuple[0]
        self.testing_truths = loaded_tuple[1]
        self.sample_length = len(loaded_tuple[0])

    def update_seed(self):
        np.random.seed(np.random.randint(2,200000))

    
    #sample from the length of testing data
    def get_sample(self):
        sample_int = np.random.choice(self.sample_length, replace=False)
        self.sample = (self.testing_data[sample_int], self.testing_truths[sample_int])
        return self.sample

        