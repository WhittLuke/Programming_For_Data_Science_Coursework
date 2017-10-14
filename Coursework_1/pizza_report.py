
""" Author: Luke Whittaker
    Student Number: 1763234

    This Python script will look to implement exercise 2 from the coursework specification. """

# Import all of the Python modules needed for this exercise
from xml.etree import ElementTree
import csv


def read_xml(filepath):

    try:
        with open(filepath) as xml_data:
            xml_pizza_data = ElementTree.parse(xml_data)

        return xml_pizza_data
    except IOError as ioe:

        print "I/O Error: unable to open file: " % ioe


def numberOfPizzaSizes(pizza_data):

    """ This function looks to extract all of the available pizza sizes

        parameter (more like data):
            self.pizza_data (the XML data passed to this class

        returns:
            A list of available pizza sizes """

    # Create an empty list to store the sizes
    list_of_pizza_sizes = []

    # Get access to root of the XML data
    size_attribute = pizza_data.getroot()

    print(size_attribute)
    # Loop through the Sizes attribute within the XML file and add them to the lis
    for size in size_attribute.find("sizes"):
        list_of_pizza_sizes.append(size.text)

    return list_of_pizza_sizes





def main():

    # First define a file path string placeholder
    data_file_string = "data/pizza.xml"

    # Now we can call the read_xml function to get access to our data
    pizza_data = read_xml(data_file_string)

    # Call the numberOfPizzaSizes() -> give the function the XML data
    sizes_available = numberOfPizzaSizes(pizza_data)

    # Call the numberOfToppings() -> give it the XML data


    # Call the numberOfCrusts() -> give it the XML data
    

    print(len(sizes_available))


if __name__ == '__main__':
    main()
