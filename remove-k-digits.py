class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"
        n = []
        for i in num:
            # Can't pop do, just append
            if k == 0:
                n.append(i)
                continue
                
            if not len(n):
                n.append(i)
                continue
            if int(i) >= int(n[-1]):
                n.append(i)
            else:
                while len(n) and k > 0 and int(i) < int(n[-1]):
                    n.pop()
                    k-=1
                n.append(i)
        while k!= 0:
            n.pop()
            k-=1
        i = -1
        for j in range(len(n)):
            if n[j] != "0":
                i = j
                break
        if i != -1 or i != 0:
            n = n[i:]
    
        if not len(n):
            return "0"
        else:
            string1="".join(n)
            return string1