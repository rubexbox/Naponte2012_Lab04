# Naponte2012_Lab04
Python project made for a class at FAU. Created with the goal of learning about dictionaries and reading files.\

The .py file consists of two functions, make_dict() and test_dict(). Neither function takes an argument.

Make_dict() first opens the text file fl_cities.txt, which contains a list of Florida cities and their zipcodes, separated by colons. The function then creates a Python dictionary of all the cities listed in fl_cities, wih the city names as the key.

Test_dict() opens the text file fl_maint.txt, which contains a list of commands. It then reads fl_maint.txt and depending on the command, will (p)rint the entire dictionary of cities with their zipcodes, (f)ind a city and print its zipcode (if it exists in the dictionary), or (c)hanges the zipcode of a city (if it exists in the dictionary). If a command is issued that isn't f, p, or c, the function will print an error message.
