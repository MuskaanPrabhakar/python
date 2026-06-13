with open('task.txt', 'r') as file:
    data = file.read().split()

for k in range(len(data)):
    if data[k].isdigit():
        data[k] = int(data[k])

        if data[k] % 2 != 0:
            data[k] *= 2

print(data)