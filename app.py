## <--------------- Ans (6) ------------------------>
# def subsetSum(A, n, k): 
#     if k == 0:
#         return True
 
#     if n < 0 or k < 0:
#         return False
 
#     include = subsetSum(A, n - 1, k - A[n])
#     exclude = subsetSum(A, n - 1, k)
#     return include or exclude 
        
# def Equal_Sum_Partition(arr):
#     sum_of_array = sum(arr)
#     if(sum_of_array %2 == 0):
#         return subsetSum(arr,len(arr)-1,sum_of_array/2)
#     else:
#         return False

# print(Equal_Sum_Partition([1,5,5,12]))

## <--------------- Ans (7) ------------------------>
# def LCS(x,y,m,n):
#     if(n==0 or m==0):
#         return 0
#     if(x[m-1] == y[n-1]):
#         return 1+LCS(x,y,m-1,n-1)
#     else:
#         return max(LCS(x,y,m-1,n),LCS(x,y,m,n-1))

# string_x = "abcdh"
# string_y = "abedfhg"
# string_x_length = len(string_x)
# string_y_length = len(string_y)
# print("[Length of Longest Common Subsequence is ]",LCS(string_x,string_y,string_x_length,string_y_length))


## <--------------- Ans (9) ------------------------> 
# Prefix = [0]
# def repeated_digit(n):
#     a = []      
#     while n != 0:
#         d = n%10
#         if d in a:
#             return 0
#         a.append(d)
#         n = n//10
#     return 1
# def pre_calculation(MAX):
#     global Prefix
#     Prefix.append(repeated_digit(1))
#     for i in range(2,MAX+1):          
#         Prefix.append( repeated_digit(i) +
#                        Prefix[i-1] )
  
# def calculate(L,R):
#     return Prefix[R]-Prefix[L-1]
  
  
# MAX = 1000
# pre_calculation(MAX)
# L=101
# R=200
# print(calculate(L, R))

## <--------------- Ans (10) ------------------------>
# n=int(input())
# j=0
# L=[0 for i in range(n)]
# for i in range(n):
#     a=int(input())
#     if a!=0:
#         L[j]=a
#         j+=1
# for i in L:
#     print(i,end=" ")