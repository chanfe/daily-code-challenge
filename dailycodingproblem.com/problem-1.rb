#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#Bonus: Can you do this in one pass?

def problem(arr, k)
  answer = false
  numberlist = {} # the hash to store number
  for i in arr # loop only once
    if numberlist[k-i] #check if the number is in the hash if so we found the answer
      answer = true
      puts i, k-i
    else #if not place the number in the hashlist
      numberlist[i] = true
    end
  end
  answer
end

arr1 = [10, 15, 3, 7]
arr2 = [1,2,3,4]

puts(problem(arr1,17))
puts(problem(arr1,16))
puts(problem(arr2,4))
puts(problem(arr2,3))
