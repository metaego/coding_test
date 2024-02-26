# https://school.programmers.co.kr/learn/courses/30/lessons/120893

def solution(my_string):
    answer = ''
    for chr in my_string:
        if  chr in 'abcdefghijklmnopqrstuvwxyz':
            answer += chr.upper()
        else:
            answer += chr.lower()
    return answer

print(solution("cccCCC"))
print(solution("abCdEfghIJ"))

##########################################
# 다른 사람 풀이 1
def solution(my_string):
    return ''.join([x.lower() if x.isupper() else x.upper() for x in my_string])



# 다른 사람 풀이 2
def solution(my_string):
    answer = ''

    for i in my_string:
        if i.isupper():
            answer+=i.lower()
        else:
            answer+=i.upper()
    return answer



# 다른 사람 풀이 3
def solution(my_string):
    return my_string.swapcase()