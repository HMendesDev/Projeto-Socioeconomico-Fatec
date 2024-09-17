import pandas as pd
import matplotlib.pyplot as plt
valores = []
colunas_para_remover = ["ID", "Hora de início", "Hora de conclusão", "Nome", "Email", "Hora da última modificação"]
tabela = pd.read_excel("DadosPSE.xlsx")
tabela = tabela.drop(columns=colunas_para_remover)
tabela.columns = tabela.columns.str.strip()
print(len(tabela.columns))
for j in range(len(tabela.columns)):
    valores.append(tabela.columns[j])
for i in range (1):
    plt.pie(tabela[valores[i]].value_counts(),labels=tabela[valores[i]].value_counts().index,autopct="%2.1f%%")
    plt.title("Quais fontes de entretenimento cultural você usa?")
    plt.savefig(f'Graficos/grafico{i}.pdf',format = 'pdf')