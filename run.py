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
        location1 = values[1]
        location2 = values[2]
        d1 = memory[int(location1)]
        d2 = memory[int(location2)]
        add = int(d1) + int(d2)
        memory.append(add)

    if command == "o":
        place = bar[2:]
        print(memory[int(place)])
