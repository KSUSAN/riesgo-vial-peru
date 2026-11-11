import yaml

def load_config():
    with open("config/pipeline.yaml","r",encoding="utf-8") as file:
        config = yaml.safe_load(file)
    return config

if __name__ == "__main__":
    config = load_config()
    print(config)
