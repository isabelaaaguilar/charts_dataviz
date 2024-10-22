import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.family'] = 'Calibri'
plt.rcParams['font.size'] = '12'

titanic = pd.read_csv("titanic.csv")
grouped_data = titanic.groupby(['survived', 'sex']).size().unstack()

barWidth = 0.3
r1 = np.arange(len(grouped_data))
r2 = [x + barWidth for x in r1]

plt.bar(r1, grouped_data['male'], color='#4d65db', width=barWidth, label='Homens')
plt.bar(r2, grouped_data['female'], color='#cf1d32', width=barWidth, label='Mulheres')

plt.xlabel('')
plt.xticks([r + barWidth / 2 for r in range(len(grouped_data))], ['Não sobreviveram', 'Sobreviveram'])
plt.ylabel('Quantidade de Pessoas')
plt.title('Comparação do Número de Sobreviventes do Titanic por Gênero', pad=25)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

for i in range(len(grouped_data)):
    plt.text(i, grouped_data['male'].iloc[i] + 10, str(grouped_data['male'].iloc[i]), ha='center') 
    plt.text(i + barWidth, grouped_data['female'].iloc[i] + 10, str(grouped_data['female'].iloc[i]), ha='center') 

plt.legend(frameon=False)
plt.show()
