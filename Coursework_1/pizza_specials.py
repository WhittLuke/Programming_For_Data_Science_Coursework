
""" Author: Luke Whittaker
    Student Number: Add this just before submission

    This script will look to implement the functionality for exercise three - creating a pizza specials menu
    that will be printed to a text file """


# Define all of the imports for this exercise
from xml.etree import ElementTree
import csv




def readXML(xml_file_path):
    """ This function will look to read all of the data from the XML file

        parameter:
            xml_file_path: Location of the XML data

        returns:
            xml_data: A variable containing the XML data """
    try:
        with open(xml_file_path) as data_file:
            xml_data = ElementTree.parse(data_file)

        return  xml_data
    except Exception as ioe:
        raise IOError("unable to open file %s" % ioe)



""" Create functions placing the data regarding sizes, toppings, and crusts into dictionaries """



def readCSV(csv_file_path):
    """ This function will read in all of the contents of the pizza_specials.csv fill

        parameter:
            csv_file_path: Location of the csv data

        returns:
            csv_data: A variable containg all of the csv data"""
    pass





def writeToTxtFile(pizza_special_list):
    """ This function will write the created specials menu to .txt file

        parameter:
            pizza_special_list: a list containing both entries describing the specials.
            Should be able to loop over this list and wrote each item to the .txt file"""
    pass





def composeSpecialsMenu(sizes_dict, toppings_dict, crusts_dict, csv_specials_data):
    """ This function takes the dictionaries and looks to compile the specials menu

        parameters:
            sizes_dict: dictionary containing all of the info regarding the sizes of pizzas
            toppings_dict: dictionary of the toppings data
            crusts_dict: dictionary of the crusts data
            csv_specials_data: the data outlining what the specials consist of. This will also act as
                            the main source to compile the menu

        returns:
            pizza_specials_list: a list containing the two available specials from the csv file.
            This will also immediately pass the created list to the writeToTxtFile()"""
    pass





def main():
    # Define the path locations for both the .xml and .csv files needed for this exercise
    xml_data_path_string = "data/pizza.xml"
    csv_data_path_string = "data/pizza_specials.csv"


    # Extract all the data from the XML file
    xml_data = readXML(xml_data_path_string)

    print(xml_data)






if __name__ == '__main__':
    main()


















