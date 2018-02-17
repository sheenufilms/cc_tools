import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(json_data):
    #Initialize a new GameLibrary
    new_game_library = test_data.GameLibrary()

    #Loop through the json_data
    for game_data in json_data["Games"]:
        new_game = test_data.Game()
        new_game.title = game_data["Title"]
        new_game.year = game_data["Year"]
        platform_data = game_data["Platform"]
        new_game.platform = test_data.Platform()

        new_game.platform.name = platform_data["Name"]
        new_game.platform.launch_year = platform_data["Launch Year"]

        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
        new_game_library.add_game(new_game)
    #Return the completed game_library

    return new_game_library