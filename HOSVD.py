#Cornell Summer School Charles F. Van Loan
def HOSVD(A):
    #A is n(1) x ... x n(d) tensor
    #U is d cell array with U(k) being the left singular vector of a's mode-k unfolding
    #S is n(1) x ... x n(d) tensor : A x1 U(1) x2 U(2) ... xd U(d)
    S = A

    for k in 1:length(A.size()):
        C = A[k,:].numpy() ##may need to make sure columns are arranged in increasing order whenever this line is run
        [U[k],Sig,V] = svd(C)
        t_U(k) = numpyu.transpose(U(k))
        S = numpy.tesnrodot(S,U(k),k)
