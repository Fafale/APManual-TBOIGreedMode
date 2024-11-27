from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value, get_option_value
from BaseClasses import MultiWorld, CollectionState

import re

def setRequiredGreedCounters(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    available_characters_list = list(get_option_value(multiworld, player, "available_characters")).copy()
    yaml_charAmount = get_option_value(multiworld, player, "character_amount")
    yaml_greedKillAmount = get_option_value(multiworld, player, "ultra_greed_kills_goal")

    clamped_charAmount = clamp(yaml_charAmount, 1, len(available_characters_list))
    clamped_greedKillAmount = clamp(yaml_greedKillAmount, 1, clamped_charAmount)

    return (f"|Greed Counter:{clamped_greedKillAmount}|")