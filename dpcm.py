def run_dpcm(zz_matrix):
    dc_coefficient = []
    for vector in range(len(zz_matrix)):
        result = []
        if vector == 0:
            result = zz_matrix[vector].copy()
            dc_coefficient.append(result)
            continue
        for i in range(len(zz_matrix[vector])):
            result.append(zz_matrix[vector][i] - zz_matrix[vector - 1][i])
        dc_coefficient.append(result)
    return dc_coefficient
