from cases.anki.remove_tags import clean_tags
import sys

from core.user_inputs.inputs import select_from_list

print('**********************************************')
print('Welcome in ANKI automations.')
print('**********************************************')

command = None
CMD_CLEAN_TAGS = 'ct'


def select_command():
    options = [
        'clean the html tags in deck',
    ]
    selected_index = select_from_list(options, with_no_selection=True)
    if selected_index == 0:
        return CMD_CLEAN_TAGS
    else:
        return None


# read an options if provided
if len(sys.argv) > 1:
    command = sys.argv[1]
else:
    print("Please select what you want to do:")
    command = select_command()

# do command
if command is None:
    print('Sorry, you selected to do nothing.')
else:
    if command.startswith(CMD_CLEAN_TAGS):
        clean_tags()
    else:
        print('Sorry, command -' + command + '- is not valid.')
