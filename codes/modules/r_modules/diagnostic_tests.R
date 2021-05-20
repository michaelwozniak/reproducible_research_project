library(olsrr)
library(lmtest)


diagnostic_tests <- function(model) {
  
  cat("VIF for collinearity of variables:\n\n")
  print(ols_coll_diag(model)[1]$vif_t)
  
  cat("\n\n\nKolmogorov-Smirnov for normality:\n")
  print(ols_test_normality(model)[1]$kolmogorv)
  
  cat("\n\n\nRESET test for correct specification:\n")
  print(resettest(model, power=2:3, type="fitted"))
  
  cat("\n\n\nBreusch-Pagan test for homogeneity:\n")
  print(bptest(model, studentize=TRUE))
  
  cat("\n\n\nDurbin-Watson test for autocorrelation:\n")
  print(dwtest(model))
}