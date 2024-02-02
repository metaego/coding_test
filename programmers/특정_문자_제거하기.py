# https://school.programmers.co.kr/learn/courses/30/lessons/120826

def solution(my_string, letter):
    # answer = ''
    # for str in my_string:
    #     if str != letter:
    #         answer += ''.join(str)
    return ''.join(str for str in my_string if str != letter ) 


print(solution("abcdef", "f"))
print(solution("BCBdbe", "B"))


##########################################
# 다른 사람 풀이
def solution(my_string, letter):
    return my_string.replace(letter, '')