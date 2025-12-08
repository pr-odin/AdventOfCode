startPoint = 50

path = "input1.txt"

with open(path, "r") as lines:
    curr = 50
    res = 0
    for line in lines:
        lineStripped = line.strip()
        direction = lineStripped[:1]
        amountString = lineStripped[1:]

        amountInt = int(amountString)

        if amountInt > 99:
            additional = amountInt // 100
            res += additional

        amount = amountInt % 100

        # print(f"Direction: {direction}, amount:{amount}")
        print(f"-----------------{lineStripped}")

        multiplier = 1

        if direction == "L":
            multiplier = -1

        oldCurr = curr

        curr = curr + (multiplier * amount)

        print(f"Curr: {curr}")

        if oldCurr != 0 and (curr < 0 or 100 < curr):
            res += 1

        print(f"Res: {res}")

        if curr < 0:
            curr = 100 + curr
            curr = abs(curr)
            curr = curr % 100
        else:
            curr = curr % 100

        if curr == 0:
            res = res + 1

        print(f"Res: {res}")

        print(f"Curr end: {curr}")


print(res)
