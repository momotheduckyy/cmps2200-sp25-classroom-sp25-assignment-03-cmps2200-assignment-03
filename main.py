import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED=None):
    # TODO -  implement top-down memoization
    f MED is None:
        MED = {}

    if (S, T) in MED:
        return MED[(S, T)]

    if len(S) == 0:
        MED[(S, T)] = len(T)
        return len(T)
    if len(T) == 0:
        MED[(S, T)] = len(S)
        return len(S)

    if S[0] == T[0]:
        result = fast_MED(S[1:], T[1:], MED)
    else:
        insert = fast_MED(S, T[1:], MED)
        delete = fast_MED(S[1:], T, MED)
        substitute = fast_MED(S[1:], T[1:], MED)
        result = 1 + min(insert, delete, substitute)

    MED[(S, T)] = result
    return result

def fast_align_MED(S, T, MED=None):
    # TODO - keep track of alignment
    if MED is None:
        MED = {}

    if (S, T) in MED:
        return MED[(S, T)]

    # Base cases
    if len(S) == 0:
        aligned_S = '-' * len(T)
        aligned_T = T
        result = (len(T), aligned_S, aligned_T)
        MED[(S, T)] = result
        return result

    if len(T) == 0:
        aligned_S = S
        aligned_T = '-' * len(S)
        result = (len(S), aligned_S, aligned_T)
        MED[(S, T)] = result
        return result

    if S[0] == T[0]:
        dist, rest_S, rest_T = fast_align_MED(S[1:], T[1:], MED)
        result = (dist, S[0] + rest_S, T[0] + rest_T)
        MED[(S, T)] = result
        return result

    # Insertion
    insert_dist, insert_S, insert_T = fast_align_MED(S, T[1:], MED)
    insert = (1 + insert_dist, '-' + insert_S, T[0] + insert_T)

    # Deletion
    delete_dist, delete_S, delete_T = fast_align_MED(S[1:], T, MED)
    delete = (1 + delete_dist, S[0] + delete_S, '-' + delete_T)

    # Substitution
    subst_dist, subst_S, subst_T = fast_align_MED(S[1:], T[1:], MED)
    subst = (1 + subst_dist, T[0] + subst_S, T[0] + subst_T)

    # Choose best
    result = min(insert, delete, subst, key=lambda x: x[0])
    MED[(S, T)] = result
    return result

