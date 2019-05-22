class BoardHelper:
    VECS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
            (-1, 1)]
    STONES = [1, -1]
    EMPTY_STONE = 0

    @classmethod
    def can_put(cls, squares, stone, x, y):
        if squares[y][x] != cls.EMPTY_STONE:
            return False

        for vec in cls.VECS:
            i = x
            j = y
            try:
                i += vec[0]
                j += vec[1]
                if i < 0 or j < 0:
                    raise IndexError(f"i: {i}, j: {j}")
                if squares[j][i] in (stone, cls.EMPTY_STONE):
                    continue
                while True:
                    i += vec[0]
                    j += vec[1]
                    if i < 0 or j < 0:
                        raise IndexError(f"i: {i}, j: {j}")
                    if squares[j][i] == stone:
                        return True
                    elif squares[j][i] == cls.EMPTY_STONE:
                        break
            except IndexError:
                continue

        return False

    @classmethod
    def get_can_put_list(cls, squares, stone):
        can_put_list = []
        for x in range(8):
            for y in range(8):
                if cls.can_put(squares, stone, x, y):
                    can_put_list.append((x, y))
        return can_put_list
