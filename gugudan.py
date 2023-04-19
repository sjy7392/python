def gugudan(n):
    result = []    # 구구단 결과를 저장할 리스트 생성
    for i in range(1, 10):
        result.append(f"{n} x {i} = {n*i}")    # 구구단 계산식을 리스트에 추가
    return result    # 구구단 결과 리스트 반환

def print_gugudan(n):
    for i in gugudan(n):    # gugudan 함수를 호출하여 리스트 반환
        print(i)    # 리스트의 요소를 출력
    print()    # 한 줄 띄우기
    
print_gugudan(3)
