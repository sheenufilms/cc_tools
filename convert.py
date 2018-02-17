import cc_dat_utils
# import test_data
# import test_json_utils
import json
#JUST FOR TESTING
# cc_dat = cc_dat_utils.make_cc_data_from_dat("data/pfgd_test.dat")
# print(cc_dat)


#Part 2
# input_json_file = "data/test_data.json"
# with open(input_json_file, "r") as reader:
#         game_library_data = json.load(reader)
# print("JSON data:")
# print(game_library_data)
# print("")
#
# gameJason = test_json_utils.make_game_library_from_json(game_library_data)
# print("Game Library loaded from JSON:")
# print(gameJason)

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print_game_library(game_library_data) in test_data.py
### End Add Code Here ###


#Part 3
import cc_json_utils

#Reads the json
with open("data/sheenuy_cc1.json", "r") as reader:
	json_cc_data= json.load(reader)
#Turns json into a data file and stores it in a variable
cc_data_file=cc_json_utils.make_cc_data_file_from_json(json_cc_data)
#Uses that variable to run it into a function that turns the json into a DAT file.
cc_dat_utils.write_cc_data_to_dat(cc_data_file, "data/sheenuy_cc1.dat")
#print(cc_data_file)