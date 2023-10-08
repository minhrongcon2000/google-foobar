from collections import deque


def get_position_with_init_dist(idx):
    return (idx - idx % 8) // 8, idx % 8, 0

def isValidCell(x, y):
    return (x >= 0) and (x <= 7) and (y >= 0) and (y <= 7)


def solution(src, dest):
    src_pos = get_position_with_init_dist(src)
    dest_pos = get_position_with_init_dist(dest)
    
    q = deque([src_pos])
    dirs = ((2, 1), (1, 2), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))
    
    visited = [[False for _ in range(8)] for _ in range(8)]
    
    while len(q) > 0:
        currNode = q.pop()
        
        visited[currNode[0]][currNode[1]] = True
        
        if currNode[0] == dest_pos[0] and currNode[1] == dest_pos[1]:
            return currNode[2]
        
        for dir in dirs:
            dirX, dirY = dir
            currX, currY, currDist = currNode
            
            newX, newY = currX + dirX, currY + dirY
            currDist += 1
            
            if isValidCell(newX, newY) and not visited[newX][newY]:
                q.appendleft((newX, newY, currDist))
        
    return -1
