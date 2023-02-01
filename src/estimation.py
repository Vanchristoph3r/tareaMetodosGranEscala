import yaml

from clean_data import get_data
from model import train_model, get_predict_values
from preprocessing import encode_data

def load_config():
    with open("../config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config

if __name__ == "__main__":
    config = load_config()
    train_path = config.get("main",{}).get("train_path")
    test_path = config.get("main",{}).get("test_path")
    output_path = config.get("main",{}).get("output_path")
    eda = config.get("main",{}).get("eda", False)
    train, test = get_data(train_path=train_path, test_path=test_path, eda=eda)
    train, test = encode_data(train=train, test=test)
    model = train_model(train_data=train)
    predited_values = get_predict_values(model=model, test_data=test)
    predited_values.to_csv(output_path, index=False)
