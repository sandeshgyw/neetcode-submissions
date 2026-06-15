class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        res=[]

        def isPali(sub):

            l=0
            r=len(sub)-1
            while l<r:
                if sub[l]!=sub[r]:
                    return False
                else:
                    l+=1
                    r-=1
            return True


        def backtrack(i):

            #valid leaf
            if i==len(s):
                result.append(res.copy())
                return
            
            #choices = n 

            for j in range(i,len(s)):
                #i=0,j=0
                sub=s[i:j+1]#i=0,j=1
                if isPali(sub):
                    res.append(sub)#["a"]ab
                    backtrack(j+1)#j+1=2nd a
                    #this line means the node of [a] with ab remaining is done
                    #so now we remove that a reach root node of []
                    res.pop()
                    #now the next loop will be with i=0 but j=1

        backtrack(0)
        return result


        