# Add spelled letters

file_path = "C:/Data/AdventofCode2023/Day1/input.txt"
with open(file_path, 'r') as file:
    data = file.readlines()

total_count = 0

words = ["one","two","three","four","five","six","seven","eight","nine"]

for i in data: 
    digits = []
    if words[0] in i: 
        print(words[0])
    for j in i:
        if j.isdigit(): 
            digits += j
    if len(digits) == 1: 
        output = digits[0] + digits[0]
    else: 
        output = digits[0] + digits[len(digits)-1]
    total_count += int(output) 

print(total_count)
    
    
