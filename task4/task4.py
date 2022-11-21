from io import StringIO
import math
import csv


def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    out = []
    for row in reader:
        out.append(row)
    arr1 = []
    [arr1.append(i[0]) for i in out]
    arr2 = []
    [arr2.append(i[1]) for i in out]
    arr3 = []
    for i in range(len(out)):
        for j in range(i+1, len(out)):
            if out[i][1] == out[j][0]:
                arr3.append(out[i][0])
    arr4 = []
    for i in range(len(out)):
        for j in range(i+1, len(out)):
            if out[i][1] == out[j][0]:
                arr4.append(out[j][1])
    arr5 = []
    for i in range(len(out)):
        for j in range(i+1, len(out)):
            if out[i][0] == out[j][0]:
                arr5.append(out[i][1])
                arr5.append(out[j][1])
    res = []
    v = set()
    for i in out:
        for j in i:
            v.add(int(j))
    vmax = max(v)
    v = sorted(v)
    [res.append([]) for i in v]
    for i in v:
        res[i - 1].append(arr1.count(str(i)))
        res[i - 1].append(arr2.count(str(i)))
        res[i - 1].append(arr3.count(str(i)))
        res[i - 1].append(arr4.count(str(i)))
        res[i - 1].append(arr5.count(str(i)))
    h = 0
    for i in range(len(v)):
        for j in range(int(vmax)):
            if res[i][j] != 0:
                h += res[i][j] * math.log(res[i][j] / (len(v) - 1), 2) / (len(v) - 1)
    h = -h
    return h
