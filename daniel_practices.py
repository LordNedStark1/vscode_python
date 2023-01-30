unseparated_numbers = eval(input("Enter a number"))

def seperating_numbers(number):
    numbers = []
    while number > -1:
        numbers = number % 10
        number/10
        count+=1
    return numbers
    return count

def main():
    answer= seperating_numbers(unseparated_numbers)
    print(answer)

main()