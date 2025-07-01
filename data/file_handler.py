import json
import os

# Reads a JSON file and return the data
def read_json(filepath):
    if not os.path.exists(filepath):
        return []
    
    with open(filepath, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return[]

#  Write a python object
def write_json(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

#  Update a record in a JSON list
def update_json(filepath, key, value, new_data):
    data = read_json(filepath)
    updated = False
    for record in data:
        if record.get(key) == value:
            record.update(new_data)
            updated = True
            break
        if updated:
            write_json(filepath, data)

# Deletes a record from a JSON list
def delete_from_json(filepath, key, value):
    data = read_json(filepath)
    new_data = [record for record in data if record.get(key) != value]
    deleted = len(data) != len(new_data)
    if deleted:
        write_json(filepath, new_data)
    return deleted