# 1

out_file = open('name.txt', 'w')
name = input("What is your name? : ")
out_file.write(name)
out_file.close()

# 2

in_file = open('name.txt', 'r')
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

# 3

in_file = open('numbers.txt', 'r')
num1 = int(in_file.readline())
num2 = int(in_file.readline())
in_file.close()
print(num1 + num2)

# 4

in_file = open('numbers.txt', 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
