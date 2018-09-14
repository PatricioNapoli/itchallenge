counts = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0
}

with open("input.txt") as f:
    while True:
        c = f.read(1)
        if not c:
            print "End of file"
            break
        counts[c] = counts[c] + 1

print(counts)
