def findMissing(arr):
   n = len(arr) + 1
   total_sum = n * (n + 1)//2
   sum1 = sum(arr)
   return total_sum - sum1

arr1 = [1]
print(findMissing(arr1))