path = "input.txt"
res = 0

with open(path, "r") as lines:
    for line in lines:
        entries = line.split(",")
        for entry in entries:
            prodIds = entry.split("-")
            startProdId = int(prodIds[0])
            endProdId = int(prodIds[1])
            # print(f"Start: {startProdId}, End: {endProdId}")

            for elem in range(startProdId, endProdId+1):
                e = str(elem)

                elemLen = len(e)
                if elemLen % 2 != 0:
                    continue

                left = e[:elemLen//2]
                right = e[elemLen//2:]

                # print(f"Left: {left}, right: {right}")
                for i in range(elemLen//2):
                    if left[i] != right[i]:
                        break
                else:
                    res += elem
                    # print(f"Item: {elem}")

print(res)
