# https://school.programmers.co.kr/learn/courses/30/lessons/120849

def solution(my_string):
    answer = ''
    for chr in my_string:
        if chr not in ['a', 'e', 'i', 'o', 'u']:
            answer += chr
    return answer

print(solution("bus"))
print(solution("nice to meet you"))

#################################################
# 다른 사람 풀이 1
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])

# 다른 사람 풀이 2
def solution(my_string):
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string

# 다른 사람 풀이 3
import re
def solution(my_string):
    return re.sub('[aeiou]', '', my_string)