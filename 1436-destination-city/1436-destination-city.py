class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        for i in range(len(paths)):
            source_key=paths[i][1]
            flag=True
            for j in range(len(paths)):
                if paths[j][0]==source_key:
                    flag=False
                    break
            if flag:
                return source_key
            