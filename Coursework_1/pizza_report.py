
""" Author: Luke Whittaker
    Student Number: Add just before submission

    This Python script will look to implement exercise 2 from the coursework specification. """

# Import all of the Python modules needed for this exercise
from xml.etree import ElementTree
import csv


def readXML(filepath):

    """ This function will extract all of the data from the XML file

        parameter:
            file path to access the data

        returns:
            a variable containing all of the XML data """
    try:
        # Open the XML data and parse it using ElementTree
        with open(filepath) as xml_data:
            xml_pizza_data = ElementTree.parse(xml_data)

        return xml_pizza_data
    except Exception as ioe:
        raise IOError("unable to open file %s" % ioe)


def numberOfPizzaSizes(pizza_data):

    """ This function looks to extract all of the available pizza sizes

        parameter:
            pizza_data (the XML data passed to this class)

        returns:
            A list of available pizza sizes """

    # Create an empty list to store the sizes
    list_of_pizza_sizes = []

    # Get access to root of the XML data
    size_attribute = pizza_data.getroot()

    # Loop through the Sizes attribute within the XML file and add them to the lis
    for size in size_attribute.find("sizes"):
        list_of_pizza_sizes.append(size.text)

    return list_of_pizza_sizes


def numberOfToppings(pizza_data):

    """ Function for accessing the number of toppings available

        parameter:
            pizza_data -> XML data

        returns:
            A list of the toppings available """

    # Create an empty list to store the toppings
    list_of_toppings = []

    # Access the root for the XML data
    toppings_attribute = pizza_data.getroot()

    # Loop through the toppings_attribute and store them into the list
    for topping in toppings_attribute.find("toppings"):
        list_of_toppings.append(topping.text)

    # return the toppings list
    return list_of_toppings


def numberOfCrusts(pizza_data):

    """ Function for accessing the number of toppings available

        parameters:
            pizza_data -> XML data

        returns:
            list of all the available crusts """

    # Create an empty list for storing the crusts
    list_of_crusts = []

    # Access the root of the XML file
    crusts_attribute = pizza_data.getroot()

    # Loop through the crusts_attribute and store the crusts into the list
    for crust in crusts_attribute.find("crusts"):
        list_of_crusts.append(crust.text)

    # return the list
    return list_of_crusts


def writeToCSV(sizes, toppings, crusts, total_combos):

    """ This function will look to write a report about the pizzas available at CMP to a .csv file

        paremeters:
            sizes: list of sizes available
            toppings: list of toppings available
            crusts: list of crusts availble
            total_combos: integer value for the total of combos """

    # First, create a file to store the results of the report
    with open('pizza_report.csv', 'w') as write_file:
        write_csv = csv.writer(write_file)

        # Create a header list -> the names will be the columns to be displayed within the .csv file
        headers = ['sizes', 'toppings', 'crusts', 'total_combo']

        # Create a list to store the results of the exercise and place them in the order of their corresponding header
        report_results = [len(sizes), len(toppings), len(crusts), total_combos]
        write_csv.writerow(headers)
        write_csv.writerow(report_results)




def main():

    # First define a file path string placeholder
    """ NOTE: if you change the location of the pizza.xml file, please update this string """
    data_file_string = "data/izza.xml"

    # Now we can call the read_xml function to get access to our data
    pizza_data_xml = readXML(data_file_string)

    # Call the numberOfPizzaSizes() -> give the function the XML data
    sizes_available = numberOfPizzaSizes(pizza_data_xml)

    # Call the numberOfToppings() -> give it the XML data
    toppings_available = numberOfToppings(pizza_data_xml)

    # Call the numberOfCrusts() -> give it the XML data
    crusts_available = numberOfCrusts(pizza_data_xml)


    # 1 -> for the size
    #  + len(toppings available)
    # 1 -> size of crust + no toppings
    total_combo_of_XL_pizzas = 1 + len(toppings_available) + 1
    total_combo_of_L_pizza = 1 + len(toppings_available) + 1
    total_combo = total_combo_of_XL_pizzas + total_combo_of_L_pizza


    # Call writeToCSV() -> pass sizes, toppings, crusts data and the total_combo data
    writeToCSV(sizes_available, toppings_available, crusts_available, total_combo)

if __name__ == '__main__':
    main()
