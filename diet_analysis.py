"""
Author: Aidan Zhong
Date: 2025/4/24 12:16
Description:
"""
import pandas as pd
from matplotlib import pyplot as plt

# load the data
file_path = 'Results_21MAR2022_nokcaladjust.csv'
df = pd.read_csv(file_path)

diet_influence = df.groupby('diet_group').agg({
    'mean_ghgs': 'mean',
    'mean_land': 'mean',
    'mean_watscar': 'mean',
    'mean_eut': 'mean',
    'mean_ghgs_ch4': 'mean',
    'mean_ghgs_n2o': 'mean',
    'mean_bio': 'mean',
    'mean_watuse': 'mean',
    'mean_acid': 'mean'
}).reset_index()

diet_influence_plot = diet_influence.set_index('diet_group')

metrics = ['mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut', 'mean_ghgs_ch4', 'mean_ghgs_n2o', 'mean_bio',
           'mean_watuse', 'mean_acid']

for metric in metrics:
    plt.figure()
    diet_influence_plot[metric].sort_values().plot(kind='barh')
    plt.xlabel(metric.replace('_', ' ').title())
    plt.ylabel('Diet Group')
    plt.title(f'Comparison of {metric.replace("_", " ").title()} by Diet Group')
    plt.tight_layout()
    plt.savefig(metric.replace('_', ' ').title() + '.png')
    plt.show()
