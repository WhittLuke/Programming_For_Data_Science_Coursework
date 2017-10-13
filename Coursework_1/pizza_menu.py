
""" Author: Luke Whittaker
    k-number: 1758283

    Description: For the first task we will look to create a pizza menu for a company called CMP.

    They have provided us with an XML file to create this menu. """


# define the imports that will be used throughout the script
from xml.etree import ElementTree


def read_xml_file(filepath):

    """
        This function looks to read in an XML file and place the contents into a variable

        parameters:
            filepath: this specifies file path that the XML file is located (should be in working directory)

        returns:
            pizza_data: all of the data contained within the XML file will be placed into this variable
    """

    try:
        with open(filepath) as data_file:
            tree = ElementTree.parse(data_file)
            pizza_data = tree.getroot()
            return pizza_data

    except IOError as ioe:
        print "I/O Error: unable to open file:", ioe


def main():

    # define a variable to hold the path of the pizza.xml file
    # this just makes changing the path easier if it needs to be changed
    data_path_string = "data/pizza.xml"

    # Now, we try and get hold of the pizza data
    company_pizza_data = read_xml_file(data_path_string)


    # First we want to print out the Company's name
    # print "#  %s" % company_pizza_data["need to access the company name"]


    # Loop through and print out all of the different sizzes that are available
    # print "\n##  Sizes"
    # for item in company_pizza_data:
    #     print "-  %s" % item.text # This is the right line, just youtube it.


    # Then loop through and print out the Toppings


    # Finally print out the different kinds of crusts


if __name__ == '__main__':

    """ This conditional statement is here only to call the main() when this script
        has been executed"""
    main()