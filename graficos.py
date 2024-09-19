import pandas as pd
import matplotlib.pyplot as plt
import numpy 
from wordcloud import WordCloud

valores = []
colunas_para_remover = ["Empresa que está contrado:","Escreva algumas linhas sobre sua história e seus sonhos de vida:"]
tabela = pd.read_excel("DadosPSE.xlsx")
tabela = tabela.drop(columns=colunas_para_remover)
tabela.columns = tabela.columns.str.strip()
for j in range(len(tabela.columns)):
    valores.append(tabela.columns[j])
    
#for i in range (len(valores)):
#    plt.figure(figsize=(14, 8)) 
#    plt.pie(tabela[valores[i]].value_counts(),autopct="%1.0f%%")
#    plt.legend(labels=tabela[valores[i]].value_counts().index, 
#           loc="upper left",  
#           bbox_to_anchor=(0.75, 1),  
#           fontsize=8)
#    plt.title(valores[i],fontsize = 14,fontweight='bold')
#    plt.savefig(f'Graficos/grafico{i}.pdf',format = 'pdf')
#    plt.close()

tabelas_esca = []
tabelas_esca.append(tabela["Relativo as questões"]) 
tabelas_esca.append(tabela["Relativo ao formulário"])    
for i in range(len(tabelas_esca)):
    faixas_formularios = ['1','2','3','4','5','6']   
    bins = [1, 2, 3, 4, 5, 6, 7]   
    plt.figure(figsize=(14, 8))
    tabelas_esca[i] = tabela["Relativo ao formulário"]
    tabela['Faixa Etária'] = pd.cut(tabelas_esca[i], bins=bins, labels=faixas_formularios, right=True)
    contagem_formu = tabela['Faixa Etária'].value_counts(sort=False)
    cores = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF6666', '#66FFCC', '#FF9966', '#9966FF']
    bars = plt.bar(contagem_formu.index, contagem_formu.values, color=cores)
    plt.legend(bars, faixas_formularios, loc="upper left", bbox_to_anchor=(1, 1))
    plt.title(tabelas_esca[i],fontsize = 14,fontweight='bold')
    plt.savefig(f"Graficos/graficoformu{i}.pdf", format = 'pdf')

