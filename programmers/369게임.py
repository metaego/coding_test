def solution(order):
    cnt = 0
    for num in str(order): 
        if num in '369':
            cnt += 1
    return cnt

print(solution(3))
print(solution(29423))