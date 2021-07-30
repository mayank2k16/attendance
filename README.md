There are a total of 2^n (possible ways to attend classes).

PART (A)

Out of them we need to reject the invalid permutations i.e permutations having 4 or more consecutive ABSENTS.
For ex if n=6
  we have choice of grouping 4A's, 5A's and 6A's 
  4A's can be arranged in 3 ways
  5A's can be arranged in 2 ways
  6A's can be arranged in 1 way
  = 3+2+1 = 6 rejected ways.
  
  so we get a formula here
  rejected_permutations = SUM_UP_T0_(1 -> N-3)
  
Hence total_valid_ways = total_number_of_ways_to_attend_classes(2^n) - invalid_attendances(SUM_UP_T0_(1 -> N-3))

PART (B)

Now as we know there will be 2^(n-1) ways for the last day to be PRESENT/ABSENT.(In our case fixing last day to ABSENT)
But these 2^(n-1) ways also included the rejected ways for last day as ABSENT.
So we filter out the already rejected days.

for ex if n=6
    AAAAAA
    PAAAAA
    PPAAAA
    these three combinations were rejected as they contain 4 or more consecutive ABSENTS and also have ABSENT ON LAST DAY.
    aftre looking some of diff values of n these cases will always comes out to be (n-3)
    
  so 2^(n-1) - (n-3) permutations are there in which we have absent in last day.
  
  so probability that a prson will be absent in his ceremony is = (2^(n-1) - (n-3)) / total_valid_ways
