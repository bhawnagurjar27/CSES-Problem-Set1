number_of_testcases = int(input())

for _ in range(number_of_testcases):
    N = int(input())
    print(N, end=" ")

    while N > 1:
        if N % 2 == 0:
           N = N // 2
        else:
           N = (3*N)+1 
        
    
        print(N, end=" ")    