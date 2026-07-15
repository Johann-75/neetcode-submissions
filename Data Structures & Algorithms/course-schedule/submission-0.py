class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {i: [] for i in range(numCourses)}

        for course,prereq in prerequisites:
            prereqMap[course].append(prereq)

        visited = set()

        def dfs(course,prereqMap):
            if course in visited:
                return False
            visited.add(course)
            for p in prereqMap[course]:
                if not dfs(p,prereqMap):
                    return False
            visited.remove(course)
            prereqMap[course] = []
            return True

            
        for c in prereqMap.keys():
            if not dfs(c,prereqMap):
                return False
        return True

        