import matplotlib.pyplot as plt

# Dados fornecidos pelo usuário
ide_usage = {
    'Visual Studio Code': 50,
    'IntelliJ IDEA': 22.5,
    'PyCharm': 9,
    'Eclipse': 6,
    'Sublime Text': 4,
    'Atom': 2.5,
    'NetBeans': 1.5
}

# Criando os dados para o gráfico
labels = list(ide_usage.keys())
sizes = list(ide_usage.values())
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f']
explode = (0.1, 0, 0, 0, 0, 0, 0)  # Destaque no primeiro pedaço

# Criando o gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Assegura que o gráfico será desenhado como um círculo.

# Título do gráfico
plt.title('Distribuição do Uso de IDEs')

# Exibindo o gráfico
plt.show()
