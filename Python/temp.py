# -*- coding: utf-8 -*-
"""
Script for generating dcat xml from spreadsheet.
"""

# import numpy
import pandas
# import csv
from string import Template
# import xml.etree.cElementTree as ET

dataset = pandas.read_csv("H:\Dokument\Git_repos\open_data\metadata.csv", 
                          sep = ";")
#dataset
#dataset["Value"]

# read in template parts
with open('H:\Dokument\Git_repos\open_data\dcat_xml\catalog_dev_pt1.xml', 'r') as myfile:
    start_template=myfile.read().replace('\n', '');
    
# read in template parts
with open('H:\Dokument\Git_repos\open_data\dcat_xml\catalog_dev_pt2.xml', 'r') as myfile:
    end_template=myfile.read().replace('\n', '');


# file_link = link to file resource

#s = Template('$when, $who $action $what.') 
#s.substitute(when='In the summer', who='John', action='drinks', what='iced tea') 

# substitute in 
temp = Template(end_template)

dataframes = ""

# loop over all rows in metadata
for i in range(0, len(dataset)):
    dataframe = temp.substitute(nr = dataset.iloc[i]["nr"],
                                    namn = dataset.iloc[i]["namn"],
                                    forklaring = dataset.iloc[i]["forklaring"],
                                    utgiven = dataset.iloc[i]["utgiven"],
                                    uppdaterad = dataset.iloc[i]["uppdaterad"],
                                    dcatnr = dataset.iloc[i]["dcatnr"],
                                    distribution = dataset.iloc[i]["distribution"],
                                    landing = dataset.iloc[i]["landing"],
                                    conforms_to = dataset.iloc[i]["conforms_to"],
                                    datanr = dataset.iloc[i]["datanr"],
                                    fil_lank = dataset.iloc[i]["fil_lank"],
                                    filformat = dataset.iloc[i]["filformat"],
                                    fromdatum = dataset.iloc[i]["fromdatum"],
                                    tomdatum = dataset.iloc[i]["tomdatum"])
        
    dataframes = dataframes + dataframe

# assemble metadata
out = start_template + dataframes + "</rdf:RDF>"

# write catalogue
file = open("H:\Dokument\Git_repos\open_data\catalog_out.xml","w") 
file.write(out)
file.close()