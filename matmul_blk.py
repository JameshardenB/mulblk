import numpy as np
import time

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
    
    ## let user set up N and blocksize n
    N = 30
    time_diff = np.array([])  # time difference between matmul_blk and np.matmul
    a = np.random.random((N,N))
    b = np.random.random((N,N))
    # define time_blk and time_matmul
    time_blk = np.array(N)
    # print(time_blk)
    time_matmul = np.array(N) 
    # print(len(time_matmul))
    for n in range (1, N+1):
        # print(n,end =',')
        # follow the running time for matmul_blk
        time_start = time.perf_counter()
        # print(time_start)
        c = matmul_blk(a,b,N,n)
        time_end = time.perf_counter()
        # print(time_end)
        # print(time_blk[])
        time_blk = time_end-time_start
        
        #print(c)
        # #print()
        # follow the running time for np.matmul
        time_matmul_start = time.perf_counter()
        c_nai = np.matmul(a,b)
        time_matmul_end = time.perf_counter()
        time_matmul = time_matmul_end-time_matmul_start
        time_diff = np.append(time_diff, time_blk-time_matmul) # time difference 
 # analyse the blocksize n and the calculation time 
fig, ax = plt.subplots()

ax.plot(range(1,N+1), time_diff, linewidth=2.0)

plt.show()
