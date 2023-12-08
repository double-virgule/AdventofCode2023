import re

file_path = "input"
with open(file_path, 'r') as file:
    data = file.readlines()

total_count = 0


for i in data: 
    digits = []

    i_replaced = i.replace("one","one1one").replace("two","two2two").replace("three","three3three").replace("four","four4four").replace("five","five5five").replace("six","six6six").replace("seven","seven7seven").replace("eight","eight8eight").replace("nine","nine9nine")

    print(i_replaced)

    for j in i_replaced:
        if j.isdigit(): 
            digits += j
    if len(digits) == 1: 
        output = digits[0] + digits[0]
    else: 
        output = digits[0] + digits[len(digits)-1]
    total_count += int(output) 

print(total_count)
