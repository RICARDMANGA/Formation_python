##   Iteration Keywords: for, while, break, continue, pass in Python
#  'for' loop example
for num in range(3):
    if num == 2:
        continue  # Skip number 2
    print(num)
# Output: 0 1

# 'while' loop example
count = 0
while count < 4:
    count += 1
    if count == 3:
        break  # Exit the loop when count reaches 4
    print(count)
# Output: 1 2