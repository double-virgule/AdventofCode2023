file_path = "input.txt"
with open(file_path, 'r') as file:
    data = file.readlines()

total_count = 0

for i in data: 
    digits = []
    for j in i:
        if j.isdigit(): 
            digits += j
    if len(digits) == 1: 
        output = digits[0] + digits[0]
    else: 
        output = digits[0] + digits[len(digits)-1]
    total_count += int(output) 

print(total_count)
