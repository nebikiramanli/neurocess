import json
import pandas as pd


def read_pickle_file(file_name):
    """
    Reads a pickle file and returns a dataframe
    """
    data = pd.read_pickle(file_name)
    return data


def read_json_file(file_name):
    """
    Reads a json file and returns a dataframe
    """
    data = json.load(open(file_name))
    return data
