def sort_012(arr):
   len_array = len(arr)
   i, left, right = 0, 0, len_array -1

   while i <= right:
      if arr[i] == 0:
         arr[left], arr[i] = arr[i], arr[left]
         left +=1
         i +=1

      elif arr[i] == 2:
         arr[right], arr[i] = arr[i], arr[right]
         right -=1

      else:
         i +=1


arr1 = [0,0,0,0,0]
print("before: ", arr1)
sort_012(arr1)
print("sorted: ", arr1)