# number_to_check=[12,2,3,4,5,6,7,17,5,4,23]
numbers_list = [3,4,4,5,5,3,6,1,2,]

def largest_number_check(listr : list):
    largest_number = listr[0]
    for i in range(len(listr)):
        if listr[i] > listr[0]:
            largest_number = listr[i]
    return largest_number

print (largest_number_check(numbers_list))

def reverse_list(listr : list):
    numbers = []
    for i in range (len(listr)):
        numbers.append(listr[len(listr)-1])
        
    return numbers

# print(reverse_list(numbers_list))
print(numbers_list)

def check_element_occurs(number, listr :list):
    for i in range(len(listr)):
        if number == listr[i]:
            return True
print(check_element_occurs(3, numbers_list))

def print_odd_index(listr : list):
    for i in range(1,len(listr), +2):
        print(listr[i])

print_odd_index(numbers_list)

def print_even_index(listr : list):
    for i in range(0, len(listr), +2):
        print(listr[i])
print("The even list")
print_even_index(numbers_list)

def sum_with_forloop(listr : list):
    sum =0
    for i in range(len(listr)):
        sum = sum + listr[i]
    return sum
print(sum_with_forloop(numbers_list))

