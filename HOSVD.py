#Cornell Summer School Charles F. Van Loan
import numpy
from numpy import svd, svds

def dense(A):
    #A is n(1) x ... x n(d) tensor
    #U is d cell array with U(k) being the left singular vector of a's mode-k unfolding
    #S is n(1) x ... x n(d) tensor : A x1 U(1) x2 U(2) ... xd U(d)
    S = A

    for k,_ in range(A.size()):
        C = A[k,:].numpy() ##may need to make sure columns are arranged in increasing order
        [U,_,_] = svd(C)
        t_U = numpy.transpose(U)
        S(k,:).append(numpy.tensordot(S,t_U,k))
    return S, t_U

def sparse(A):
    #A is n(1) x ... x n(d) tensor
    #U is d cell array with U(k) being the left singular vector of a's mode-k unfolding
    #S is n(1) x ... x n(d) tensor : A x1 U(1) x2 U(2) ... xd U(d)
    S = A

    for k,_ in range(A.size()):
        C = A[k,:].numpy() ##may need to make sure columns are arranged in increasing order
        [U,_,_] = svds(C)
        t_U = numpy.transpose(U)
        S(k,:).append(numpy.tensordot(S,t_U,k))
    return S, t_U