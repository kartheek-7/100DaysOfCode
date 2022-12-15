#leetcode-289,GameofLife

def condition(a,b):
            count=0
            p,q,r,s=False,False,False,False
            if a-1>=0:
                p=True
            if b-1>=0:
                q=True
            if a+1<m:
                r=True
            if b+1<n:
                s=True
            
            if p and q:
                if board[a-1][b-1]==1:
                    count=count+1
            if p:
                if board[a-1][b]==1:
                    count=count+1

            if q:
                if board[a][b-1]==1:
                    count=count+1

            if r and q:
                if board[a+1][b-1]==1:
                    count=count+1

            if r:
                if board[a+1][b]==1:
                    count=count+1

            if r and s:
                if board[a+1][b+1]==1:
                    count=count+1

            if s:
                if board[a][b+1]==1:
                    count=count+1

            if p and s:
                if board[a-1][b+1]==1:
                    count=count+1
            
            if board[a][b]==1:
                if count<2:
                        return 0

                if count==2:
                        return 1

                if count==3:
                    return 1

                if count>3:
                        return 0

            else:
                if count==3:
                    return 1

                else:
                    return 0

board=[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]  
m=len(board)
n=len(board[0])
nb=[[0 for i in range(n)] for j in range(m)]
for i in range(m):
    for j in range(n):
        nb[i][j]=condition(i,j)

for i in range(m):
    for j in range(n):
        board[i][j]=nb[i][j]
        
print(board)