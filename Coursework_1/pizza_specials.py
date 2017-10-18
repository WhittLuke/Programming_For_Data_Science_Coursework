
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


def sizesDict(pizza_xml_data, pizza_data_dict):
    """ This function will take the data regarding the sizes available and convert it into a dictionary

        parameter:
            pizza_xml_data: data outlining all of the available sizes
            pizza_data_dict: the dictionary for storing all of the xml data """

    root = pizza_xml_data.find("sizes")

    # Then we can try and loop through the sizes_data and see if we're able to put data into the dict
    for pizza_size in root:

        if pizza_size.text == "Large":
            pizza_data_dict["L"] = pizza_size.text

        elif pizza_size.text == "Extra Large":
            pizza_data_dict["XL"] = pizza_size.text




def toppingsDict(pizza_xml_data, pizza_data_dict):

    """ This function will convert the topping xml data into a dictionary

        parameter:
            pizza_xml_data: all of the pizza data extracted from the xml file
            pizza_data_dict: the dictionary for storing all of the xml data """

    # Get all of the xml data regarding toppings
    root = pizza_xml_data.find("toppings")

    # Now loop through the data and place them into the dictionary
    for pizza_topping in root:

        if pizza_topping.text == "Mushrooms":
            pizza_data_dict["m"] = pizza_topping.text

        elif pizza_topping.text == "Extra Cheese":
            pizza_data_dict["x"] = pizza_topping.text



def crustsDict(crusts_data, pizza_data_dict):

    """ This function will place all of the data about the crusts into the crust dictionary

        parameter:
            crust_data: xml data about pizzas
            pizza_data_dict: the dictionary for storing all of the xml data"""

    # Loop through and place all of the types of crusts into the dictionary
    for crust in crusts_data.find("crusts"):
        pizza_data_dict["thick"] = crust.text



def readCSV(csv_file_path):
    """ This function will read in all of the contents of the pizza_specials.csv fill

        parameter:
            csv_file_path: Location of the csv data

        returns:
            csv_data: A variable containg all of the csv data"""

    try:
        with open(csv_file_path) as csv_data_file:
            csv_data = csv.reader(csv_data_file)
            next(csv_data)  # This removed the headers from the data

            # Now convert the csv data into a list
            csv_data = list(csv_data)
        return csv_data

    except Exception as ioe:
        raise IOError("unable to read file %s" % ioe)





def writeToTxtFile(pizza_special_list):
    """ This function will write the created specials menu to .txt file

        parameter:
            pizza_special_list: a list containing both entries describing the specials.
            Should be able to loop over this list and wrote each item to the .txt file"""
    with open('pizza_specials.txt', 'w') as write_file:
        for row in pizza_special_list:
            write_file.write(row + '\n')



def composeSpecialsMenu(pizza_data_dict, csv_specials_data):
    """ This function takes the dictionaries and looks to compile the specials menu

        parameters:
            pizza_data_dict: all of the data from the xml file store in a dictionary
            csv_specials_data: the data outlining what the specials consist of. This will also act as
                            the main source to compile the menu

        returns:
            pizza_specials_list: a list containing the two available specials from the csv file.
            This will also immediately pass the created list to the writeToTxtFile()"""

    pizza_specials_list = []

    # split the toppings if there appears to be more than one option

    first_special_toppings = list(csv_specials_data[0][2])

    # Create the specials menu from the
    supreme_special = "%s: %s Pizza with %s and %s and %s" % (csv_specials_data[0][0],
                                                              pizza_data_dict[csv_specials_data[0][1]],
                                                              pizza_data_dict[first_special_toppings[0]],
                                                              pizza_data_dict[first_special_toppings[1]],
                                                              pizza_data_dict[csv_specials_data[0][3]])

    simple_special = "%s: %s Pizza with %s and %s" % (csv_specials_data[1][0],
                                                      pizza_data_dict[csv_specials_data[1][1]],
                                                      pizza_data_dict[csv_specials_data[1][2]],
                                                      pizza_data_dict[csv_specials_data[1][3]])

    pizza_specials_list.append(supreme_special)
    pizza_specials_list.append(simple_special)

    # Send the specials_menu to the writeToTxtFile to save it to a .txt file
    writeToTxtFile(pizza_specials_list)





def main():
    # Define the path locations for both the .xml and .csv files needed for this exercise
    """ Examiner NOTE: if you change the location for the data files please update the corresponding file paths
        below """
    xml_data_path_string = "data/pizza.xml"
    csv_data_path_string = "data/pizza_specials.csv"

    # Create a dictionary to store all of the XML data and their codes
    pizza_data_dict = {}

    # Extract all the data from the XML file
    xml_data = readXML(xml_data_path_string)

    # Call the crustsDict()
    crustsDict(xml_data, pizza_data_dict)

    # Call the sizeDict()
    sizesDict(xml_data, pizza_data_dict)

    # Call the toppingDict()
    toppingsDict(xml_data, pizza_data_dict)

    # Now that all of the data from the xml file is stored in the dictionary
    # We can now look to read in the csv file
    returned_csv_data = readCSV(csv_data_path_string)

    # Call the composespecialsMenu()
    composeSpecialsMenu(pizza_data_dict, returned_csv_data)




if __name__ == '__main__':
    main()


















