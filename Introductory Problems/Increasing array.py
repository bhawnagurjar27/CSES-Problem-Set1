number_of_testcases = int(input())

for _ in range(number_of_testcases):

    N = int(input())
    array = list(map(int, input().split()))
    count=0
    for i in range(N):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], arr[j]
                count = count + 1
    
    print(count + 1)            