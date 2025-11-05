import yaml
import numpy as np
import hydra
from omegaconf import DictConfig, OmegaConf

class UsingPyyaml():
    def __init__(self):
        pass

    def read_yaml(self, filename):
        with open(filename) as file:
            try: 
                data = yaml.safe_load(file)
                return data
            except yaml.YAMLError as e:
                print(e)

    def write_yaml(self, filename, data):
        with open(filename, mode="w") as write_file:
            output = yaml.dump(data, write_file)
            return output
        
def parse_cfg(cfg):
    app, db, feat, log = cfg.app, cfg.database, cfg.features, cfg.logging
    print(app, db, feat, log)
    print(type(app))
    print(app.name)

@hydra.main(version_base=None, config_path=".", config_name="app-config")
def main(cfg: DictConfig) -> None:
    # print(OmegaConf.to_yaml(cfg))
    parse_cfg(cfg=cfg)

if __name__ == "__main__":
    # up = UsingPyyaml()
    # filename = "random-data.yaml"
    # # data = read_yaml(filename)
    # data = {
    #     "name": "random_name",
    #     "address": "random_address", 
    #     "age": np.random.randint(18, 25),
    #     "stack": ["systems engineering", "reinforcement learning", "computer vision", "simulations"]
    # }
    # print(data)
    # print(type(data))
    # for key, value in data.items():
    #     print(f"{key}: {value}")
    # output = up.write_yaml(filename=filename, data=data)
    data = main()
    # print(data.weekday)
    type(data)
