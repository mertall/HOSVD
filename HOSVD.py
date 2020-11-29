#Cornell Summer School Charles F. Van Loan
class HOSVD(object):
    def dense(A):
        #A is n(1) x ... x n(d) tensor
        #U is d cell array with U(k) being the left singular vector of a's mode-k unfolding
        #S is n(1) x ... x n(d) tensor : A x1 U(1) x2 U(2) ... xd U(d)
        S = A

        for k in range(A.size()):
            C = A[k,:].numpy() ##may need to make sure columns are arranged in increasing order
            [U[k],Sig,V] = svd(C)
            t_U = numpy.transpose(U)
            S = numpy.tensordot(S,t_U[k],k)
        return S, U, V

    def sparse(A):
        #A is n(1) x ... x n(d) tensor
        #U is d cell array with U(k) being the left singular vector of a's mode-k unfolding
        #S is n(1) x ... x n(d) tensor : A x1 U(1) x2 U(2) ... xd U(d)
        S = A

        for k in range(A.size()):
            C = A[k,:].numpy() ##may need to make sure columns are arranged in increasing order
            [U[k],Sig,V] = svds(C)
            t_U = numpy.transpose(U)
            S = numpy.tensordot(S,t_U[k],k)
        return S, U, V
    def emotions(S,t_U,V)
        eigen = t_U * S * V
        unique_info = numpy.transpose(t_U)
    # emotions is S? Clasification will use LS/QReither solving for min||C_e*a_e-z||_2 (LS) or R_e*a_e=QT_ez(QE)
