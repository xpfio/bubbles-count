import json
from pprint import pprint
import seaborn as sns
import pandas as pd

with open('bubble-count-310fd-bubble-entries-export.json') as json_data:
    d = json.loads(json_data.read())
    json_data.close()
    # pprint(d)

    # values = {
    #     1:[],
    #     2:[],
    #     3:[],
    #     4:[],
    #     5:[],
    #     6:[],
    #     7:[],
    #     8:[],
    #     9:[],
    # }
    # for key in d:
    #     # print(key)
    #     key_ball = d[key]['numberOfBubbles']
    #     value = d[key]['timeSpent']
    #     values[key_ball].append(value)
    # print(values)

    # data = []
    # for key in d:
    #     data.append(d[key])
    # df = pandas.DataFrame(data=data)

    df = pd.DataFrame(data=d).transpose()
    # print(df)
    # ax = sns.violinplot(x="numberOfBubbles", y="timeSpent", data=df)
    ax2 = sns.boxplot(x="numberOfBubbles", y="timeSpent", data=df)
    ax2.get_figure().savefig("output1.png")
    # ax = sns.swarmplot(x="numberOfBubbles", y="timeSpent", data=df)
    ax = sns.violinplot(x="numberOfBubbles", y="timeSpent", data=df)
    ax.get_figure().savefig("output2.png")
