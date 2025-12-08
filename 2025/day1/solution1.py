startPoint = 50

path = "input1.txt"

with open(path, "r") as lines:
    curr = 50
    res = 0
    for line in lines:
        lineStripped = line.strip()
        direction = lineStripped[:1]
        amountString = lineStripped[1:]
        amount = int(amountString) % 100

        multiplier = 1

        if direction == "L":
            multiplier = -1

        curr = curr + (multiplier * amount)

        if curr < 0:
            curr = 100 + curr
            curr = abs(curr)
            curr = curr % 100
        else:
            curr = curr % 100

        if curr == 0:
            res = res + 1

        print(f"Result: {curr}")

        print(f"Direction: {direction}, amount:{amount}")

print(res)
