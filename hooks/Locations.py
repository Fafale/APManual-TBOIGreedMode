from ..Data import characters_list, generic_char_locations

def before_location_table_processed(location_table: list) -> list:
    for char_name in characters_list:
        for idx in range(0, len(generic_char_locations)):
            locName = generic_char_locations[idx][0].replace("CHAR", char_name)
            locRequirement = generic_char_locations[idx][1].replace("CHAR", char_name)
            location = {}

            location["name"] = locName
            location["category"] = [char_name]
            location["requires"] = locRequirement
            location_table.append(location)
        
        location = {}
        locName = f"{char_name} - Greed Counter"
        locRequirement = "(|Unlock CHAR| and |CHAR Progressive Floor: 6| and {ItemValue(CHAR items:8)}".replace("CHAR", char_name)
        location["name"] = locName
        location["category"] = [char_name]
        location["requires"] = locRequirement
        location["place_item"] = ["Greed Counter"]
        location_table.append(location)

    return location_table


# TO BE DONE!
# This function was copied from the Crash Team Racing manual,
# but I didn't bother to implement it yet.
#
# Change the Victory Location name according to the yaml settings
def create_victory_locations(location_table: list) -> list:
    location = {}
    location["name"] = "Defeat Ultra Greed 1 time"
    location["requires"] = "|@Greed Counter:1|"
    location["victory"] = True
    location_table.append(location)
    for i in range(2, 35):
        location = {}
        location["name"] = f"Defeat Ultra Greed {i} times"
        location["requires"] = f"|@Greed Counter:{i}|"
        location["victory"] = True
        location_table.append(location)

    return location_table