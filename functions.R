generate_dcatxml <- function(metadata, outname){
  template <- 
    readLines("sandbox_min_template.xml") %>% 
    paste(collapse = "\n")
  
  
  meta_xlsx <- openxlsx::read.xlsx(metadata)
  
  meta_xlsx<- 
    meta_xlsx %>% 
    spread(Var, Value)
  
  out <- whisker.render(template, meta_xlsx)
  
  writeLines(out, paste0("dcat_xml/", outname,".xml"))
}