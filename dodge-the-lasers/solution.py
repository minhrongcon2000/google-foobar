c = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727

def solve(s):
    if s == 1:
        return 1
    if s < 1:
        return 0
    s1 = (c * s) // (10 ** 100)
    return s * s1 + s * (s + 1) // 2 - s1 * (s1 + 1) // 2 - solve(s1) 

def solution(s):
    return str(solve(int(s)))
