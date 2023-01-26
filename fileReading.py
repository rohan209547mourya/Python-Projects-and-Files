file = open("basic.txt")

data = file.readlines()

print(data)

file.close()

# ===============================

with open('basic.txt') as file:
    output = file.readlines()

print(output)


with open('basic.txt', mode='a') as file:
    file.write("\nhey my name is rohan")

with open('basic.txt') as file:
    output = file.readlines()

print(output)




