import pandas as pd
from catboost import CatBoostRegressor
from catboost import Pool
from catboost import cv
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

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
    return {"model":model, "params":grid_search_result["params"]}

def random_forest_model(df: pd.DataFrame, target: str, features: list) -> RandomForestRegressor:
    '''
    The method allows to train Random Forest model with hyperparameters tuning in the grid search. 
    
    Attributes
    ----------
    df : pd.DataFrame
        dataframe used to train model
    target: str
        endogenous variables used to train model
    features: list
        all exogenous variables used to train model
    '''
    X = df[features]
    y = df[target]
    # find the best possible 'unbiased' model
    model = RandomForestRegressor(random_state=2020)
    grid = { 
    'n_estimators': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'max_features': ['auto', 'sqrt', 'log2'],
    'max_depth' : [2, 3, 4, 5, 6, 7, 8]} 
    grid_search_result = GridSearchCV(model, grid, refit= True, verbose=-1, n_jobs=-1, cv=3) 
    grid_search_result.fit(X, y) 
    
    # infer with above model on the training set 
    model = RandomForestRegressor(**grid_search_result.best_params_, random_state= 2020)
    model = model.fit(X, y)
    print("R^2 of the best model in the grid search on the training set", model.score(X,y))
    return {"model":model, "params":grid_search_result.best_params_}