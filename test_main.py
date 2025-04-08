from main import *
def fast_MED(S, T, memo=None):
    if memo is None:
        memo = {}

    if (S, T) in memo:
        return memo[(S, T)]

    if len(S) == 0:
        memo[(S, T)] = len(T)
        return len(T)

    if len(T) == 0:
        memo[(S, T)] = len(S)
        return len(S)

    if S[0] == T[0]:
        result = fast_MED(S[1:], T[1:], memo)
    else:
        insert = fast_MED(S, T[1:], memo)
        delete = fast_MED(S[1:], T, memo)
        substitute = fast_MED(S[1:], T[1:], memo)
        result = 1 + min(insert, delete, substitute)

    memo[(S, T)] = result
    return result

def fast_align_MED(S, T, memo=None):
    if memo is None:
        memo = {}

    if (S, T) in memo:
        return memo[(S, T)]

    # Base Case 1: S is empty → insert everything from T
    if len(S) == 0:
        aligned_S = '-' * len(T)
        aligned_T = T
        result = (len(T), aligned_S, aligned_T)
        memo[(S, T)] = result
        return result

    # Base Case 2: T is empty → delete everything from S
    if len(T) == 0:
        aligned_S = S
        aligned_T = '-' * len(S)
        result = (len(S), aligned_S, aligned_T)
        memo[(S, T)] = result
        return result

    # Match → no cost
    if S[0] == T[0]:
        dist, rest_S, rest_T = fast_align_MED(S[1:], T[1:], memo)
        result = (dist, S[0] + rest_S, T[0] + rest_T)
        memo[(S, T)] = result
        return result

    # Try all three edits
    insert_dist, insert_S, insert_T = fast_align_MED(S, T[1:], memo)
    insert = (1 + insert_dist, '-' + insert_S, T[0] + insert_T)

    delete_dist, delete_S, delete_T = fast_align_MED(S[1:], T, memo)
    delete = (1 + delete_dist, S[0] + delete_S, '-' + delete_T)

    subst_dist, subst_S, subst_T = fast_align_MED(S[1:], T[1:], memo)
    subst = (1 + subst_dist, T[0] + subst_S, T[0] + subst_T)

    result = min(insert, delete, subst, key=lambda x: x[0])
    memo[(S, T)] = result
    return result
    
def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])

