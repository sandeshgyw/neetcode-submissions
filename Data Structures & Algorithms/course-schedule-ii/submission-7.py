class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        results=[]
        adjList=defaultdict(list)

        for crs,pre in prerequisites:
            adjList[crs].append(pre)

        visiting=set()
        completed=set()
        
        #decides if a course can be completed or not. if not returns false, if yes
        # appends to result
        def canFinish(course):
            # cannot complpete
            if course in visiting:
                return False
            #can complete
            # but this is not jut the case, if a course has adjlist and no loop it still completes
            if course in completed:
                return True
            if adjList[course]==[]:
                results.append(course)
                completed.add(course)
                return True
            
            
            visiting.add(course)

            for nei in adjList[course]:
                if not canFinish(nei):
                    return False
            
            results.append(course)
            completed.add(course)
            visiting.remove(course)
            return True
            

        for i in range(numCourses):
            if not canFinish(i):
                return []

        return results


        
