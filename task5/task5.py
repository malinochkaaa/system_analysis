import json
import numpy as np

def task(ranking1_str, ranking2_str):
    ranking1 = json.loads(ranking1_str)
    ranking2 = json.loads(ranking2_str)

    y_a = relationship_matrix(ranking1)
    y_a_t = y_a.transpose()

    y_b = relationship_matrix(ranking2)
    y_b_t = y_b.transpose()

    y_a_b = np.multiply(y_a, y_b)
    y_a_b_t = np.multiply(y_a_t, y_b_t)

    conflicts = []

    for i in range(y_a_b.shape[0]):
        for j in range(y_a_b[i].shape[1]):
            if int(y_a_b[i,j]) == 0 and int(y_a_b_t[i,j]) == 0:
                if [str(j+1),str(i+1)] not in conflicts:
                    conflicts.append([str(i+1),str(j+1)])

    return conflicts


def relationship_matrix(ranking):
    ranks = dict()
    rank_len = ranking_length(ranking)
    for i, rank in enumerate(ranking):
        if type(rank) is str:
            ranks[int(rank)] = i
        else:
            for r in rank: 
                ranks[int(r)] = i

    return np.matrix([[1 if ranks[i+1] <= ranks[j+1] else 0 for j in range(rank_len)] for i in range(rank_len)])

def ranking_length(ranking) -> int:
    length = 0;
    for i in ranking:
        if type(i) is str:
            length+=1
        else:
            length+=len(i)
    return length

if __name__ == '__main__':
    str1 = '["1", ["2", "3"], "4", ["5", "6", "7"], "8", "9", "10"]'
    str2 = '[["1", "2"], ["3", "4", "5"], "6", "7", "9", ["8", "10"]]'
    print(task(str1, str2))