# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionSet

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value

from ..Data import characters_list



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#

class UltraGreedKills(Range):
    """
    How many times you need to kill Ultra Greed (with different characters) to win the game.

    (Maximum capped at the character_amount value)
    """
    display_name = "Ultra Greed kills for goal"
    range_start = 1
    range_end = 34
    default = 3

class CharacterAmount(Range):
    """
    Amount of characters from the list to be added to the item pool. (Including starting characters)

    (Maximum capped at number of characters in available_characters)
    """
    display_name = "Character Amount"
    range_start = 1
    range_end = 34
    default = 3

class StartingCharacters(Range):
    """
    Number of characters from the item pool to start with.

    (Maximum capped at the character_amount value)
    """
    display_name = "Starting Characters"
    range_start = 1
    range_end = 34
    default = 1

class Characters(OptionSet):
    """
    List of available characters that CAN be added to the item pool.
    """
    display_name = "Available Characters"
    valid_keys = [char_name for char_name in characters_list]
    default = sorted(set([char_name for char_name in characters_list]))



# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["available_characters"] = Characters
    options["character_amount"] = CharacterAmount
    options["starting_characters"] = StartingCharacters
    options["ultra_greed_kills_goal"] = UltraGreedKills
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    return options