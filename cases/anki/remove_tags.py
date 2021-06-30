# 21.6.2021 - 1h
# 22.6.2021 - 2h
# 23.6.2021 - 2h
# 24.6.2021 - 5h
# 25.6.2021 - 3.5h
# 30.6.2021 - 1h

from ankipandas import Collection
import os

from cases.anki.cleam_html import clean_html
from core.configuration.user_conf import load_config_value, HOME_DIRECTORY
from core.user_inputs.inputs import select_from_list

ANKI_CONFIG = 'anki_config.yaml'

MODEL_BASIC = 'Basic'
MODEL_BASIC_AND_REVERTED = 'Basic (and reversed card)'


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


def clean_html_tags_for_basic_cards(col, _selection):
    _selection.fields_as_columns(inplace=True)
    log_notes(_selection, 'Before transformation:')

    _selection['nfld_Front'] = clean_html(_selection['nfld_Front'])
    _selection['nfld_Back'] = clean_html(_selection['nfld_Back'])

    log_notes(_selection, 'After transformation:')

    col.notes.update(_selection.fields_as_list())
    col.write(modify=True)


def clean_tags():
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
    cards = col.cards

    # choose which deck you want to clean
    decks = cards.list_decks()
    selected_index_of_deck = select_from_list(decks)

    # note IDs gotten e.g. from a query on cards
    deck_notes_ids = col.cards[cards.cdeck == decks[selected_index_of_deck]].nid.unique()
    # get a DataFrame of rows for these note IDs
    relevant_notes = col.notes.loc[deck_notes_ids]

    clean_html_tags_for_basic_cards(col, selection(relevant_notes, MODEL_BASIC))
    clean_html_tags_for_basic_cards(col, selection(relevant_notes, MODEL_BASIC_AND_REVERTED))
