# create a yaml file and read it

import yaml

def create_and_read_yaml(file_path):
    # 1. Define the data structure
    data = {
        'project': 'Data Handling Suite',
        'version': 1.0,
        'features': ['serialization', 'deserialization', 'validation'],
        'settings': {
            'debug': True,
            'max_connections': 5
        }
    }

    # 2. Write the data to a YAML file
    print(f"Creating {file_path}...")
    with open(file_path, 'w') as file:
        # sort_keys=False preserves the order of your dictionary
        yaml.dump(data, file, default_flow_style=False, sort_keys=False)

    # 3. Read the data back from the YAML file
    print(f"Reading {file_path}...")
    with open(file_path, 'r') as file:
        loaded_data = yaml.safe_load(file)

    print("\nData retrieved from file:")
    print(loaded_data)
    
    # Verification
    assert data == loaded_data
    print("\nSuccess: The loaded data matches the original dictionary.")

if __name__ == "__main__":
    create_and_read_yaml('example.yaml')