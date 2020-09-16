from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    if len(square_matrix) == 0:
        return []
    if len(square_matrix) == 1:
        return square_matrix[0]
    ans = []
    x, y, d = 0, 0, 0
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for _ in range(len(square_matrix) * len(square_matrix[0])):
        ans.append(square_matrix[x][y])
        square_matrix[x][y] = None
        nx, ny = x + direction[d][0], y + direction[d][1]
        if not (0 <= nx < len(square_matrix) and 0 <= ny < len(square_matrix[0]) and square_matrix[nx][ny] is not None):
            d = (d + 1) % 4
            nx, ny = x + direction[d][0], y + direction[d][1]
        x, y = nx, ny
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
