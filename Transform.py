import json
import pandas as pd

with open('./vvb.json', 'r') as f:
  data = json.load(f)

df = pd.DataFrame(data)
dir_pandas = './{}'.format('vvb.csv')
df.to_csv(dir_pandas, index=False, encoding='utf-8')