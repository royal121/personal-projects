"""
    This is the parser for the csv files. 
    
    The koding virtualenv is named as DataVizProject. Use workon DataVizProject 
    to get the modules
    
    Few things to try/learn:
        -In the directory of this folder..try "import parse"
        -Then you would be able to use the commands like help(parse.parse)
         It would give the docstring for the parse function
        -To get the values of the constants you can try "parse.MY_FILE"
         Objects should be prefaced with parse
        - You can also do 
            new_data = parse.parse(my_file, ",")
            new_data[0].keys()
            for dict_item in new_data:
                print dict_item["Descript"]
    
"""

import csv

MY_FILE = "../dataviz/data/sample_sfpd_incident_all.csv"

def parse(file_name, delimiter):
    """ Convert a raw-csv file to a json like object """
    
    #open the file
    opened_file = open(file_name)
    
    #read the csv data
    csv_data = csv.reader(opened_file, delimiter=delimiter)
    
    #get the headers
    fields = csv_data.next()
    
    #empty list
    parsed_data = []
    
    for row in csv_data:
        #zip function is interesting ;)
        parsed_data.append(dict(zip(fields,row)))
        
    #close the file
    opened_file.close()
    
    return parsed_data
    
def main():
    print parse(MY_FILE, ",")
    
if __name__ == "__main__":
    #boilerplate code
    #for people to use just the parse function
    main()
    
    
    
    