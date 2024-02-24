# https://school.programmers.co.kr/learn/courses/30/lessons/120905

def solution(n, numlist):
#     answer = []
#     for num in numlist:
#         if num % n != 0:
#             answer.append(num)
    return [num for num in numlist if num % n == 0]

print(solution(3, [4, 5, 6, 7, 8, 9, 10, 11, 12]))