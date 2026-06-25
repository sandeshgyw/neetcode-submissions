class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1={}
        l=0
        counts2={}#window state

        if len(s1)>len(s2):
            return False

        k=len(s1)

        for i in range(len(s1)):
            counts1[s1[i]]=counts1.get(s1[i],0)+1

        
        for r in range(len(s2)):
            counts2[s2[r]]=counts2.get(s2[r],0)+1

            while r-l+1>k:
                #invalid window
                counts2[s2[l]]=counts2.get(s2[l],0)-1
                if counts2[s2[l]]==0:
                    del counts2[s2[l]]
                l+=1


            if counts1==counts2:
                return True
        
        return False




        