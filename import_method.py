import random
def cal():
  number_one = random.sample(0,9)
  number_two = random.sample(0,9)
  sum =  number_one + number_two
  print("The sum is: ", sum)

option = eval(input ("1--> to play\n2--> to end"))
while option == 1:
    cal()
    option = eval(input ("1--> to play\n2--> to end"))

    