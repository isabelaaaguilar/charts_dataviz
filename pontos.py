import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Calibri'
plt.rcParams['font.size'] = '12'
data = pd.read_csv('healthexp.csv')
usa_data = data[data['Country'] == 'USA']
usa_data = usa_data[usa_data['Year'] >= 2000]

plt.figure(figsize=(6, 6))
plt.grid(True, which='both', axis='y', linestyle='solid', linewidth=0.5, alpha=0.5)
plt.scatter(usa_data['Life_Expectancy'], usa_data['Year'], color='#4d65db', marker='o', alpha=1, s=60)

plt.title('Expectativa de Vida nos Estados Unidos de 2000 em diante')
plt.xlabel('Expectativa de Vida (Anos)')
plt.ylabel('Ano')

plt.xticks(range(int(usa_data['Life_Expectancy'].min()), int(usa_data['Life_Expectancy'].max()) + 1))
plt.yticks(usa_data['Year'].unique())

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()  
plt.show()


