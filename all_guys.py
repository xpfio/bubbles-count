import json
from pprint import pprint
import seaborn as sns
import pandas as pd
import math

import matplotlib.pyplot as plt

with open('bubble-count-310fd-export (21).json') as json_data:
    d = json.loads(json_data.read())
    json_data.close()

    df = pd.DataFrame(data=d['bubble-entries']).transpose()
    ids = pd.Series.unique(df['id'])
    print(ids)
    print(df['id'].value_counts())
    print('Number of IDS',len(ids))

    for ID in ids:
        if not math.isnan(ID):
            ID_format = int(ID)
            selected_input = df[df['id'] == ID_format].iloc[1:]
            if len(selected_input.index) > 1:
                plot = sns.boxplot(x="numberOfBubbles", y="timeSpent", data=selected_input)
                plt.savefig(str(ID_format)+'-'+str(len(selected_input.index))+'.png')
                plt.clf()
            