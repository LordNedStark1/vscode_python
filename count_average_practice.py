option = eval(input ("Enter 1 to use"
                     "\nEnter 0 to end "))
count = 0
sum = 0
while option == 1:
    numbers_to_sum= eval(input("Enter a number or enter 0 to end "))
    if numbers_to_sum == 0:
        print("The sum is ", sum, "\nTe average is ", average)
        break
    elif numbers_to_sum !=0:
        sum += numbers_to_sum
        count +=1

    average = sum//count


