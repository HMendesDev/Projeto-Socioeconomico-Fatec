import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#Nuvem de palavras das Empresas
nuvem = pd.read_csv("NuvemSonhos.txt")
print(nuvem)
text = " ".join(i for i in nuvem["Sonhos:"])
print(text)
# eliminar = set(STOPWORDS)
# eliminar = eliminar.update(["Não", "se", "sea", "aplica","eu","meus","você", "meu",
# "e","em","as","do","na","e","era","fui","é","no","de","Tenho","Estou","como","para"])
# wordcloud = WordCloud(stopwords=eliminar,background_color= "black",width=1600,
# height=800).generate(text)
# plt.figure()
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.savefig('Graficos/graficonuvem1.jpeg',format = 'jpeg')

#Nuvem de palavras dos Sonhos
