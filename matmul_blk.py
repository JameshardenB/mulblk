import numpy as np

# N square size of Matrix, n blockSize, C=AB

def matmul_blk(A, B, N, n):
    C = np.zeros((N,N))
    for jj in range(0, N, n):
        for kk in range(0, N, n):
            for i in range(0, N):
                for j in range(jj, min(jj+n, N)):
                    temp = 0
                    for k in range(kk, min(kk+n, N)):
                        temp += A[i][k] * B[k][j]
                    C[i][j] += temp
    return C

if __name__ == '__main__':

    a = np.random.random((9,9))
    b = np.random.random((9,9))

    c = matmul_blk(a,b,9,3)
    print(c)
    print()
    
    c_naive = np.matmul(a,b)
    print(c_naive)
