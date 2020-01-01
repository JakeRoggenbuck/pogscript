memory = []
with open('app.txt', 'r') as file:
    data = file.read().replace('\n', '')
    new = data.replace(' ', '')
    codeslice = new.rsplit(">")
    
for x in range(len(codeslice)):
    bar = codeslice[x]
    command = bar[0]

    if command == "v":
        memory.append(bar[2:])

    if command == "a":
        values = bar.rsplit("{")
        add = int(memory[int(values[1])]) + int(memory[int(values[2])])
        memory.append(add)

    if command == "s":
        values = bar.rsplit("{")
        subtract = int(memory[int(values[1])]) - int(memory[int(values[2])])
        memory.append(subtract)

    if command == "m":
        values = bar.rsplit("{")
        multiply = int(memory[int(values[1])]) * int(memory[int(values[2])])
        memory.append(multiply)

    if command == "d":
        values = bar.rsplit("{")
        divide = int(memory[int(values[1])]) / int(memory[int(values[2])])
        memory.append(divide)

    if command == "p":
        values = bar.rsplit("{")
        press = str(memory[int(values[1])]) + str(memory[int(values[2])])
        memory.append(press)

    if command == "c":
        char = chr(int(memory[int(bar[2:])]))
        memory.append(char)

    if command == "o":
        place = bar[2:]
        print(memory[int(place)])
