from core.configuration.user_conf import load_config, save_config

SAVINGS_CONFIG = 'savings_config.yaml'


def adding(a, b):
    return a + b


def newer_value(a, b):
    return b


def put_value_to_config(key1, key2, new_value, alter_func=adding):
    config = load_config(SAVINGS_CONFIG)
    value = config.get(key1, None)
    if value is None:
        config.setdefault(key1, dict())
        config.get(key1).setdefault(key2, new_value)
        save_config(SAVINGS_CONFIG, config)
        return new_value
    else:
        value2 = value.get(key2, None)
        if value2 is None:
            value.setdefault(key2, new_value)
            save_config(SAVINGS_CONFIG, config)
            return new_value
        else:
            calculated_value = alter_func(value2, new_value)
            value[key2] = calculated_value
            save_config(SAVINGS_CONFIG, config)
            return calculated_value


def final_message(key, manual_per_item_seconds, hours_of_programming, number_of_items):
    savings = number_of_items * manual_per_item_seconds
    print("I save you " + str(savings) + " seconds this time.")

    put_value_to_config(key, 'manual_per_item_seconds', manual_per_item_seconds, newer_value)
    put_value_to_config(key, 'hours_of_programming', hours_of_programming, newer_value)
    total_number_of_items = put_value_to_config(key, 'number_of_items', number_of_items)
    total_savings = put_value_to_config(key, 'seconds_saved', savings)

    hours = total_savings / 60 / 60
    print("In total, I save you " + str(hours) + " hours for " + str(total_number_of_items) + " items")
    print("")
    print("And spent " + str(hours_of_programming) + " hours for programming this functionality.")


# final_message("test", 5, 2, 100)
