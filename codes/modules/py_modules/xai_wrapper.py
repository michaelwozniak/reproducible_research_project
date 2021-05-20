from typing import Union
import os
import sys
import pathlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import inspection
from catboost import CatBoostRegressor
from sklearn.ensemble import RandomForestRegressor
import shap
from pdpbox import pdp
from .ale import ale_plot

class XAI_analysis():
    '''
    The class allows to create, display and save figures of: permutation importance plot, shap summary plot, partial dependence plot 1d, partial dependence plot 2d, 
    accumulated local effects 1d, accumulated local effects 2d.
    
    Attributes
    ----------
    model : Union[CatBoostRegressor, RandomForestRegressor]
        trained model
    df : pd.DataFrame
        dataframe used to train model
    target: str
        endogenous variables used to train model
    features: list
        exogenous variables used to train model 
    path: str
        directory to save file plot
    shap_usage: bool
        whether shap will be used
    run_all_plots: bool
        whether run all xai plots
    x_of_interest: str
        exogenous variables for 1d pdp and ale plot
    xs_of_interest: list
        exogenous variables for 2d pdp and ale plot
    '''
    def __init__(self, model: Union[CatBoostRegressor, RandomForestRegressor], df: pd.DataFrame, target: str, features: list, 
                 path: str, shap_usage: bool = True, run_all_plots: bool = False, x_of_interest: str = None, xs_of_interest: list = None):
        self.model = model
        self.df = df
        self.target = target
        self.features = features
        self.path = path
        self.x_of_interest = x_of_interest
        self.xs_of_interest = xs_of_interest
        self.__X = df[features]
        self.__y = df[target]
        if shap_usage == True or run_all_plots == True:
            shap_explainer = shap.TreeExplainer(model)
            self.__shap_values = shap_explainer.shap_values(self.__X)
        if (x_of_interest == None and run_all_plots == True) or (xs_of_interest == None and run_all_plots == True):
            raise Exception("You have to declare x_of_interest and xs_of_interest to run all plots")
        if run_all_plots == True:
            self.__run_all_plots()
        
    def permutation_importance_plot(self):
        result = inspection.permutation_importance(self.model, self.__X, self.__y, n_repeats=10, random_state=2021, n_jobs=-1)
        sorted_idx = result.importances_mean.argsort()[-15:][::-1]
        results_sorted = pd.DataFrame(result.importances[sorted_idx].T, columns=self.__X.columns[sorted_idx].tolist())
        results_sorted_melted = pd.melt(results_sorted, var_name='Variable', value_name='Importance')

        sns.set(font_scale = 1, style="white")
        sns.set_palette("Blues")
        fig, ax = plt.subplots(figsize=(5,5))
        sns.boxplot(x="Importance", y="Variable", data=results_sorted_melted)
        ax.set_ylabel('')    
        plt.title(f"Permutation importance for {self.target} model", fontsize = 15)
        plt.savefig(f"{self.path}/permutation_importance_plot_of_{self.target}.png", bbox_inches='tight', dpi=500)
        plt.show()

    def shap_summary_plot(self):
        shap.summary_plot(self.__shap_values, self.__X, feature_names=self.__X.columns.tolist(), plot_size=(5,5), show=False)
        plt.title(f"SHAP Summary Plot for {self.target} model\n", fontsize = 14)
        plt.savefig(f"{self.path}/summary_plot_of_{self.target}.png", bbox_inches='tight', dpi=500)
        plt.show()
        
    def pdp_1d_plot(self):
        fig, ax, = plt.subplots(nrows=1, ncols=1, figsize=(4,4))
        shap.dependence_plot(self.x_of_interest, self.__shap_values, self.__X, interaction_index=None, ax = ax, dot_size=20, show=False)
        plt.title(f"SHAP Dependence plots for {self.x_of_interest} \nwith {self.target} as dependent variable", fontsize=14)
        plt.savefig(f"{self.path}/pdp_1d_{self.target}_vs_{self.x_of_interest}.png", bbox_inches='tight', dpi=500)
        plt.show()

    def ale_1d_plot(self):
        plt.rc("figure", figsize=(7, 7))
        ale_plot(self.model, self.__X, self.x_of_interest, bins=15, monte_carlo=True)
        plt.savefig(f"{self.path}/ale_1d_{self.target}_vs_{self.x_of_interest}.png", bbox_inches='tight', dpi=500)
        plt.show()
        
    def pdp_2d_plot(self):
        inter1 = pdp.pdp_interact(model=self.model, dataset=self.__X, model_features=self.features, features=self.xs_of_interest)
        plt.rc("figure", figsize=(7, 7))
        pdp.pdp_interact_plot(pdp_interact_out=inter1, feature_names=self.xs_of_interest, 
                              plot_params={"subtitle":"", "title":f"PDP interact for {self.xs_of_interest[0]} and {self.xs_of_interest[1]} - {self.target} model"})
        plt.savefig(f"{self.path}/pdp_2d_{self.target}_vs_{self.xs_of_interest[0]}_and_{self.xs_of_interest[1]}.png", bbox_inches='tight', pad_inches=0)
        plt.show()
        
    def ale_2d_plot(self):
        plt.rc("figure", figsize=(10, 10))
        ale_plot(self.model, self.__X, self.xs_of_interest, bins=15, monte_carlo=True, monte_carlo_rep=100)
        plt.savefig(f"{self.path}/ale_2d_{self.target}_vs_{self.xs_of_interest[0]}_and_{self.xs_of_interest[1]}.png")
        plt.show()
        
    def __run_all_plots(self):
        self.permutation_importance_plot()
        self.shap_summary_plot()
        self.pdp_1d_plot()
        self.ale_1d_plot()
        self.pdp_2d_plot()
        self.ale_2d_plot()