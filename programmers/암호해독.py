# https://school.programmers.co.kr/learn/courses/30/lessons/120892

def solution(cipher, code):
    return ''.join(cipher[code * num -1] for num in range(1, int(len(cipher)/code +1)))

print(solution("dfjardstddetckdaccccdegk", 4))
print(solution("pfqallllabwaoclk", 2))

###############################
# 다른 사람 풀이 1
def solution(cipher, code):
    return cipher[code-1::code]

# 다른 사람 풀이 2
def solution(cipher, code):
    return ''.join(cipher[i] for i in range(code-1,len(cipher),code))