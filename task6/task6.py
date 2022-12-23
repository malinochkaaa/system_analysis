import json
import numpy as np

def yt(x, k):
    return np.matmul(x, k)

def kt(x, k, s):
    lambtt = np.matmul(np.ones((len(s))), np.matmul(x,k))
    return 1/lambtt*yt(x, k)

def task(s):
    s = json.loads(s)
    rang = np.zeros((len(s), len(s[0]), len(s[0])))

    for n in range(len(s)):
        for m in range(len(s[0])):
            for k in range(len(s[0])):
                if s[n][m] > s[n][k]:
                    rang[n][m][k] = 1
                elif s[n][m] == s[n][k]:
                    rang[n][m][k] = 0.5
                else: rang[n][m][k] = 0

    x = np.zeros((len(s[0]), len(s[0])))

    for n in range(len(s[0])):
        for k in range(len(s[0])):
            for m in range(len(s)):
                x[n][k] += rang[m][n][k]
    x = x/len(s)
    x = np.transpose(x)
    k0 = np.ones((len(s)))/len(s)

    e = 0.001
    while np.linalg.norm(kt(x, k0, s) - k0) >= e:
        k0 = kt(x, k0, s)
    res = list(np.around(kt(x, k0, s), 3))
    encodedNumpyData = json.dumps(res)
    return encodedNumpyData

