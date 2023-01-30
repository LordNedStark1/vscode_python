n = eval(input("Enter an integer >= 2: "))
found = False
factor = 2
while factor <= n and not found:
  if n % factor == 0:
    found = True
  else:
    factor += 1
print("The smallest factor other than 1 for", n, "is", factor)