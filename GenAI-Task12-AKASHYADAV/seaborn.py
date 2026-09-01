import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('Utube.csv')
df.head()
sns.relplot(x='Total Videos', y='Avg Video Length (min)', hue='Holographic Content Rating', data=df)
plt.show()


tips = sns.load_dataset('tips')
tips.head()
sns.lineplot(y='total_bill', x='day', hue='sex', data=tips, style = 'smoker')
plt.show()