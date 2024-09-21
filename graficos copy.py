import pandas as pd
import matplotlib.pyplot as plt
import numpy 
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

tabela = pd.read_excel("DadosPSE.xlsx")
nuvem = tabela.dropna(subset=['Empresa que está contrado:'],axis=0)['Empresa que está contrado:']
stopowords = set(STOPWORDS)
stopowords.update(["de", "meu", "em", "você", "eu", "os","nao","por","conta","trabalho","Faço","aplica","G","Gê"])
toda_nuvem = " ".join(k for k in nuvem)
print(toda_nuvem)
wordcloud = WordCloud(stopwords=stopowords,background_color="black",width=1600,height=800).generate(toda_nuvem)
fig, ax = plt.subplots(figsize = (10,6))
ax.imshow(wordcloud,interpolation='bilinear')
ax.set_axis_off()
plt.savefig(f'Graficos/graficonuvem.jpeg',format = 'jpeg')


