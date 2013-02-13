n_str = "4"
n = int(n_str)
result = 1
for i in range(1, n+1):
  result *= i
  print 'We multiply our current result by ' + str(i) ' to get ' + str(result)

print str(n) + ' factorial is ' + str(result)
