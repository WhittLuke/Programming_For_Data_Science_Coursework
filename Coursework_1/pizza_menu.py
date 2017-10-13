
""" Author: Luke Whittaker
    k-number: 1758283

    Description: For the first task we will look to create a pizza menu for a company called CMP.

    They have provided us with an XML file to create this menu. """


# define the imports that will be used throughout the script
from xml.etree import ElementTree


def main():

    """ NOTE TO EXAMINER: If you change the location of the pizza.xml file
         please assign its path to the data_path_string variable"""

    # define a variable to hold the path of the pizza.xml file
    # this just makes changing the path easier if it needs to be changed
    data_path_string = "data/pizza.xml"

    try:
        # I haven't specified the mode because the default mode for open is read
        with open(data_path_string) as data_file:
            tree = ElementTree.parse(data_file)

    except IOError as ioe:

        print "I/O Error: unable to open file: %s" % ioe

    # Access the root from the data stored within the tree variable
    root = tree.getroot()

    # First we want to print out the Company's name
    print "# %s" % root.find("shopname").text


    """ Not an ideal solution but it works """

    # Loop through and print out all of the different sizes that are available
    print "\n## Sizes"
    for item in root.find("sizes"):
        print "-  %s" % item.text


    # Then loop through and print out the Toppings
    print "\n## Toppings"
    for item in root.find("toppings"):
        print "- %s" % item.text


    # Finally print out the different kinds of crusts
    print "\n## Crusts"
    for item in root.find("crusts"):
        print "- %s" % item.text


if __name__ == '__main__':

    """ This conditional statement is here only to call the main() when this script
        has been executed"""
    main()