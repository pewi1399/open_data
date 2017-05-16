# -*- coding: utf-8 -*-
"""
Script for generating dcat xml from spreadsheet.
"""

# import numpy
import pandas
# import csv
import io
from string import Template
# import xml.etree.cElementTree as ET

#dataset = pandas.read_csv("H:\Dokument\Git_repos\open_data\metadata.csv", 
#                          sep = ";")
dataset = pandas.read_csv("H:\Dokument\Git_repos\open_data\metadata\metadata.txt", 
                          sep = "\t")

dataset_singles = dataset.query('periodiserad == "nej"')
dataset_multiples = dataset.query('periodiserad == "ja"')
#dataset
#dataset["Value"]

# read in template parts
with open('H:\Dokument\Git_repos\open_data\templates\catalog_dev_pt1.xml', 'r') as myfile:
    start_template=myfile.read().replace('\n', '');
    
with open('H:\Dokument\Git_repos\open_data\templates\catalog_dev_pt2.xml', 'r') as myfile:
    end_template=myfile.read().replace('\n', '');


# substitute in 
temp = Template(end_template)


dataframes = ""

# loop over all rows in metadata
for i in range(0, len(dataset_singles)):
    dataframe = temp.substitute(nr = dataset_singles.iloc[i]["nr"],
                                    namn = dataset_singles.iloc[i]["namn"],
                                    forklaring = dataset_singles.iloc[i]["forklaring"],
                                    utgiven = dataset_singles.iloc[i]["utgiven"],
                                    uppdaterad = dataset_singles.iloc[i]["uppdaterad"],
                                    dcatnr = dataset_singles.iloc[i]["dcatnr"],
                                    distribution = dataset_singles.iloc[i]["distribution"],
                                    landing = dataset_singles.iloc[i]["landing"],
                                    conforms_to = dataset_singles.iloc[i]["conforms_to"],
                                    datanr = dataset_singles.iloc[i]["datanr"],
                                    namn_lank = dataset_singles.iloc[i]["namn_lank"],
                                    forklaring_lank = dataset_singles.iloc[i]["forklaring_lank"],
                                    fil_lank = dataset_singles.iloc[i]["fil_lank"],
                                    filformat = dataset_singles.iloc[i]["filformat"],
                                    fromdatum = dataset_singles.iloc[i]["fromdatum"],
                                    tomdatum = dataset_singles.iloc[i]["tomdatum"])
        
    dataframes = dataframes + dataframe

#------------------------------ multiframes -----------------------------------     
  
with open('H:\Dokument\Git_repos\open_data\templates\catalog_dev_multi_pt1.xml', 'r') as myfile:
    multi_pt1=myfile.read().replace('\n', '');    

with open('H:\Dokument\Git_repos\open_data\templates\catalog_dev_multi_pt2.xml', 'r') as myfile:
    multi_pt2=myfile.read().replace('\n', '');    

with open('H:\Dokument\Git_repos\open_data\templates\catalog_dev_multi_pt3.xml', 'r') as myfile:
    multi_pt3=myfile.read().replace('\n', '');    
  
with open('H:\Dokument\Git_repos\open_data\templates\catalog_dev_multi_pt4.xml', 'r') as myfile:
    multi_pt4=myfile.read().replace('\n', '');    
  
    
# substitute in 
temp_multi_pt1 = Template(multi_pt1)
temp_multi_pt2 = Template(multi_pt2)
temp_multi_pt3 = Template(multi_pt3)
temp_multi_pt4 = Template(multi_pt4)

# loop over multiples
multiframes = ""    
for value in dataset_multiples.namn.unique():
    tmp_data = dataset_multiples.query('namn == @value')
    
    start = temp_multi_pt1.substitute(nr = tmp_data.iloc[0]["nr"],
                                      dcatnr = tmp_data.iloc[0]["dcatnr"],
                                      namn = tmp_data.iloc[0]["namn"],
                                      forklaring = tmp_data.iloc[0]["forklaring"]
                                      )
    middle = ""
    links = ""
    for i in range(0, len(tmp_data)):
        middle_part = temp_multi_pt2.substitute(distribution = tmp_data.iloc[i]["distribution"])
        middle = middle + middle_part
        
        link = temp_multi_pt4.substitute(nr = tmp_data.iloc[i]["nr"],
                                         datanr = tmp_data.iloc[i]["datanr"],
                                distribution = tmp_data.iloc[i]["distribution"],
                                namn_lank = tmp_data.iloc[i]["namn_lank"],
                                forklaring_lank = tmp_data.iloc[i]["forklaring_lank"],
                                fil_lank = tmp_data.iloc[i]["fil_lank"],
                                filformat = tmp_data.iloc[i]["filformat"],
                                fromdatum = tmp_data.iloc[i]["fromdatum"],
                                tomdatum = tmp_data.iloc[i]["tomdatum"])
        links = links + link
        
    end = temp_multi_pt3.substitute(utgiven = tmp_data.iloc[0]["utgiven"],
                                    uppdaterad = tmp_data.iloc[0]["uppdaterad"],
                                    dcatnr = tmp_data.iloc[0]["dcatnr"],
                                    distribution = tmp_data.iloc[0]["distribution"],
                                    landing = tmp_data.iloc[0]["landing"],
                                    conforms_to = tmp_data.iloc[0]["conforms_to"],
                                    datanr = tmp_data.iloc[0]["datanr"])
    
    multiframes = multiframes + start + middle + end + links
    
    
    


# assemble metadata
out = start_template + dataframes + multiframes + "</rdf:RDF>"

#out = out.encode("utf-8")

# write catalogue
#file = open("H:\Dokument\Git_repos\open_data\catalog_out.xml","w") 

with io.open("H:\Dokument\Git_repos\open_data\xml\catalog.xml",'w',encoding='utf8') as f:
    f.write(out)


#file.write("ggggggÖÖÖÖ")
#file.close()