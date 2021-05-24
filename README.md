# Reproducible Research project of the working paper **Institutional Underpinnings and Democracy Backsliding in the Perspective of COVID-19**

## Requirements/Instalation
#### How to install python dependencies:
pip install -r py_requirements.txt

#### How to install R dependencies:
install.packages(scan(file = "r_requirements.txt", what = character()))

### Project tree
```bash
└───reproducible_research_project
    │   py_requirements.txt
    │   r_requirements.txt
    │
    └───codes
        │   __init__.py
        │
        └───experiments
            └───main_research
                |    catboost_info
                |    .gitkeep
                │    1_data_merging_and_cleaning.ipynb
                │    2_ols_regression.ipynb
                │    3_catboost_regression.ipynb
                │    4_random_forest_regression.ipynb
                │    __init__.py
             └───robustness_check
                |    catboost_info
                |    .gitkeep
                │    1_data_merging_and_cleaning.ipynb
                │    2_ols_regression.ipynb
                │    3_catboost_regression.ipynb
                │    4_random_forest_regression.ipynb
                │    __init__.py
        └───modules
             └───py_modules
                |    __py_cache__
                |    __init__.py
                |    ale.py
                |    feature_engineering.py
                |    ml_models_training.py
                |    xai_wrapper.py
                └───r_modules
                    |    diagnostic_tests.R
                    └─── feature_engineering.R
        

```
