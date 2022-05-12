import numpy.linalg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from PIL import Image
import PIL
import cv2

""" converter uma imagem para escalas de cinza e convertendo pra quadrado com python pillow """

img = Image.open('vegetacao.jpg')
largura = img.size[0]
altura = img.size[1]
corretivo = largura-altura
largura = largura-corretivo
img = img.resize((largura ,altura), Image.ANTIALIAS)
img.save('vegetacao1.jpg')

img = Image.open('vegetacao1.jpg')
img = img.convert('L')
img.save('vegetacao2.jpg')

X = plt.imread('vegetacao2.jpg')

pca = PCA(0.99)
lower_dimension_data = pca.fit_transform(X)

def pca_with_var_exp(X, var_exp = 0.99):
    pca = PCA(var_exp)
    lower_dimension_data = pca.fit_transform(X)
    approximation = pca.inverse_transform(
        lower_dimension_data
    )
    return approximation

def plot_subplot( X, i):
    plt.subplot(3 ,2, i)
    plt.imshow(X, cmap="gray")
    plt.xticks([])
    plt.yticks([])

img_1 = pca_with_var_exp(X, var_exp=0.99)
img_2 = pca_with_var_exp(X, var_exp=0.95)
img_3 = pca_with_var_exp(X, var_exp=0.90)

np.cov(np.transpose(X))
autovalores, autovetores= numpy.linalg.eig(X)

Explained_Variance_Ratio = X/np.sum(X)

#Matriz de covariância
print(X,'\n'*2)

#autovalores
print(autovalores,'\n'*2)

#autovetores
print(autovetores,'\n'*2)

#Variância explicada
print(Explained_Variance_Ratio,'\n'*2)

#Aplicação da Matriz à imagme original e a imagem original
plt.figure(figsize=(6,8))

plot_subplot(X, 1)
plt.title("original")

plot_subplot(img_1,2)
plt.title("Var. Explicada de 99%")

plot_subplot(X, 3)
plt.title("original")

plot_subplot(img_2,4)
plt.title("Var. Explicada de 95%")

plot_subplot(X, 5)
plt.title("original")

plot_subplot(img_3,6)
plt.title("Var. Explicada de 90%")

plt.tight_layout()
plt.show()


def impdados():

    with open(f'data.txt', 'w') as arquivo:
        arquivo.write(f'Variância: \n {X} \n\n')
        arquivo.write(f'Autovalores: \n {autovalores} \n\n')
        arquivo.write(f'Autovetores: \n {autovetores} \n\n')
        arquivo.write(f'variância explicada: \n {Explained_Variance_Ratio} \n\n')
        arquivo.write('\n\n')
        print(arquivo)

impdados()