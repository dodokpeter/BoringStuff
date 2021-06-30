from cases.anki.remove_tags import clean_tags
import sys

from core.user_inputs.inputs import select_from_list

print('Welcome in ANKI automations. Please select what you want to do:')

# read an options if provided
command = str(sys.argv[1])

clean_tags_command = command.startswith('ct')

if not clean_tags_command:
    options = [
        'clean the html tags in deck',
    ]
    selected_index_of_deck = select_from_list(options)
    if selected_index_of_deck == 0:
        clean_tags_command = True

if clean_tags_command:
    clean_tags()
else:
    print('Sorry, command -' + command + '- is not valid.')
