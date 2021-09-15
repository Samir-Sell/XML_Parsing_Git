import pandas as pd


def convert_list_dict(list_dict):
    df = pd.DataFrame(list_dict)
    print(df)
    return(df)