def get_sum_before_0(numbers):
   sum = 0
   for number in numbers:
       if number == 0:
          break
       sum = sum + number
   return sum
       
list_of_numbers = [4, 4, 3, 5, 0, 6, 7]
print get_sum_before_0(list_of_numbers)


