# CMPS 2200 Assignment 3
## Answers

**Name:** Mohini


Place all written answers from `assignment-03.md` here for easier grading.
1a)
Greedy Algorithm
In order to have the fewest coins in Geometrica while continuing the power of 2 denomination. You can start with the largest coin denomination (<=N), use as many of that coin as possible and subtract the total value of those coins from N. You can then repeat this with the next largest denomination, continuing until N is equal to 0. This works because it is equal to taking the binary representation of N and using one coin for every 1 bit in binary.

1b) Greed choice property: 
Claim: There exists an optimal solution that includes the greedy choice. 
Proof:
If C= {2^0,2^1,...2^k} is the set of coin denominations, and N is the target amount
Let 2^j be the largest coin such that 2^j <= N. The greedy algorithm will choose 2^j and recurse of N' = N-2^j. 
For contradiction, that there is exists an optimal solution S that does not use coin 2^j<= N, S must only use smaller coins 
The maximum sum you can get from at most one of each smaller coins is:
2^j-1+2^j-1+....+2^0 = 2^j-1<2^j
This proves that its impossible to build 2^j using only smaller coins unless you use multiple instances of some- which leads to more coins tham just using one 2^j. 
Any optimal solution must include 2^j, the greedy choice is part of some optimaul solution, this proves that the greedy choice holds.

Optimal substructure proof:
claim: The optimal solution to amount N contains within it optimal solutions to subproblems (amounts <N)
Proof:
Assume the greedy algorithm chooses 2^j, so we reduce the problem to finding optimal change N-2^j
We solve the subproblem N-2^j using a non-optimal set of coins. Combining that with the coin 2^j gives a non-optimal solution for N, which contradicts the assumption that we are making an optimal solution. 
Therefore, any optimal solution for N must include optimal solutions for its subproblems, this means that the optimal substructure holds. 
In conclusion, since both the greedy choice property and the optimal substructure property hold for coin denominations that are powers of 2- the greedy algorithm is guaranteed to fins an optimal solution. 

1c) Work: O(log N) since there are at most log2N bits in the binary representation of N, and each correspond to a coin. 
Span: O(log N) assuming a sequential scan from largest to smallest power of 2. With parrallelism it can be reduced to O(log logN)

2a) Counterexample, if the denominations in this example are {1,3,4} in order to make a chnage for 6:
  Greedy algorithm: take one 4 (remaining 2), then twos 1- 3coins
  Optimal Solution: take two 3s- 2 coins. 
Greedy does not guarantee the minimum number of coins. 

2b) Optimal Substructure
Let C(N) be the minimum number of coins nedded to make change for amount N, 
Optimal substructure:
  For any amount N, the optimal solution:
    C(N) = min(1+c(N-Di)) 
  proof:
  The optimal solution for N uses coin D_j then remaining value is N-D_j. The minimal number of coins to make up N-D_j is C(N-D_j) by the optimal substructure assumption. So adding 1 for the coin D_j, we get C(N) = 1+C(N-D_j)

  2c) The total work: O(Nk)
  The total span: O(N)
