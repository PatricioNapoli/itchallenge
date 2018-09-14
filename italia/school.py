counts = {
    "p": 0,
    "c": 0,
    "m": 0,
    "b": 0,
    "z": 0
}

with open("input.txt") as f:
    while True:
        c = f.read(1)
        if not c:
            print "End of file"
            break
        counts[c] = counts[c] + 1

print(counts)
