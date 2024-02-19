def quantization(channel, table):
    quantization_output = []
    for i in channel:
        matrix_8x8 = []
        for j, qrow in zip(i, table):
            vector_1x8 = []
            for val, q in zip(j, qrow):
                vector_1x8.append(int(val // q))
            matrix_8x8.append(vector_1x8)
        quantization_output.append(matrix_8x8)

    return quantization_output
