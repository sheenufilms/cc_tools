import cc_dat_utils
import test_data
import test_json_utils
import json

cc_dat = cc_dat_utils.make_cc_data_from_dat("data/pfgd_test.dat")
print(cc_dat)


#Part 2
input_json_file = "data/test_data.json"
with open(input_json_file, "r") as reader:
        game_library_data = json.load(reader)
print("JSON data:")
print(game_library_data)
print("")

gameJason = test_json_utils.make_game_library_from_json(game_library_data)
print("Game Library loaded from JSON:")
print(gameJason)

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print_game_library(game_library_data) in test_data.py
### End Add Code Here ###


#Part 3
#Load your custom JSON file
#Convert JSON data to cc_data
#Save converted data to DAT file