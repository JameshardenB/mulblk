# mulblk
function do multiplication of the matrix 
## The matrix product C = AB is a key numerical kernel in scientific computing. This multiplication
form a large part of the computational work in codes for, e.g., data-science, control and
simulation.An efficient implementation of matrix multiplication makes use of blocking. If size the sub-blocks of the matrices is chosen well, then
a sub-block of A, B and C should simultaneously fit in cache-memory
