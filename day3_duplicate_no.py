def findMissing(arr):
   n = len(arr) - 1
   total_sum = n * (n + 1)//2
   sum1 = sum(arr)
   return sum1 - total_sum

arr1 = [1, 3, 4, 2, 2]
print(findMissing(arr1))