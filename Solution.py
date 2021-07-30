class Solution:

    def __init__(self, n):
        self.n = n

    def get_total_number_of_ways_to_attend_classes(self):
        return 2 ** self.n

    def _sum(self, n):
        ans = 0
        for i in range(1, n+1):
            ans += i
        return ans

    def get_invalid_attendances(self):  # more then 4 consecutive attendances
        return self._sum(self.n-3)

    def get_possibilities_for_not_attending_ceremony(self):
        return 2**(self.n - 1) - (self.n - 3)

    def solve(self):
        valid_ways = self.get_total_number_of_ways_to_attend_classes() - self.get_invalid_attendances()
        print(valid_ways)
        print(str(self.get_possibilities_for_not_attending_ceremony()) + "/" + str(valid_ways))

n = int(input())
Solution(n).solve()
