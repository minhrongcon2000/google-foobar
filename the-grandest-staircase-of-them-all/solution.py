def solution(n):
    num_rows = n + 1
    num_cols = n - 1
    
    sol_table = [[None for _ in range(num_cols)] for _ in range(num_rows)]
    
    for i in range(num_rows):
        for j in range(num_cols):
            if i == 0:
                sol_table[i][j] = 0
            elif i == 1:
                sol_table[i][j] = 1
            elif i == 2:
                sol_table[i][j] = 1 if j >= 1 else 0
            elif j == 0:
                sol_table[i][j] = 1 if i == 1 else 0
            else:
                if i < j + 1:
                    sol_table[i][j] = sol_table[i][j - 1]
                elif i == j + 1:
                    sol_table[i][j] = sol_table[i][j - 1] + 1
                else:
                    sol_table[i][j] = sol_table[i][j - 1] + sol_table[i - j - 1][j - 1]
            
    return sol_table[-1][-1]
