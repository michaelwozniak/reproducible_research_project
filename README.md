# Reproducible Research project of the working paper **Institutional Underpinnings and Democracy Backsliding in the Perspective of COVID-19**

## Requirements/Instalation
#### How to install python dependencies:
pip install -r py_requirements.txt

#### How to install R dependencies:
install.packages(scan(file = "r_requirements.txt", what = character()))

### Project tree
```bash
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
|   |   |       |-- catboost_training.json
|   |   |       |-- learn
|   |   |       |   `-- events.out.tfevents
|   |   |       |-- learn_error.tsv
|   |   |       |-- test
|   |   |       |   `-- events.out.tfevents
|   |   |       |-- test_error.tsv
|   |   |       `-- time_left.tsv
|   |   `-- robustness_check
|   |       |-- 1_data_merging_and_cleaning.ipynb
|   |       |-- 2_ols_regressions.ipynb
|   |       |-- 3_catboost_regression.ipynb
|   |       |-- 4_random_forest_regression.ipynb
|   |       |-- _init_.py
|   |       `-- catboost_info
|   |           |-- catboost_training.json
|   |           |-- learn
|   |           |   `-- events.out.tfevents
|   |           |-- learn_error.tsv
|   |           |-- test
|   |           |   `-- events.out.tfevents
|   |           |-- test_error.tsv
|   |           `-- time_left.tsv
|   `-- modules
|       |-- _init_.py
|       |-- py_modules
|       |   |-- __pycache__
|       |   |   |-- ale.cpython-37.pyc
|       |   |   |-- feature_engineering.cpython-37.pyc
|       |   |   |-- ml_models_training.cpython-37.pyc
|       |   |   `-- xai_wrapper.cpython-37.pyc
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
|   |   |   `-- final_dataset.csv
|   |   `-- raw_data
|   |       |-- country_classification_world_bank.xls
|   |       |-- country_location.csv
|   |       |-- export_gdp_world_bank.csv
|   |       |-- fractionalization.xlsx
|   |       |-- gdp_pc_world_bank.csv
|   |       |-- gini_index_world_bank.csv
|   |       |-- import_gdp_world_bank.csv
|   |       |-- inflation_world_bank.csv
|   |       |-- military_world_bank.csv
|   |       |-- mineral_world_bank.csv
|   |       |-- oil_world_bank.csv
|   |       |-- population_density_world_bank.csv
|   |       |-- variables_description.md
|   |       |-- vdem_2019.csv
|   |       `-- vdem_pandem_data_v3.csv
|   `-- robustness_check
|       |-- processed_data
|       |   |-- final_dataset_Q2.csv
|       |   |-- final_dataset_Q3.csv
|       |   |-- final_dataset_Q4.csv
|       |   `-- final_dataset_all.csv
|       `-- raw_data
|           |-- dataset_covid_data.csv
|           |-- dataset_main_research.csv
|           |-- dataset_new_pandem_indexes.csv
|           `-- variables_description.md
|-- py_requirements.txt
|-- r_requirements.txt
`-- results
    |-- main_research
    |   |-- catboost
    |   |   |-- ale_1d_panback_vs_polyarchy.png
    |   |   |-- ale_1d_pandem_dis_vs_polyarchy.png
    |   |   |-- ale_1d_pandem_vs_polyarchy.png
    |   |   |-- ale_2d_panback_vs_polyarchy_and_rule.png
    |   |   |-- ale_2d_pandem_dis_vs_polyarchy_and_rule.png
    |   |   |-- ale_2d_pandem_vs_polyarchy_and_rule.png
    |   |   |-- pdp_1d_panback_vs_polyarchy.png
    |   |   |-- pdp_1d_pandem_dis_vs_polyarchy.png
    |   |   |-- pdp_1d_pandem_vs_polyarchy.png
    |   |   |-- pdp_2d_panback_vs_polyarchy_and_rule.png
    |   |   |-- pdp_2d_pandem_dis_vs_polyarchy_and_rule.png
    |   |   |-- pdp_2d_pandem_vs_polyarchy_and_rule.png
    |   |   |-- permutation_importance_plot_of_panback.png
    |   |   |-- permutation_importance_plot_of_pandem.png
    |   |   |-- permutation_importance_plot_of_pandem_dis.png
    |   |   |-- summary_plot_of_panback.png
    |   |   |-- summary_plot_of_pandem.png
    |   |   `-- summary_plot_of_pandem_dis.png
    |   |-- ols_regression
    |   |   |-- Table_1_regression.html
    |   |   `-- Table_2_regression.html
    |   `-- random_forest
    |       |-- ale_1d_panback_vs_polyarchy.png
    |       |-- ale_1d_pandem_dis_vs_polyarchy.png
    |       |-- ale_1d_pandem_vs_polyarchy.png
    |       |-- ale_2d_panback_vs_polyarchy_and_rule.png
    |       |-- ale_2d_pandem_dis_vs_polyarchy_and_rule.png
    |       |-- ale_2d_pandem_vs_polyarchy_and_rule.png
    |       |-- pdp_1d_panback_vs_polyarchy.png
    |       |-- pdp_1d_pandem_dis_vs_polyarchy.png
    |       |-- pdp_1d_pandem_vs_polyarchy.png
    |       |-- pdp_2d_panback_vs_polyarchy_and_rule.png
    |       |-- pdp_2d_pandem_dis_vs_polyarchy_and_rule.png
    |       |-- pdp_2d_pandem_vs_polyarchy_and_rule.png
    |       |-- permutation_importance_plot_of_panback.png
    |       |-- permutation_importance_plot_of_pandem.png
    |       |-- permutation_importance_plot_of_pandem_dis.png
    |       |-- summary_plot_of_panback.png
    |       |-- summary_plot_of_pandem.png
    |       `-- summary_plot_of_pandem_dis.png
    `-- robustness_check
        |-- catboost
        |   |-- ale_1d_panback_vs_polyarchy.png
        |   |-- ale_1d_pandem_vs_polyarchy.png
        |   |-- ale_2d_panback_vs_polyarchy_and_rule.png
        |   |-- ale_2d_pandem_vs_polyarchy_and_rule.png
        |   |-- pdp_1d_panback_vs_polyarchy.png
        |   |-- pdp_1d_pandem_vs_polyarchy.png
        |   |-- pdp_2d_panback_vs_polyarchy_and_rule.png
        |   |-- pdp_2d_pandem_vs_polyarchy_and_rule.png
        |   |-- permutation_importance_plot_of_panback.png
        |   |-- permutation_importance_plot_of_pandem.png
        |   |-- summary_plot_of_panback.png
        |   `-- summary_plot_of_pandem.png
        |-- ols_regression
        |   |-- main_tables
        |   |   |-- Table_1_regression.html
        |   |   `-- Table_2_regression.html
        |   |-- robustness_collinearity
        |   |   |-- Table_1_regression_collinearity.html
        |   |   `-- Table_2_regression_collinearity.html
        |   |-- robustness_missings
        |   |   |-- Table_1_regression_missings.html
        |   |   `-- Table_2_regression_missings.html
        |   `-- robustness_time_periods
        |       |-- Table_1_regression_Q2.html
        |       |-- Table_1_regression_Q3.html
        |       |-- Table_1_regression_Q4.html
        |       |-- Table_2_regression_Q2.html
        |       |-- Table_2_regression_Q3.html
        |       `-- Table_2_regression_Q4.html
        `-- random_forest
            |-- ale_1d_panback_vs_polyarchy.png
            |-- ale_1d_pandem_vs_polyarchy.png
            |-- ale_2d_panback_vs_polyarchy_and_rule.png
            |-- ale_2d_pandem_vs_polyarchy_and_rule.png
            |-- pdp_1d_panback_vs_polyarchy.png
            |-- pdp_1d_pandem_vs_polyarchy.png
            |-- pdp_2d_panback_vs_polyarchy_and_rule.png
            |-- pdp_2d_pandem_vs_polyarchy_and_rule.png
            |-- permutation_importance_plot_of_panback.png
            |-- permutation_importance_plot_of_pandem.png
            |-- summary_plot_of_panback.png
            `-- summary_plot_of_pandem.png

```
