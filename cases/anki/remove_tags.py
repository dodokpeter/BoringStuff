from ankipandas import Collection
import os

from cases.anki.cleam_html import clean_html
from core.configuration.user_conf import load_config_value, HOME_DIRECTORY
from core.console.inputs import select_from_list
from core.console.saving import final_message

ANKI_CONFIG = 'anki_config.yaml'

MODEL_BASIC = 'Basic'
MODEL_BASIC_AND_REVERTED = 'Basic (and reversed card)'

# one item means
#  - one card to be copied into notepad++ and copy back into the clipboard
#  - editing spaces and formatting
SAVING_PER_CARD = 10
# 21-10.7.2021 - 17h - #6 Add script for loading and saving anki notes front and back text
PROGRAMMING_HOURS = 17


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
    # check if _selection is not empty, this caused key error later
    if _selection.empty:
        print("No data selected for transformation.")
    else:
        _selection.fields_as_columns(inplace=True)
        log_notes(_selection, 'Before transformation:')

        _selection['nfld_Front'] = _selection['nfld_Front'].apply(clean_html)
        _selection['nfld_Back'] = _selection['nfld_Back'].apply(clean_html)

        log_notes(_selection, 'After transformation:')

        col.notes.update(_selection.fields_as_list())
        col.write(modify=True)

        return _selection['nfld_Front'].count() + _selection['nfld_Back'].count()


def add_to_count(items_count):
    if items_count is None:
        return 0
    else:
        return int(items_count)


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
    col = Collection(collection_path, user=user_name)
    cards = col.cards

    # choose which deck you want to clean
    decks = cards.list_decks()
    selected_index_of_deck = select_from_list("Select your deck: ", decks)

    # note IDs gotten e.g. from a query on cards
    deck_notes_ids = col.cards[cards.cdeck == decks[selected_index_of_deck]].nid.unique()
    # get a DataFrame of rows for these note IDs
    relevant_notes = col.notes.loc[deck_notes_ids]
    sel1_count = clean_html_tags_for_basic_cards(col, selection(relevant_notes, MODEL_BASIC))
    sel2_count = clean_html_tags_for_basic_cards(col, selection(relevant_notes, MODEL_BASIC_AND_REVERTED))

    count = add_to_count(sel1_count) + add_to_count(sel2_count)

    final_message(
        key="anki_remove_tags",
        manual_per_item_seconds=SAVING_PER_CARD,
        hours_of_programming=PROGRAMMING_HOURS,
        number_of_items=count
    )
