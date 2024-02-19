from scipy import fft
from quantization import quantization
from chroma_subsampling import chroma_subsampling

from convert_image_to_matrix import convert_image_to_matrix
from create_block import create_blocks
from dpcm import run_dpcm
from rlc import run_rlc
from save_output import save_result
from zigzag_traverse import zigzag_traverse

image = "test1.png"


LUMINANCE_QUANTIZATION_TABLE = [
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99],
]

CHROMINANCE_QUANTIZATION_TABLE = [
    [17, 18, 24, 47, 99, 99, 99, 99],
    [18, 21, 26, 66, 99, 99, 99, 99],
    [24, 26, 56, 99, 99, 99, 99, 99],
    [47, 66, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
]

image_matrix = convert_image_to_matrix(image)

y_channel = []
for tup in image_matrix:
    result = tup[0] * 0.299 + tup[1] * 0.587 + tup[2] * 0.114
    y_channel.append(result)


cb_channel = []
for tup, y in zip(image_matrix, y_channel):
    result = ((tup[2] - y) / 1.772) + 0.5
    cb_channel.append(result)

cr_channel = []
for tup, y in zip(image_matrix, y_channel):
    result = ((tup[0] - y) / 1.402) + 0.5
    cr_channel.append(result)

y_blocks = create_blocks(y_channel)
cb_blocks = create_blocks(cb_channel)
cr_blocks = create_blocks(cr_channel)


cb_chroma_result = chroma_subsampling(cb_blocks)
cr_chroma_result = chroma_subsampling(cr_blocks)

y_dct_result = fft.dct(y_blocks)
cb_dct_result = fft.dct(cb_chroma_result)
cr_dct_result = fft.dct(cr_chroma_result)


y_quantized = quantization(y_dct_result, LUMINANCE_QUANTIZATION_TABLE)
cb_quantized = quantization(cb_dct_result, CHROMINANCE_QUANTIZATION_TABLE)
cr_quantized = quantization(cr_dct_result, CHROMINANCE_QUANTIZATION_TABLE)


zigzag_y = zigzag_traverse(y_quantized)
zigzag_cb = zigzag_traverse(cb_quantized)
zigzag_cr = zigzag_traverse(cr_quantized)


y_dc_coefficient = run_dpcm(zigzag_y)
cb_dc_coefficient = run_dpcm(zigzag_cb)
cr_dc_coefficient = run_dpcm(zigzag_cr)


y_rlc_coefficient = run_rlc(zigzag_y)
cb_rlc_coefficient = run_rlc(zigzag_cb)
cr_rlc_coefficient = run_rlc(zigzag_cr)


list_result = [
    y_dc_coefficient,
    cb_dc_coefficient,
    cr_dc_coefficient,
    y_rlc_coefficient,
    cb_rlc_coefficient,
    cr_rlc_coefficient,
]

name_list_result = [
    "result_y_dc_coefficient",
    "result_cb_dc_coefficient",
    "result_cr_dc_coefficient",
    "result_y_rlc_coefficient",
    "result_cb_rlc_coefficient",
    "result_cr_rlc_coefficient",
]

for index, result in enumerate(list_result):
    save_result(f"{name_list_result[index]}.txt", result)
