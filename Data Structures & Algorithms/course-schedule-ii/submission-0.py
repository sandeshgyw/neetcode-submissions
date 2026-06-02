class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        results=set()
        adjList=defaultdict(list)
        visited=set()
        visiting=set()

        for crs,pre in prerequisites:
            adjList[crs].append(pre)

        def canFinish(course):
            if adjList[course]==[]:
                results.add(course)
                visited.add(course)
                return True

            if course in results:
                return True

            if course in visiting:
                return False
            
            visiting.add(course)
            for pre in adjList[course]:
                if not canFinish(pre):
                    return False
            visiting.remove(course)
            visited.add(course)
            results.add(course)
            return True

            

        

        for i in range(numCourses):
            if not canFinish(i):
                return []
            
        return list(results)
