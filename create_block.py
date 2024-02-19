def create_blocks(channel):
    total_image_pixels = len(channel)

    for i in range(64 - (total_image_pixels % 64)):
        channel.append(0)

    result_blocks = []
    row = []
    inner = []
    row_num = 0
    col_num = 0
    for pixel in channel:
        if col_num == 8:
            result_blocks.append(inner)
            inner = []
            col_num = 0
        else:
            if row_num == 8:
                inner.append(row)
                row = []
                row_num = 0
                col_num += 1
            else:
                row.append(pixel - 128)
                row_num += 1

    return result_blocks
