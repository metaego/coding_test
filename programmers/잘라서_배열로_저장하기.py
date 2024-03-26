# https://school.programmers.co.kr/learn/courses/30/lessons/120913

# def solution(my_str, n):
#     answer = []
#     start = 0
#     end = n
#     for num in range(int(len(my_str) // n) + 1):
#         print(num)
#         start = num * n
#         end = (num + 1) * n
#         answer.append(my_str[start:end])
#         print('my_str[start:end]: ', my_str[start:end])
#         print('start:', start, 'end: ', end)
#     return answer

# print(solution("abc1Addfggg4556b", 6))

# my_str = "abc1Addfggg4556b"
# n = 6
# # print(list(range(int(len(my_str) // n))))