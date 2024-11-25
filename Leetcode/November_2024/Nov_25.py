class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def encode(board):
            return ''.join(list(map(str,board[0])))+''.join(list(map(str,board[1])))
        dp={}
        def solve(board,i,j,cost):
            repr=encode(board)
            for dr,dc in [(-1,0),(0,-1),(1,0),(0,1)]:
                row = i+dr
                col = j+dc
                if(0<=row<2 and 0<=col<3):
                    board[i][j],board[row][col]=board[row][col],board[i][j]
                    if(cost+1<dp.get(encode(board),1e9)):
                        dp[encode(board)]=cost+1
                        solve(board,row,col,cost+1)
                    board[i][j],board[row][col]=board[row][col],board[i][j]
        r,c = -1, -1
        for i in range(2):
            for j in range(3):
                if(board[i][j]==0):
                   r,c=i,j
                   break 
        dp[encode(board)]=0
        solve(board,r,c,0)
        
        return dp.get('123450',-1)