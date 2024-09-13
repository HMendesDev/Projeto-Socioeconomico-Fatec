import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_excel("DadosPSE.xlsx")
tabela = tabela.drop("ID",axis=1)
tabela = tabela.drop("Hora de início",axis=1)
tabela = tabela.drop("Hora de conclusão",axis=1)
tabela = tabela.drop("Nome",axis=1)
tabela = tabela.drop("Email",axis=1)
tabela = tabela.drop("Hora da última modificação",axis=1)


for i in range (3):
    plt.pie(tabela["Pai"].value_counts(),labels=tabela["Pai"].value_counts().index,autopct="%1.1f%%")
    plt.savefig(f'Graficos/grafico{i}.pdf',format = 'pdf')