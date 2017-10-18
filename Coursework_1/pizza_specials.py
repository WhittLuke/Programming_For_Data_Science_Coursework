
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

def sizesDict(sizes_data):
    """ This function will take the data regarding the sizes available and convert it into a dictionary

        parameter:
            sizes_data: data outlining all of the available sizes

        returns:
            sizes_dict: a dictionary with the sizes key being 'L' etc.. and the value 'Large' """


    # First let's define are dictionary placehlder
    sizes_dict = {}
    root = sizes_data.find("sizes")
    # Create a list of codes that we can use as the keys
    list_of_sizes = ['XL', 'L']

    # Then we can try and loop through the sizes_data and see if we're able to put data into the dict
    for pizza_size in root:

        if pizza_size.text == "Large":
            sizes_dict[list_of_sizes[1]] = pizza_size.text

        elif pizza_size.text == "Extra Large":
            sizes_dict[list_of_sizes[0]] = pizza_size.text

    return sizes_dict



def toppingsDict(pizza_xml_data):

    """ This function will convert the topping xml data into a dictionary

        parameter:
            pizza_xml_data: all of the pizza data extracted from the xml file

        returns:
            toppings_dict: a dictionary which will highlight the codes for each topping and thier value """


    # Define a dict placeholder for the toppings
    toppings_dict = {}

    # Get all of the xml data regarding toppings
    root = pizza_xml_data.find("toppings")

    list_of_toppings = ['x', 'm']

    # Now loop through the data and place them into the dictionary
    for pizza_topping in root:

        if pizza_topping.text == "Mushrooms":
            toppings_dict["m"] = pizza_topping.text

        elif pizza_topping.text == "Extra Cheese":
            toppings_dict["x"] = pizza_topping.text

    return toppings_dict



def crustsDict(crusts_data):

    """ This function will place all of the data about the crusts into the crust dictionary

        parameter:
            crust_data: xml data about pizzas

        returns:
            crusts_dict: a dictionary outlining the crust code and its corresponding value """

    crusts_dict = {}

    # Loop through and place all of the types of crusts into the dictionary
    for crust in crusts_data.find("crusts"):
        crusts_dict["thick"] = crust.text

    return crusts_dict




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
    """ Examiner NOTE: if you change the location for the data files please update the corresponding file paths
        below """
    xml_data_path_string = "data/pizza.xml"
    csv_data_path_string = "data/pizza_specials.csv"

    # Extract all the data from the XML file
    xml_data = readXML(xml_data_path_string)

    # Call the crustsDict()
    return_crusts_dict = crustsDict(xml_data)
    print(return_crusts_dict)

    # Call the sizeDict()
    returned_sizes_dict = sizesDict(xml_data)
    print(returned_sizes_dict)


    # Call the toppingDict()
    returned_toppings_dict = toppingsDict(xml_data)
    print(returned_toppings_dict)



if __name__ == '__main__':
    main()


















