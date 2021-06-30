# user will be asked for selection from the string list
def select_from_list(list_of_choices):
    list_len = len(list_of_choices)
    for i in range(list_len):
        print('Select ' + str(i) + ' for ' + list_of_choices[i])
    index = -1
    while index < 0 or index > list_len - 1:
        index = int(input("Select your deck: "))
    print('You selected: ' + list_of_choices[index])
    return index


def ask_string_value(message, default):
    user_input = input(message + ' (default = ' + default + "'): ")
    if user_input == '':
        return default
    else:
        return user_input
