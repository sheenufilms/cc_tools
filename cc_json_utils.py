import cc_data


def make_cc_data_file_from_json(json_data):
    cc_data_file = cc_data.CCDataFile()

    for json_level in json_data:
        #Renders basic information: Level number, number of chips, .etc
        cc_level = cc_data.CCLevel()
        cc_level.level_number = json_level["level_number"]
        cc_level.num_chips = json_level["num_chips"]
        cc_level.time = json_level["time"]
        cc_level.upper_layer = json_level["upper_layer"]
        cc_level.lower_layer = json_level["lower_layer"]
        #Renders optional fields: Titles, hints, encoded passwords
        json_fields = json_level["optional_fields"]
        for json_field in json_fields:
            field_type = json_field["type"]
            #TITLE
            if (field_type == "title"):
                print("It's a title!")
                title = json_field["title"]
                cc_title_field = cc_data.CCMapTitleField(title)
                cc_level.add_field(cc_title_field)
            #HINT
            elif (field_type == "hint"):
                print("It's a hint")
                hint = json_field["hint"]
                cc_hint_field = cc_data.CCMapHintField(hint)
                cc_level.add_field(cc_hint_field)
            #PASSWORD
            elif (field_type == "password"):
                print("It's a encoded password")
                password = json_field["password"]
                cc_password_field = cc_data.CCEncodedPasswordField(password)
                cc_level.add_field(cc_password_field)
            #MONSTER
            elif (field_type == "monster"):
                print("Monster is loaded")
                #Take monster coordinates from JSON
                monsterarray = json_field["monster"]
                monster_cc = []
                for monster in monsterarray:
                    #Convert standard JSON coordinates to CCCoordinates
                    monster = cc_data.CCCoordinate(monster[0], monster[1])
                    #Add to the monster_cc array
                    monster_cc.append(monster)
                #Add entire array to MonsterMovementField function
                cc_monster_field = cc_data.CCMonsterMovementField(monster_cc)
                cc_level.add_field(cc_monster_field)
            else:
            #IF UNKNOWN, PRINT IDK
                print("IDK")
            print(field_type)
        print(cc_level)

        cc_data_file.add_level(cc_level)
    #Returns variable CC_DATA_FILE
    return cc_data_file
