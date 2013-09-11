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
ex <- myDropCols(read.csv("External_Data.csv", stringsAsFactors=FALSE))
lgas <- read.csv("~/Dropbox/Nigeria/Nigeria 661 Baseline Data Cleaning/lgas.csv")

outputIfLgaIDDuplicated <- function(df) {
  if(anyDuplicated(df$lga_id)) {
    cat(paste("\n\n~~~~~ERROR~~~~~\n DUPLICATED LGA_IDs:"),
        paste(df[duplicated(df$lga_id), 'lga_id'], collapse=" "),
        "\n\n")
  }
}
errs <- lapply(list(hl, wl, el, ex), outputIfLgaIDDuplicated)
if(is.null(unlist(errs))) stop()

mmerge <- function(x, y) {
  merge(x, y, by="lga_id", all=T)
}

myfmerge <- function(left, right){
    merge(x = left, y = right, by="lga_id", all.x=T)
}

all <- mmerge(lgas, mmerge(ex, mmerge(wl, mmerge(hl, el))))
write.csv(all, "LGA_Data.csv")
