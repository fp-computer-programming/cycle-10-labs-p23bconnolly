# lab 10-2

x = []

while True:
    input_number = int(input("Input number here: "))
    if input_number == -1:
        break
    elif input_number % 3 == 0:
        x.append(input_number)
    else:
        continue

print("Multiples of 3: ", x)