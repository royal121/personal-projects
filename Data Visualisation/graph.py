# First import the standard libraries
from collections import Counter

#Importing third party libraries. Add them in alphabetical order
import csv
import matplotlib.pyplot as plt #Importing pyplot module as plt name
import numpy.numarray as na

#Importing personal libraries
import parse

def visualize_days():
    """ This function will visualise data by day of week"""
    
    parsed_data = parse.parse(parse.MY_FILE, ",")
    #Get the parsed data
    
    
    #Counter would give us the tally of each dayofweek
    counter = Counter(item["DayOfWeek"] for item in parsed_data)
    """Help for counter function:
        print Counter(['a', 'b', 'c', 'a', 'b', 'b'])
        print Counter({'a':2, 'b':3, 'c':1})
        print Counter(a=2, b=3, c=1)
        
        Output:
        Counter({'b': 3, 'a': 2, 'c': 1})
        Counter({'b': 3, 'a': 2, 'c': 1})
        Counter({'b': 3, 'a': 2, 'c': 1})
    
        Read more: http://www.pythonforbeginners.com/collection/python-collections-counter
    """
    
    data_list = [
                    counter["Monday"],
                    counter["Tuesday"],
                    counter["Wednesday"],
                    counter["Thursday"],
                    counter["Friday"],
                    counter["Saturday"],
                    counter["Sunday"]
                ]
    day_tuple = tuple(["Mon", "Tue","Wed", "Thurs", "Fri", "Sat", "Sun"])
    #tuple coz plt.xticks() only accepts tuples
    
    plt.plot(data_list)
    #for y axis
    plt.xticks(range(len(day_tuple)), day_tuple)
    #for x axis
    """
        range(len(day_tuple) return [0,1,2,3,4,5,6]
        day_tuple is the list of days
    """
    
    plt.savefig("Days.png")
    #Save the file
    
    plt.clf()
    
def visualize_types():
    """
        This will plot the graph according to the types of crime
    """
    parsed_data = parse.parse(parse.MY_FILE, ",")
    #Get the parsed data
    
    
    #Counter would give us the tally of each dayofweek
    counter = Counter(item["Category"] for item in parsed_data)
    
    labels = tuple(counter.keys())
    #Here we are directly using counter.keys() coz the order of list doesn't matter
    
    xlocations = na.array(range(len(labels))) + 0.5
    #these are the locations of xticks
    # [0.5, 1.5, 2.5, ... , 16.5, 17.5]
    
    width = 0.5
    plt.bar(xlocations, counter.values(), width=width)
    
    plt.xticks(xlocations + width / 2, labels, rotation=90)
    #plot the x ticks between the bars. that's why width/2
    #labels should be vertical
    
    plt.subplots_adjust(bottom=0.4)
    #To move the graph up because of long labels. See days.png and days1.png
    
    
    plt.savefig("/home/isthegeek/Web/Days1.png")
    
    plt.clf()
def main():
    visualize_types()

if __name__ == "__main__":
    main()
