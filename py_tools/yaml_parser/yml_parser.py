import yaml
import os
PARAMETERS_FILE='parameters.yml'
TEST_PARAMETERS_FILE='test_parameters.yml'

def parse_yaml(filename):
    full_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),filename)
    with open(full_filename, 'r') as config:
        try:
            parsed_yaml = yaml.load(config)
        except yaml.YAMLError as exc:
            print(exc)
    return parsed_yaml

def write_to_yaml_file(filename, contents):
    full_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),filename)
    f_stream = open(full_filename, 'w')
    yaml.dump(contents, f_stream, default_flow_style=False)
    f_stream.close()

def walk_and_merge(base_dict, custom_option):
    for key in base_dict:
        custom_option_key = list(custom_option)[0]
        if type(base_dict.get(key)) == type(dict()):
            print("this is dict")
            walk_and_merge(base_dict, custom_option)
        elif key == custom_option_key:
            base_dict[key] = custom_option[custom_option_key]
    return base_dict

def merge_files(base, custom):
    base_config = parse_yaml(base)
    print(base_config)
    custom_config = parse_yaml(custom)
    for key in custom_config:
         base_config = walk_and_merge(base_config, {key: custom_config.get(key)})
    print(base_config)
    #yaml.dump(base_config, PARAMETERS_FILE, default_flow_style=False)
    write_to_yaml_file(PARAMETERS_FILE, base_config)

def main():
    print("alloha")
    merge_files(PARAMETERS_FILE, TEST_PARAMETERS_FILE)

if __name__ == '__main__':
    main()