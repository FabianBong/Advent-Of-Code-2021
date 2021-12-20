import numpy as np


def expand(img):
    expanded = np.zeros((img.shape[0] + 2, img.shape[1] + 2), dtype='u2') + rest_of_img
    expanded[1:-1, 1:-1] = img
    return expanded


def calc_pixel(image, i, j):
    pix_string = image[i - 1][j - 1] << 8 | image[i - 1][j] << 7 | image[i - 1][j + 1] << 6 | image[i][j - 1] << 5 | \
                 image[i][j] << 4 | image[i][j + 1] << 3 | image[i + 1][j - 1] << 2 | image[i + 1][j] << 1 | \
                 image[i + 1][j + 1]
    return pix_string


with open("/Users/fabianbong/Documents/Advent_Of_Code/Day_20/input.txt") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

algo_string = lines[0].replace('#', '1').replace('.', '0')
algo_string = [int(c) for c in algo_string]

image = lines
del image[0]
del image[0]
rest_of_img = 0

## extend the image
np_img = np.array([[c == '#' for c in line.strip()] for line in image], dtype='u2')
np_img = expand(np_img)

for _ in range(2):
    np_img = expand(np_img)
    rep_map = [["0"]*len(np_img[0]-1) for _ in range(len(np_img)-1)]
    for i in range(1, len(np_img) - 1):
        for j in range(1, len(np_img[0]) - 1):
            rep_map[i][j] = calc_pixel(np_img,i,j)

    rest_of_img = algo_string[0] if rest_of_img == 0 else algo_string[511]
    np_img[:, :] = rest_of_img
    for i in range(1, len(np_img) - 1):
        for j in range(1, len(np_img[0]) - 1):
            np_img[i, j] = algo_string[rep_map[i][j]]


print(np.count_nonzero(np_img))

