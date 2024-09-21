import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

nuvem = pd.read_csv("NuvemEmpresas.txt")
print(nuvem)
text = " ".join(i for i in nuvem["Empresas:"])
print(text)
eliminar = set(STOPWORDS)
eliminar = eliminar.update(["Não", "se", "sea", "aplica"])
wordcloud = WordCloud(stopwords=eliminar,background_color= "black",width=1600,
height=800).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig('Graficos/graficonuvem1.jpeg',format = 'jpeg')


