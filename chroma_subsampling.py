# 4:2:0
import numpy as np


def chroma_subsampling(matrix):
    result = []

    for block in matrix:
        temp = np.array(block)
        temp[1::2, :] = temp[::2, :]
        temp[:, 1::2] = temp[:, ::2]
        result.append(temp.tolist())

    return result
