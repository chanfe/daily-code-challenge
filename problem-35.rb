#Given an array of strictly the characters 'R', 'G', and 'B', segregate the
#values of the array so that all the Rs come first, the Gs come second, and
#the Bs come last. You can only swap elements of the array.
#Do this in linear time and in-place.
#For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
#it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

def RGB_placer(arr)
  front = 0
  pos = 0
  back = arr.length - 1
  while pos < back + 1
    if arr[pos] == 'R'
      temp = arr[front]
      arr[front] = arr[pos]
      arr[pos] = temp
      front+= 1
    elsif arr[pos] == 'B'
      temp = arr[back]
      arr[back] = arr[pos]
      arr[pos] = temp
      back -= 1
    end
    if arr[pos] == 'G'
      pos += 1
    end
  end
  arr
end

arr1 = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
print(arr1)
puts
print(RGB_placer(arr1))
puts
