library(whisker)
library(magrittr)


template <- 
readLines("sandbox_min_template.xml") %>% 
  paste(collapse = "\n")
  
PM_katalog <- "Pensionsmyndighetens datakatalog"
Katalogbeskrivning <- "Katalogen innehåller information om det svenska pensionssystemet, tillhandahållna av Pensionsmyndigheten"
Organisationsnamn <- "Pensionsmyndigheten"
Datasetnamn <- "Utbetalningar bostadstillägg dec 2015"
Dataset_beskrivning <- "Utbetalade belopp under decembermånad 2015. Geografisk koppling till kommun tillhandahålls i övrigt är data helt avidentifierat"

out <- whisker.render(template)



meta_xlsx <- data.frame(
  PM_katalog = "Pensionsmyndighetens datakatalog",
  Katalogbeskrivning = "Katalogen innehåller information om det svenska pensionssystemet, tillhandahållna av Pensionsmyndigheten",
  Organisationsnamn = "Pensionsmyndigheten",
  Datasetnamn  = "Utbetalningar bostadstillägg dec 2015",
  Dataset_beskrivning = "Utbetalade belopp under decembermånad 2015. Geografisk koppling till kommun tillhandahålls i övrigt är data helt avidentifierat"
)

out <- whisker.render(template, meta_xlsx)

writeLines(out, "output.xml")

