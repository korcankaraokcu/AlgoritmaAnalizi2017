def SubMaxSum(L):
    N = len(L)
    S = [0]*N
    S[0] = L[0]
    for i in range(1,N):
        S[i] = max(S[i-1]+L[i], L[i])
    return max(S)

test_array=[-6, -3, 5, -2, -1, 2, 6, -5]
print(SubMaxSum(test_array))