import pandas as pd
import matplotlib.pyplot as plt
import numpy 
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

valores = []
colunas_para_remover = ["Empresa que está contrado:","Escreva algumas linhas sobre sua história e seus sonhos de vida:","Idade:"]
tabela = pd.read_excel("DadosPSE.xlsx")
idade = (tabela["Idade:"])
tabela = tabela.drop(columns=colunas_para_remover)
tabela.columns = tabela.columns.str.strip()

#Graficos em pizza
for j in range(len(tabela.columns)):
    valores.append(tabela.columns[j])
    
for i in range (len(valores)):
    plt.figure(figsize=(15, 8)) 
    plt.pie(tabela[valores[i]].value_counts(),autopct="%1.0f%%")
    plt.legend(labels=tabela[valores[i]].value_counts().index, 
           loc="upper left",  
           bbox_to_anchor=(0.75, 1),  
           fontsize=8)
    plt.title(valores[i],fontsize = 14,fontweight='bold')
    plt.savefig(f'Graficos/grafico{i}.jpeg',format = 'jpeg')
    plt.close()
    
#Graficos em barras
idade = idade.dropna(how = 'all')
plt.figure(figsize=(15, 8)) 
idade_freq = idade.value_counts().sort_index()
ax = idade_freq.plot(kind='bar', color='blue')
plt.title('Idades:',fontsize = 14,fontweight='bold')
plt.xlabel('Idades',fontsize = 12,fontweight = 'bold')
plt.ylabel('Frequência',fontsize = 12,fontweight = 'bold')
ax.set_xticklabels(idade_freq.index.astype(int), rotation=0)
plt.savefig(f'Graficos/graficoidade.jpeg',format = 'jpeg')
plt.close()