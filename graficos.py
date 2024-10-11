import csv
import matplotlib.pyplot as plt

# Inicializar listas para armazenar os resultados
num_jogos = []
vitorias_jogador1 = []
empates = []
vitorias_jogador2 = []

# Ler os dados do arquivo CSV usando a biblioteca padrão csv
with open('resultados.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # Pegar os últimos quatro valores da linha
        num_jogos.append(int(row[-4]))
        vitorias_jogador1.append(int(row[-3]))
        empates.append(int(row[-2]))
        vitorias_jogador2.append(int(row[-1]))

# Usar os valores mais recentes (última linha do CSV) para o gráfico de pizza
labels = ['Jogador X', 'Empates', 'Jogador O']
sizes = [vitorias_jogador1[-1], empates[-1], vitorias_jogador2[-1]]
colors = ['#4CAF50', '#FFC107', '#F44336']  # Cores para cada setor do gráfico

# Plotar o gráfico de pizza
plt.figure(figsize=(13, 8))
plt.pie(sizes, radius=0.5, colors=colors, autopct='%1.1f%%', startangle=90)
plt.legend(labels,
            title='Legenda',
           loc="lower left",
          bbox_to_anchor=(1, 0, 0.5, 1))
plt.title('Distribuição dos Resultados de "Campeão contra Campeão" em 10.000 jogos')
plt.axis('equal')  # Garantir que o gráfico de pizza seja um círculo

# Mostrar o gráfico
plt.show()
