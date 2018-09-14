routers = []

class Router:
    def __init__(self, pos, range):
        self.pos = int(pos)
        self.range = int(range)

    def in_range(self, otherRouter):
        if otherRouter.pos == self.pos:
            return False

        selfSignalUp = self.pos + self.range # 550
        selfSignalDown = self.pos - self.range # 450

        routerSignalUp = otherRouter.pos + otherRouter.range
        routerSignalDown = otherRouter.pos - otherRouter.range

        if selfSignalUp >= routerSignalUp >= selfSignalDown and selfSignalDown <= routerSignalDown <= selfSignalUp:
            return True

        return False

with open("input1.txt") as fp:
    line = fp.readline()

    while line:
        parts = line.split(" ")
        router = Router(parts[0], parts[1])
        routers.append(router)
        line = fp.readline()

with open("input2.txt") as fp:
    line = fp.readline()
    parts = line.split(" ")

    overlaps = []

    for query in parts:
        overlap_count = 0
        router = routers[int(query)]

        for r in routers:
            if router.in_range(r):
                overlap_count = overlap_count + 1

        overlaps.append(str(overlap_count))

    print("".join(overlaps))
