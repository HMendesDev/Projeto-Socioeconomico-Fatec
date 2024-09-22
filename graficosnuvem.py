import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import nltk
from nltk.corpus import stopwords


stopwords_pt = set(stopwords.words('portuguese'))
eliminar = ["Não", "se", "sea", "aplica","quero","área", "Sonho","dar",
"SP","Sempre","ter","fazer","tentar","mim","toda","vida","financeira","dar","ano"
,"nasci","anos","família","dia","escola","possa","desde","pai","mãe","então","pessoa"
,"area","estudei","pública","algo","pais","objetivo","Franca","Fatec","carreira","grande"
,"outra","Gosto","curso","interessei","atualmente","tudo","morar","tempo","bom","desejo",
"faço","pós","espero","bem","faculdade","cresci","Agora","Paulo","pois","forma","talvez",
"cidade","tão","decidi","vestibular",]
stopwords_pt.update(eliminar)

#Nuvem de palavras das Empresas
nuvem = pd.read_csv("NuvemEmpresas.txt")
print(nuvem)
text_empresas = " ".join(i for i in nuvem["Empresas:"])
print(text_empresas)
wordcloud_empresas = WordCloud(stopwords=eliminar,background_color= "black",width=1600,
height=800).generate(text_empresas)
plt.figure()
plt.imshow(wordcloud_empresas, interpolation="bilinear")
plt.axis("off")
plt.savefig('Graficos/graficonuvem1.jpeg',format = 'jpeg')

#Nuvem de palavras dos Sonhos
nuvem2 = pd.read_excel("DadosPSE.xlsx")
nuvem2 = nuvem2.dropna(how = 'all')
nuvem_sonhos= nuvem2["Sonhos:"].dropna()
texto_completo = " ".join(nuvem_sonhos.astype(str))
palavras_sem_stopwords = [palavra for palavra in texto_completo.split() if palavra.lower() not in stopwords_pt]
text_sonhos = " ".join(palavras_sem_stopwords)
print(text_sonhos)
wordcloud_sonhos = WordCloud(stopwords=stopwords_pt,background_color= "black",width=1600,
height=800).generate(text_sonhos)
plt.figure()
plt.imshow(wordcloud_sonhos, interpolation="bilinear")
plt.axis("off")
plt.savefig('Graficos/graficonuvem2.jpeg',format = 'jpeg')