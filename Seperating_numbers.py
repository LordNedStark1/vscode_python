unseparated_numbers = eval(input("Enter a number "))

def seperating_numbers(number):
    numbers = []
    while number >= 0:
        numbers.append( number % 10)
        number//=10
        
    return numbers
    
def count_number(number):
    count = 0
    while number >= 0:
        number//=10
        count+=1
    return count



# def main():
    print(seperating_numbers(unseparated_numbers))
    print(count_number(unseparated_numbers))



# main()