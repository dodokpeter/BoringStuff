import yaml


def load_config(config_name):
    if config_name is None: config_name = 'BoringStuff.yml'
    with open(config_name, 'r') as file:
        mainConf = yaml.safe_load(file)
        # return type is dictionary f.e.:
        # prime_service['rest']['url']




names_yaml = """
- 'eric'
- 'justin'
- 'mary-kate'
"""

with open('names.yaml', 'w') as file:
    yaml.dump(names, file)
    print(open('names.yaml').read())