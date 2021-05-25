# Reproducible Research project of the working paper **Institutional Underpinnings and Democracy Backsliding in the Perspective of COVID-19**

### Requirements/Instalation
#### How to install python dependencies:
pip install -r py_requirements.txt

#### How to install R dependencies:
install.packages(scan(file = "r_requirements.txt", what = character()))

### Project tree
```
|-- README.md
|-- codes
|   |-- _init_.py
|   |-- experiments
|   |   |-- _init_.py
|   |   |-- main_research
|   |   |   |-- 1_data_merging_and_cleaning.ipynb
|   |   |   |-- 2_ols_regression.ipynb
|   |   |   |-- 3_catboost_regression.ipynb
|   |   |   |-- 4_random_forest_regression.ipynb
|   |   |   |-- _init_.py
|   |   |   `-- catboost_info
|   |   `-- robustness_check
|   |       |-- 1_data_merging_and_cleaning.ipynb
|   |       |-- 2_ols_regressions.ipynb
|   |       |-- 3_catboost_regression.ipynb
|   |       |-- 4_random_forest_regression.ipynb
|   |       |-- _init_.py
|   |       `-- catboost_info
|   `-- modules
|       |-- _init_.py
|       |-- py_modules
|       |   |-- _init_.py
|       |   |-- ale.py
|       |   |-- feature_engineering.py
|       |   |-- ml_models_training.py
|       |   `-- xai_wrapper.py
|       `-- r_modules
|           |-- diagnostic_tests.R
|           `-- feature_engineering.R
|-- data
|   |-- main_research
|   |   |-- processed_data
|   |   `-- raw_data
|   `-- robustness_check
|       |-- processed_data
|       `-- raw_data
|-- py_requirements.txt
|-- r_requirements.txt
`-- results
    |-- main_research
    |   |-- catboost
    |   |-- ols_regression
    |   `-- random_forest
    `-- robustness_check
        |-- catboost
        |-- ols_regression
        |   |-- main_tables
        |   |-- robustness_collinearity
        |   |-- robustness_missings
        |   `-- robustness_time_periods
        `-- random_forest
```

### Project description
We created a project based on the article ["Institutional Underpinnings and Democracy Backsliding in the Perspective of COVID-19"](https://www.researchgate.net/publication/351692275_Institutional_Underpinnings_and_Democracy_Backsliding_in_the_Perspective_of_COVID-19_Authors) and the poster ["A study of Democracy Backsliding in the Perspective of COVID-19 using econometrics and machine learning approaches"](https://www.researchgate.net/publication/351692152_A_study_of_Democracy_Backsliding_in_the_Perspective_of_COVID-19_using_econometrics_and_machine_learning_approaches) by PhD Jacek Lewkowicz, Michał Woźniak and Michał Wrzesiński. Originally we investigated the drivers of the impact of the political decisions, as a response to the COVID-19 pandemic. We used a novel global dataset covering the period of the first wave of the pandemic (March-June 2020), which included the variables that we used as dependent variables. In these studies, we applied various econometric and machine learning tools.

The main goals of the reproducible project are:
- reproduction of the initial results
- improvement of the study by performing robustness checks
- structuring the project
- clean and readable code for reproducibility
- combination of the research methodology developed as a part of a scientific article and a poster from conference MLinPL

### Project structure description
We divide our project into three main folders.
1) In `code` folder you can find `experiments` and `modules`. Folder `modules` contains python and R classes and functions. Folder `experiments` is divided into two subfolders: `main_research` and `robustness_check`. Folder `main_research` contains files that were created during original research. In turn, folder `robustness_check` contains files, that are reproduced by us with new dependent variables (updated by the authors for a longer time range).
2) In `data` folder you can find two subfolders for main research and robustness check. In `main_research`, folder `raw_data` contains initial files that were used to create database. In turn, `processed_data` contains `final_dataset.csv` that is our main dataset for initial study. Analogously, `robustness_check` folder has two subfolders for raw data and processed data. `raw_data` contains final dataset from main research, new dataset for dependent variables and dataset for covid data. Folder `processed data` contains four processed files: `final_dataset_all` for new time range (March-December 2020) and minor datasets for three subperiods (March-June 2020, July-September 2020 and October-December 2020). In both `raw_data` folders for main research and robustness check you can find `variables_description.md` files with short description of databases/variables.
3) In `result` folder, again you can find two subfolders for main research and robustness check. Both of them contains results for OLS regression, Random Forest and CatBoost. In the case of OLS regressions for `main_research` there are two tables for main regressions. For `robustness_check` we have division into four folders: `main_tables` (reproduced tables from main research with new dependent variables), `robustness_time_periods`, `robustness_collinearity` and `robustness_missings`. All above mentioned folders contains tables with regression results for various specifications. In the case of Random Forest and CatBoost, both `main_research` and `robustness_check` folders contain analogous files: results for Permutation Importance, SHAP summary plots, Partial Dependence Plots (1 dimensional and 2 dimensional) and Accumulated Local Effects plots (1 dimensional and 2 dimensional).

