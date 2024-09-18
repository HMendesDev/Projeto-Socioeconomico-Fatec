import pandas as pd
import matplotlib.pyplot as plt
import numpy 
valores = []
colunas_para_remover = ["Empresa que está contrado:","Escreva algumas linhas sobre sua história e seus sonhos de vida:","Idade:"]
tabela = pd.read_excel("DadosPSE.xlsx")
tabela = tabela.drop(columns=colunas_para_remover)
tabela.columns = tabela.columns.str.strip()
for j in range(len(tabela.columns)):
    valores.append(tabela.columns[j])
for i in range (len(valores)):
    plt.figure(figsize=(14, 6)) 
    plt.pie(tabela[valores[i]].value_counts(),autopct="%1.0f%%")
    plt.legend(labels=tabela[valores[i]].value_counts().index, 
           loc="upper left",  
           bbox_to_anchor=(0.75, 1),  
           fontsize=8)
    plt.title(valores[i],fontsize = 14,fontweight='bold')
    plt.savefig(f'Graficos/grafico{i}.pdf',format = 'pdf')
    plt.close()