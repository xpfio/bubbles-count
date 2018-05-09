import json
from pprint import pprint
import seaborn as sns
import pandas as pd

with open('bubble-count-310fd-bubble-entries-export (5).json') as json_data:
    d = json.loads(json_data.read())
    json_data.close()

    df = pd.DataFrame(data=d).transpose()
    print(df['id'].value_counts())
