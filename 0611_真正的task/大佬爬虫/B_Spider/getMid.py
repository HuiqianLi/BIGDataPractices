import os
import pandas as pd

def read_csv(path):
    df = pd.read_csv(path)
    up_dict = dict(df)
    return up_dict