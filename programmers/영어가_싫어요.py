# https://school.programmers.co.kr/learn/courses/30/lessons/120894

def solution(numbers):
    temp_str = ''
    answer = ''
    eng_num = [ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for chr in numbers:
        temp_str += chr
        if temp_str in eng_num:
            answer += str(eng_num.index(temp_str))
            temp_str = ''
    return int(answer)

print(solution('onetwothreefourfivesixseveneightnine'))
print(solution("onefourzerosixseven"))

#####################################
# 다른 사람 풀이 1
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)


# 다른 사람 풀이 2
def solution(numbers):
    r = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',\
         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for k in r.keys():
        numbers = numbers.replace(k, r[k])

    return int(numbers)