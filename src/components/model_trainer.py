import pandas as pd
import os

train_data_path: str=os.path.join('artifacts',"train.csv")
test_data_path: str=os.path.join('artifacts',"test.csv")
raw_data_path: str=os.path.join('artifacts',"data.csv")

print(train_data_path)

test = os.makedirs(os.path.dirname(train_data_path),exist_ok=True)
print(test)