# This code follows this tutorial: https://realpython.com/python-json/#writing-json-with-python

import json

# 1) Convert Python dictionaries into JSON.
def part_1_convert_dict_to_json():
    food_ratings = {"organic_dog_food": 2, 
                    "human_food": 10}
    json1 = json.dumps(food_ratings) # returns a string when run on cli. On code - use print statement. Hence storing in a variable for printing.
    print(json1)

    numbers_present = {1: True,
                    2: True, 
                    0: False}
    json2 = json.dumps(numbers_present)
    print(json2) # automatically converts boolean types to lowercase - json format. Also, numbers become strings.

    dog_id = 1
    dog_name = "Frieda"
    dog_registry = {dog_id: {"name": dog_name}}
    json3 = json.dumps(dog_registry)
    print(json3)

    available_nums = {(1, 2): True, 3: False}
    # json.dumps(available_nums) # This should flag a TypeError, as one of the keys is a tuple - unsupported format.
    json4 = json.dumps(available_nums, skipkeys=True) # This works, and skips the key-value pair that follows unsupported format.
    print(json4) # Use skip keys with caution.

    toy_conditions = {"chew_bone": 7,
                    "ball": 3, 
                    "sock": -1}
    json5 = json.dumps(toy_conditions, sort_keys=True) # Sorts keys alphabetically.
    print(json5)

# 2) Write a JSON File with Python.
dog_data = {
    "name": "Frieda", 
    "isDog": True,
    "hobbies": ["eating", "sleeping", "barking"],
    "age": 8,
    "address": {
        "work": None, 
        "home": ["Berlin", "Germany"]
    },
    "friends": [
        {
            "name": "Philipp",
            "hobbies": ["eating", "sleeping", "reading"]
        },
        {
            "name": "Mitch",
            "hobbies": ["running", "snacking"]
        }
    ]
}

def part_2_writing_json():
    with open("hello_frieda.json", mode="w", encoding="utf-8") as write_file:
        json.dump(dog_data, write_file) # dump requires - object intended to write & the file to write.
        # Optional parameters are the same for dump & dumps.

### Reading JSON with Python.
# As a rule of thumb, you work with json.loads() when your data is already present in your Python program. 
# You use json.load() with external files that are saved on your disk.

# 2) Convert JSON objects to a python dictionary.
def part3_json_python_interconversion():
    dog_registery = {1: {"name": "Frieda"}}
    dog_json = json.dumps(dog_registery)
    print(dog_json)
    new_dog_registry = json.loads(dog_json) # won't be the same as 1 being an integer would have become a string when serialized to json. 
    # Later when converted back to python dic, there's no way python will know it was an int before, so the 1 remains a string from the json.
    print(new_dog_registry)
    print(new_dog_registry == dog_registery) # False

    dog_data = {
        "name": "Frieda", 
        "is_dog": True, 
        "hobbies": ["eating", "sleeping", "barking"],
        "age": 8,
        "address": {
            "work": None, 
            "home": ("Berlin", "Germany")
        }
    }
    print(dog_data)
    dog_data_json = json.dumps(dog_data)
    print(dog_data_json)
    new_dog_data = json.loads(dog_data_json)
    print(new_dog_data)
    print(new_dog_data == dog_data)
    # When you serialize a Python tuple, it becomes a JSON array. 
    # When you load JSON, a JSON array correctly deserializes into a list because Python has no way of knowing that you want the array to be a tuple.

    with open("hello_frieda.json", mode="r", encoding="utf-8") as read_file:
        frie_data = json.load(read_file) # argument must be a text file or a binary file.
    print(type(frie_data))
    print(frie_data["name"])











if __name__ == "__main__":
    # part_1_convert_dict_to_json()
    # part_2_writing_json()
    part3_json_python_interconversion()


