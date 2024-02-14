# https://school.programmers.co.kr/learn/courses/30/lessons/120845

def solution(box, n):
    return (box[0] // n) * (box[1] // n) * (box[2] // n)

print(solution([1, 1, 1], 1))
print(solution([10, 8, 6], 3))


###########################
# 다른 사람 풀이 1
def solution(box, n):
    x, y, z = box
    return (x // n) * (y // n) * (z // n )


# 다른 사람 풀이 2
import math
def solution(box, n):
    return math.prod(map(lambda v: v//n, box))