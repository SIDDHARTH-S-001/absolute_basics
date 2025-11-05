import yaml
import numpy as np

def read_yaml(filename):
    with open(filename) as file:
        try: 
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print(e)

def write_yaml(filename, data):
    with open(filename, mode="w") as write_file:
        output = yaml.dump(data, write_file)
        return output

filename = "random-data.yaml"
# data = read_yaml(filename)
data = {
    "name": "random_name",
    "address": "random_address", 
    "age": np.random.randint(18, 25),
    "stack": ["systems engineering", "reinforcement learning", "computer vision", "simulations"]
}
print(data)
print(type(data))
for key, value in data.items():
    print(f"{key}: {value}")
output = write_yaml(filename=filename, data=data)
