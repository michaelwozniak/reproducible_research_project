import pandas as pd
from catboost import CatBoostRegressor
from catboost import Pool
from catboost import cv

def catboost_model(df: pd.DataFrame, target: str, features: list, cat_features: list=None) -> CatBoostRegressor:
    '''
    The method allows to train CatBoost model with hyperparameters tuning in the grid search. 
    
    Attributes
    ----------
    df : pd.DataFrame
        dataframe used to train model
    target: str
        endogenous variables used to train model
    features: list
        all exogenous variables used to train model
    cat_features: list
        exogenous categorical variables used to train model
    '''
    X = df[features]
    y = df[target]
    # find the best possible 'unbiased' model
    dataset = Pool(X, y, cat_features=cat_features)
    model = CatBoostRegressor(random_state=2020, verbose=False)
    grid = {'depth': [2, 3, 4, 5, 6],
            'learning_rate': [0.05, 0.1, 0.3, 0.5],
            'iterations': [10, 20, 30, 40, 50, 100]}
    grid_search_result = model.grid_search(grid, X=dataset, cv=3, verbose=False)
    
    # infer with above model on the training set 
    model = CatBoostRegressor(**grid_search_result['params'], verbose=False)
    model.fit(dataset)
    print("R^2 of the best model in the grid search on the training set", model.score(X,y))
    
    return model