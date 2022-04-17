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

    # N size of Matrix, n blocksize
    
    N = 100
    n = 3

    a = np.random.random((N,N))
    b = np.random.random((N,N))

    time_start = time.perf_counter()
    c = matmul_blk(a,b,N,n)
    time_end = time.perf_counter()
    print(time_end-time_start)
    print(c)
    print()
    
    # the built in method np.matmul
    time_start = time.perf_counter()
    c_nai = np.matmul(a,b)
    time_end = time.perf_counter()
    print(time_end-time_start)
    print(c_nai)
