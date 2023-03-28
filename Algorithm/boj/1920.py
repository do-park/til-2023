N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    result = 0
    st, en = 0, N-1
    while st <= en:
        mid = (st + en) // 2
        if A[mid] < number:
            st = mid + 1
        elif A[mid] > number:
            en = mid - 1
        else:
            result = 1
            break
    print(result)