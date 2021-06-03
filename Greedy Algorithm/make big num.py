def solution(number, k):
    # stack에 입력값을 순서대로 삽입
    stack = [number[0]]
    for num in number[1:]:
        print(stack, num, k)
        while len(stack) > 0 and stack[-1] < num and k > 0:
            # 값을 한개 빼서 k는 1이 제거
            k -= 1
            # 내부의 값을 제거
            stack.pop()
        # 새로운 값을 삽입
        stack.append(num)

    if k != 0:
        stack = stack[:-k]

    return ''.join(stack)