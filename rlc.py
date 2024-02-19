def run_rlc(matrix):
    count = 0
    rlc_result = []
    for vector in matrix:
        temp = []
        for i in range(len(vector) - 1):
            if i == 0:
                first = vector[i]
                temp.append(first)
            if vector[i + 1] == 0:
                count += 1
                continue
            else:
                tup = (count, vector[i + 1])
                count = 0
            temp.append(tup)
        rlc_result.append(temp)
    return rlc_result
