setwd("~/Code/nmis_data_for_bamboo/data")

myDropCols <- function(df) {
  df$X <- NULL
  df$lga <- NULL
  df$state <- NULL
  df$zone <- NULL
  df
}

hl <- myDropCols(read.csv("Health_LGA.csv", stringsAsFactors=FALSE))
el <- myDropCols(read.csv("Education_LGA.csv", stringsAsFactors=FALSE))
wl <- myDropCols(read.csv("Water_LGA.csv", stringsAsFactors=FALSE))
lgas <- read.csv("~/Dropbox/Nigeria/Nigeria 661 Baseline Data Cleaning/lgas.csv")


all <- merge(lgas, merge(merge(hl, el, by="lga_id"), wl, by="lga_id"), by="lga_id")
write.csv(all, "LGA_Data.csv")

