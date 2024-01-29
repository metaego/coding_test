# https://school.programmers.co.kr/learn/courses/30/lessons/120819

def solution(money):
    answer = []
    answer.append(money // 5500)
    answer.append(money % 5500)
    return answer


print(solution(5_500))
print(solution(15_000))


###############################
# 다른 사람 풀이_1
def solution(money):
    return [money // 5500, money % 5500]


# 다른 사람 풀이_2
def solution(money):
    return divmod(money, 5500)