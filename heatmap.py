import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'Calibri'
plt.rcParams['font.size'] = '12'

titanic = pd.read_csv("titanic.csv")

bins = [0, 15, 30, 40, 50, 80]
labels = ['0 - 15', '15 - 30', '30 - 40', '40 - 50', '50 - 80']
titanic['age_group'] = pd.cut(titanic['age'], bins=bins, labels=labels)

age_group_by_embark_town = titanic.groupby(['embark_town', 'age_group']).size().unstack()

plt.figure(figsize=(10, 6))
sns.heatmap(age_group_by_embark_town, annot=True, cmap='coolwarm', linewidths=0.5, fmt="d")

plt.title('Número de Pessoas por Faixa Etária e Cidade de Embarque', pad=25)
plt.xlabel('Faixa Etária') 
plt.ylabel('Cidade de Embarque')

plt.yticks(rotation=0)

plt.show()

