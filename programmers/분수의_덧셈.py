# https://school.programmers.co.kr/learn/courses/30/lessons/120808

def solution(numer1, denom1, numer2, denom2):

    lst = []

    numer = ((numer1 * denom2) + (numer2 * denom1)) 
    denom = denom1 * denom2

    # 최소 공배수 구하기
    min_com = max(numer, denom) 
    for num in range(min_com, 0, -1):
        if (numer % num == 0) and (denom % num == 0):
            min_com = num
            break 

    answer = [numer//min_com, denom//min_com]
    return answer

solution(1, 2, 3, 4)
solution(9, 2, 1, 3)

################
# 다른 사람 풀이1
import math

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num)
    return [denum//gcd, num//gcd]


# 다른 사람 풀이2
from fractions import Fraction

def solution(denum1, num1, denum2, num2):
    answer = Fraction(denum1, num1) + Fraction(denum2, num2)
    return [answer.numerator, answer.denominator]