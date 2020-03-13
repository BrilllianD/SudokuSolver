z = 0
input = [[3, 4, z, z, 2, 6, z, 8, z],
         [z, z, 1, z, 7, z, z, z, z],
         [7, 2, z, 8, z, z, 4, 3, 9],
         [4, z, 9, 6, z, z, 3, z, 2],
         [z, z, z, z, 1, 9, z, 7, z],
         [1, z, z, z, z, 4, 9, z, z],
         [z, z, z, 5, 6, 8, z, z, 7],
         [z, z, z, z, z, 2, z, z, 5],
         [2, 5, 4, z, 9, 7, 8, 6, 3]]

count_z = 0

for x in range(9):
    for y in range(9):
        if input[x][y] == z:
            count_z += 1

variants = [[set() for j in range(9)] for i in range(9)]

while True:
    for x in range(9):
        for y in range(9):

            if input[x][y] == z:

                if len(variants[x][y]) == 0:
                    variant = {1, 2, 3, 4, 5, 6, 7, 8, 9}

                    for I in range(9):
                        if input[x][I] != z and input[x][I] in variant:
                            variant.remove(input[x][I])

                    for I in range(9):
                        if input[I][y] != z and input[I][y] in variant:
                            variant.remove(input[I][y])

                    variants[x][y] = variant

                if len(variants[x][y]) == 1:
                    input[x][y] = variants[x][y].pop()
                    count_z -= 1

                    print(f'detect [{x}][{y}] -> {input[x][y]}')

                    for I in range(9):
                        if len(variants[x][I]) > 1 and input[x][y] in variants[x][I]:
                            variants[x][I].remove(input[x][y])

                    for I in range(9):
                        if len(variants[I][y]) > 1 and input[x][y] in variants[I][y]:
                            variants[I][y].remove(input[x][y])

                else:
                    block_x = x // 3
                    block_y = y // 3

                    for I in range(3):
                        for J in range(3):

                            v = input[block_x * 3 + I][block_y * 3 + J]
                            if v in variants[x][y]:
                                variants[x][y].remove(v)

    if count_z == 0:
        break

for x in range(9):
    print(input[x])
