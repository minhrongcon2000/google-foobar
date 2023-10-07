def solution(L):
    digit_freq = [0 for _ in range(10)]
    
    s = 0
    
    for item in L:
        digit_freq[item] += 1
        s = (s + item) % 3
        
    if s != 0:
        found = True
        
        for i in [2, 5, 8] if s == 2 else [1, 4, 7]:
            if digit_freq[i] > 0:
                digit_freq[i] -= 1
                found = True
                break
            
        if not found:
            decreaseTime = 0
            for i in [1, 4, 7] if s == 2 else [2, 5, 8]:
                while digit_freq[i] > 0 and decreaseTime < 2:
                    digit_freq[i] -= 1
                    decreaseTime += 1
                    
                if decreaseTime == 2:
                    break
                
    
    output = ""
    for i in range(9, -1, -1):
        output += str(i) * digit_freq[i]
        
    if output.startswith("0"):
        return 0
    return int(output)

    