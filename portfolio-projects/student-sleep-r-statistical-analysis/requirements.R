packages <- c(
  "flextable",
  "knitr",
  "clickR",
  "mice",
  "ggplot2",
  "reshape2",
  "car",
  "MASS",
  "gridExtra",
  "scales",
  "rmarkdown"
)

install.packages(setdiff(packages, rownames(installed.packages())))
