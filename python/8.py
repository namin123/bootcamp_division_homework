"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    n=int(input())
    sum_n=0
    fact=1

    for i in range(1,n+1):
        sum_n +=i
        fact*=i

    print(sum_n)
    print(fact)
    return


if __name__ == '__main__':
    main()
