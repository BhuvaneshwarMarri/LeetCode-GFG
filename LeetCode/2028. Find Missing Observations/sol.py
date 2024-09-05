class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        sum_m=sum(rolls)
        sum_n=mean*(n+m)-sum_m

        # print(sum_m,sum_n)
        #condition verification
        if sum_n<0 or (sum_n==0 and n!=0) or sum_n//n>6 or (sum_n//n==6 and sum_n%n!=0) or sum_n//n==0:
            return []
        
        ans=[sum_n//n]*n

        if sum_n%n !=0:
            for i in range(sum_n%n):
                ans[i]+=1
        return ans