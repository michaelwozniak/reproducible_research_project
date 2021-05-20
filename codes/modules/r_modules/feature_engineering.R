library(fastDummies)

initial_transformations <- function(dataframe) {
  
  # removing redundant columns
  dataframe$country_text_id <- NULL
  dataframe$continent <- NULL
  dataframe$sub_region <- NULL
  dataframe$region_pol <- NULL
  dataframe$pandem_old <- NULL
  dataframe$pandem_dis_old <- NULL
  dataframe$panback_old <- NULL
  
  # creating dummies
  data <- fastDummies::dummy_cols(dataframe,select_columns = c("income_group","region_geo"),remove_most_frequent_dummy = TRUE, remove_selected_columns = TRUE)
  
  # renaming columns (income categories)
  data <- data %>% rename(
    low_income = 'income_group_Low income',
    lower_middle_income = 'income_group_Lower middle income',
    upper_middle_income = 'income_group_Upper middle income'
  )
  
  # logarithm transformation
  data$gini_log <- log(data$gini) 
  data$density_log <- log(data$density) 
  data$gdp_pc_log <- log(data$gdp_pc) 
  data$trade_gdp_log <- log(data$trade_gdp)
  data$education_log <- log(data$education) 
  
  # square transformation
  data$rule2 <- data$rule * data$rule
  data$polyarchy2 <- data$polyarchy * data$polyarchy
  
  
  return(data)
}