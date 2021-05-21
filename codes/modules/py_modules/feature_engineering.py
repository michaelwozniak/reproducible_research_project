import pandas as pd
import numpy as np

def initial_transformations(df: pd.DataFrame) -> pd.DataFrame:
    '''
    The method allows to prepare dataset to further machine learning analysis
    
    Attributes
    ----------
    df : pd.DataFrame
        dataframe of interest
    '''
    df = df.copy()
    df["gini_log"] = np.log(df.gini)
    df["education_log"] = np.log(df.education)
    df["gdp_pc_log"] = np.log(df.gdp_pc)
    df["trade_gdp_log"] = np.log(df.trade_gdp)
    df["density_log"] = np.log(df.density)
    df["region_geo"] = 'reg_' + df["region_geo"].astype(str)    
    return df
    