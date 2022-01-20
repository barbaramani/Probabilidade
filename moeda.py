import numpy as np

p = 0.5
nsim = 10
nhead = 0
saida = []

for i in range(0,nsim):
    if (np.random.uniform() < p):
        nhead = nhead+1
        saida.append(1)
    else:
        saida.append(0)
print('Saida:', saida)
print('Frequência de caras:', nhead/nsim)