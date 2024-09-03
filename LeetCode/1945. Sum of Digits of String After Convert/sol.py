class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def transform(s:str)->str:
            return f"{sum(list(map(int,list(s))))}"
        alpha=list("abcdefghijklmnopqrstuvwxyz")
        h={}
        for i in range(1,27):
            h[alpha[i-1]]=f"{i}"
        ans=""
        for i in s:
            ans+=h[i]
        for i in range(k):
            ans=transform(ans)
        return int(ans)
        