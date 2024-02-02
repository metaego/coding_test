# https://school.programmers.co.kr/learn/courses/30/lessons/120830

def solution(n, k):
    lamb_skewer_price = n * 12_000
    if n >= 10:
        k -= (n // 10)
        if k < 0:
            k = 0

    total_price = lamb_skewer_price + k * 2_000
    return total_price

print(solution(10, 3))
print(solution(64, 6))

###########################
# 다른 사람 풀이 1
def solution(n, k):
    return (n*12000)+(k*2000)-((n//10)*2000)


# 다른 사람 풀이 2
def solution(n, k):
    service = n//10
    drink = max(0, k-service)
    return (12000*n)+(2000*drink)

