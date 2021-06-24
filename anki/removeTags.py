# 21.6.2021 - 1h
# 22.6.2021 - 2h
# 23.6.2021 - 2h
# 24.6.2021 - 5h

# uses <span style="background-color: rgba(255, 255, 255, 0.9);">Ich will in einem Haus mit einem
# groß..&nbsp;</span><span style="background-color: rgba(255, 255, 255, 0.9);">&nbsp;Garten wohnen.</span>


from ankipandas import Collection
import os

from anki import MODEL_BASIC, MODEL_BASIC_AND_REVERTED, ANKI_CONFIG
from configuration import load_config, HOME_DIRECTORY, load_config_value
from user_inputs import select_from_list, ask_string_value


def clean_html_tags(x):
    x = '<br>' + x
    return x


def selection(_relevant_notes, _nmodel):
    relevant_selection = _relevant_notes.query("nmodel=='{}'".format(_nmodel)).copy()
    if relevant_selection.count == 0:
        print("Selection is empty!")
    return relevant_selection


def log_notes(_notes, _message):
    print("***********************************************************************")
    print(_message)
    print(_notes['nfld_Front'])
    print(_notes['nfld_Back'])
    print("***********************************************************************")
    print("\n")


def clean_html_tags_for_basic_cards(_selection):
    _selection.fields_as_columns(inplace=True)
    log_notes(_selection, 'Before transformation:')

    _selection['nfld_Front'] = clean_html_tags(_selection['nfld_Front'])
    _selection['nfld_Back'] = clean_html_tags(_selection['nfld_Back'])

    log_notes(_selection, 'After transformation:')

    col.notes.update(_selection.fields_as_list())
    col.write(modify=True)


# read configuration, if not exist, write new one
collection_path = load_config_value(
    config_name=ANKI_CONFIG,
    message="No config value is saved for ANKI COLLECTION PATH. Please insert one ",
    default=HOME_DIRECTORY + os.sep + 'AppData' + os.sep + 'Roaming' + os.sep + 'Anki2',
    config_key1='collection_path'
)
print(collection_path)
user_name = load_config_value(
    config_name=ANKI_CONFIG,
    message="No config value is saved for ANKI USER. Please insert one ",
    default='Default',
    config_key1='user_name'
)
print(user_name)

# open collection
col = Collection("C:\\Users\\pedo\\AppData\\Roaming\\Anki2", user="tisan")
notes = col.notes
cards = col.cards

# choose which deck you want to clean
decks = cards.list_decks()
selected_index_of_deck = select_from_list(decks)

# note IDs gotten e.g. from a query on cards
deck_notes_ids = col.cards[cards.cdeck == decks[selected_index_of_deck]].nid.unique()
# get a DataFrame of rows for these note IDs
relevant_notes = col.notes.loc[deck_notes_ids]

clean_html_tags_for_basic_cards(selection(relevant_notes, MODEL_BASIC))
clean_html_tags_for_basic_cards(selection(relevant_notes, MODEL_BASIC_AND_REVERTED))
