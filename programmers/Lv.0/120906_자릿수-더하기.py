def solution(n):
    answer = 0
    while True :
        if n != 0 :
            answer += n % 10
            n = (n - n % 10) / 10
        else :
            break
    return answer
