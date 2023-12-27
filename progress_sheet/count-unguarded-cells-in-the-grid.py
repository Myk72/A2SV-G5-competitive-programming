class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        g = [[0] * n for i in range(m)]
        for i, j in guards:
            g[i][j] = 1
        for i, j in walls:
            g[i][j] = 1
        st=set()
        for a,b in guards:
            # row
            right,left=b+1,b-1

            while left>=0 and g[a][left]!=1:
                st.add((a,left))
                left-=1
            while right<n and g[a][right]!=1:
                st.add((a,right))
                right+=1
            # column
            up,bottom=a-1,a+1
            while up>=0 and g[up][b]!=1:
                st.add((up,b))
                up-=1
            while bottom < m and g[bottom][b]!=1:
                st.add((bottom,b))
                bottom+=1

        return m*n-len(st)-len(walls)-len(guards)
                