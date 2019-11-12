import numpy as np

m = int(input("Enter m: "))
n = int(input("Enter n: "))

print("Start entering rows of the matrix:")

A = []

for i in range(m):
    A.append(np.array(list(map(float, input().strip().split()[:n]))))

A = np.array(A)

def mat_round(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            M[i][j] = round(M[i][j], 5)

def getQ(M):
    Q = []
    M = np.transpose(M)

    for i in range(len(M)):
        v = np.copy(M[i])
        for j in range(i):
            v -= (np.dot(M[i], Q[j]) / np.dot(Q[j], Q[j])) * Q[j]
        Q.append(v)

    Q = np.array(list(map(lambda v: v / sum(v**2)**0.5, Q)))
    Q = Q.transpose()

    return Q

def getR(M, Q):
    Q_t = np.transpose(Q)
    return np.matmul(Q_t, M)

Q = getQ(A)
R = getR(A, Q)

mat_round(Q)
mat_round(R)

print("\nQ:\n", Q)
print("\nR:\n", R)
