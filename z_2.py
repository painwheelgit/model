import requests
import numpy as np
import math
import scipy.special as sp
import scipy.constants as const
import matplotlib.pyplot as plt
import json
import os

res = requests.get('https://jenyay.net/uploads/Student/Modelling/task_02_02.txt')

var = res.text.splitlines()[5].split()
r = float(var[1]) / 2
fmin = float(var[2])
fmax = float(var[3])
dx = 1000000
freq = np.arange(fmin, fmax, dx)
L = const.c / freq
k = 2 * math.pi / L


def func1(n, x):
    return sp.spherical_jn(n, x) + 1j * sp.spherical_yn(n, x)


def func3(n, x):
    return (x * sp.spherical_jn(n - 1, x) - n * sp.spherical_jn(n, x)) / (x * func1(n - 1, x) - n * func1(n, x))


def func2(n, x):
    return sp.spherical_jn(n, x) / func1(n, x)


massivSum = []
for sigN in range(1, 20):
    massivSum.append(((-1) ** sigN) * (sigN + 0.5) * (func3(sigN, k * r) - func2(sigN, k * r)))
sigma = (L ** 2) / math.pi * abs(np.sum(massivSum, axis=0)) ** 2

payload = {
    "data": []
}

for i in range(0, len(L) - 1):
    row = {"freq": freq[i], "lambda": L[i], "rcs": sigma[i]}
    payload['data'].append(row)
filename = "results/GFG.json"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, 'w', encoding='utf-8') as file:
    file.write(
        '{\n\t"data": [\n' + ',\n'.join('\t\t' + json.dumps(i) for i in payload["data"]) + '\n\t]\n}'
    )
plt.plot(freq / 10e6, sigma)
plt.grid()
plt.show()
