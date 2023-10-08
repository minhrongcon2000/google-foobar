def calculate_xor_first_n(n):
    if n % 4 == 0:
        return n
    
    if n % 4 == 1:
        return 1
    
    if n % 4 == 2:
        return n + 1
    
    return 0

def calculate_xor_from_i_to_j(i, j):
    return calculate_xor_first_n(j) ^ calculate_xor_first_n(i)

def solution(start, length):
    end = start + length * length - 1
    
    all_xor = calculate_xor_from_i_to_j(start - 1, end)
    
    for i in range(length):
        start_pos = start + i * length
        end_pos = start + i * length + length - 1
        
        remove_part = calculate_xor_from_i_to_j(start_pos - 1, end_pos) ^ calculate_xor_from_i_to_j(start_pos - 1, end_pos - i)
        
        all_xor ^= remove_part
        
    return all_xor