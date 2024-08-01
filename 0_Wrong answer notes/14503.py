def clean_room(n,m,r,c,d,grid) :
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    cleaned = [[False] * m for _ in range(n)]
    cleaned_count = 0
    
    while True :
        if not cleaned[r][c] :
            cleaned[r][c] = True
            cleaned_count += 1
            
        cleaned_or_wall_around = True
        
        for _ in range(4) :
            d = (d + 3) % 4
            nx = r + dx[d]
            ny = c + dy[d]
            
            if 0 <= nx < n and 0 <= ny < m and not cleaned[nx][ny] and grid[nx][ny] == 0 :
                r,c = nx , ny
                cleaned_or_wall_around = False
                break
            
        if cleaned_or_wall_around :
            back_direction = (d+2) % 4
            br = r + dx[back_direction]
            bc = c + dy[back_direction]
            
            if 0 <= br < n and 0 <= bc < m and grid[br][bc] == 0 :
                
                r,c = br , bc
                
            else :
                break
            
    return cleaned_count
                
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n,m = map(int,input().split())
    r,c,d = map(int,input().split())
    grid = [list(map(int,input().split())) for _ in range(n)]

    result = clean_room(n, m, r, c, d, grid)
    print(result)