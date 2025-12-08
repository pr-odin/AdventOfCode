path = "input.txt"
res = 0
count = 0


def compare_arrs(this, other):
    if len(this) != len(other):
        return False

    for i in range(len(this)):
        if this[i] != other[i]:
            return False

    return True


def compare_arrs_list(arr):
    originalArr = arr[0]
    for arrIndex in range(1, len(wordSplits)):
        # print(f"Comparing {originalArr} with {wordSplits[arrIndex]}")
        res = compare_arrs(
            originalArr, wordSplits[arrIndex])
        if not res:
            # print("Returned false compare arrs")
            return False

    return True


with open(path, "r") as lines:
    for line in lines:

        entries = line.split(",")
        for entry in entries:
            count += 1
            # if not (4 < count and count < 6):
            #     continue

            prodIds = entry.split("-")
            startProdId = int(prodIds[0])
            endProdId = int(prodIds[1])
            # print(f"Start: {startProdId}, End: {endProdId}")

            for elem in range(startProdId, endProdId+1):
                # print(f"Elem: {elem}")
                e = str(elem)

                elemLen = len(e)

                halfLen = elemLen // 2

                for i in range(1, halfLen + 1):
                    # print(f"I: {i}")
                    if elemLen % i != 0:
                        continue

                    wordSplits = []
                    c = 0
                    for j in range(elemLen//i):
                        wordSplits.append(e[c:c + i])
                        c = c + i

                    # print(wordSplits)

                    if compare_arrs_list(wordSplits):
                        res += elem
                        # print(f"Item: {elem}")
                        break

print(res)
