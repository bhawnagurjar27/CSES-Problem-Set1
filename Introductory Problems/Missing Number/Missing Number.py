number_of testcases = int(input())

for _ in range(number_of_testcases):
   N = int(input())
   array = list(map(int, input().split()))
   sum1 = 0
   sum2 = 0
   sum3 = 0
   sum1 = N*(N+1) // 2
   #print(sum1)

   for i in range(0, N-1):
      sum2=sum2 +array[i]
   #print(sum2)    

   sum3 = sum1 - sum2
   print(sum3)