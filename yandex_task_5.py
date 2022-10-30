N, M, K = map(int, input().split(' '))
B = []
for i in range(N):
    B.append(list((map(int, input().split(' ')))))


import copy


def printMatrix(A):
    print(max(map(lambda x: x[0], A)))


def getMaxOrder(A, K):
    ans = copy.deepcopy(A)

    for i in range(len(A)):
        for j in range(len(A[0])):
            start = (i, j)
            for l in range(len(A)):
                for _ in range(len(A[0])):
                    point = (l, _)
                    if (((i - l) ** 2) + ((j - _) ** 2)) <= (K ** 2) and start != point:
                        ans[i][j] += A[l][_]

    return ans




printMatrix(getMaxOrder(B, K))