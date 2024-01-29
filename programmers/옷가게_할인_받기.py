# https://school.programmers.co.kr/learn/courses/30/lessons/120818

def solution(price):
    if price >= 500_000:
        answer = int(price - (price * 0.2))
    elif price >= 300_000:
        answer = int(price - (price * 0.1))
    elif price >= 100_000:
        answer = int(price - (price * 0.05))
    else:
        answer = price
    return answer


print(solution(150000))
print(solution(580000))

##########################################################
# 다른 사람 풀이 1
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)



# 다른 사람 풀이 2
def solution(price):
    if price>=500000:
        price = price *0.8
    elif price>=300000:
        price = price *0.9
    elif price>=100000:
        price = price * 0.95
    return int(price)