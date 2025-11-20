from sortedcontainers import SortedDict
import random

class SparseMatrix:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.data = SortedDict()
        self.is_transposed = False
        self.shape = (rows, cols)

    @classmethod
    def load_from_file(cls, file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()

        rows = len(lines)
        cols = len(lines[0].strip().split())
        matrix = cls(rows, cols)

        for i, line in enumerate(lines):
            for j, value in enumerate(line.strip().split()):
                matrix.insert(i, j, float(value))

        return matrix

    @classmethod
    def random(cls, rows, cols, density=0.2, value_range=(1, 10)):
        matrix = cls(rows, cols)
        non_zero = int(rows * cols * density)

        for _ in range(non_zero):
            while True:
                i = random.randint(0, rows - 1)
                j = random.randint(0, cols - 1)
                if matrix.access(i, j) == 0:
                    value = random.uniform(value_range[0], value_range[1])
                    matrix.insert(i, j, value)
                    break
        return matrix

    def show(self, dense=False):
        if dense:
            for i in range(self.rows):
                row_values = []
                for j in range(self.cols):
                    row_values.append(str(self.access(i, j)))
                print(" ".join(row_values))
        else:
            for r, cols_dict in self.data.items():
                for c, val in cols_dict.items():
                    print(f"({r}, {c}): {val}")

    def _get_coords(self, r, c):
        return (c, r) if self.is_transposed else (r, c)

    def access(self, i, j):
        r, c = self._get_coords(i, j)
        if r not in self.data:
            return 0.0
        return self.data[r].get(c, 0.0)

    def insert(self, i, j, value):
        r, c = self._get_coords(i, j)

        if value == 0:
            if r in self.data and c in self.data[r]:
                del self.data[r][c]
                if len(self.data[r]) == 0:
                    del self.data[r]
            return

        if r not in self.data:
            self.data[r] = SortedDict()
        self.data[r][c] = value

    def transpose(self):
        self.is_transposed = not self.is_transposed
        self.shape = (self.shape[1], self.shape[0])

    def __add__(self, other):
        if not isinstance(other, SparseMatrix):
            raise ValueError("Matrix addition requires another SparseMatrix.")

        if self.shape != other.shape:
            raise ValueError("Matrices must have the same dimension.")

        result = SparseMatrix(self.rows, self.cols)

        for r, cols_dict in self.data.items():
            result.data[r] = SortedDict(cols_dict)

        for r, other_cols in other.data.items():
            if r not in result.data:
                result.data[r] = SortedDict()

            row_ref = result.data[r]

            for c, v in other_cols.items():
                new_value = row_ref.get(c, 0) + v
                if new_value == 0:
                    if c in row_ref:
                        del row_ref[c]
                else:
                    row_ref[c] = new_value

            if len(row_ref) == 0:
                del result.data[r]

        return result

    def _scalar_mul(self, scalar):
        result = SparseMatrix(self.rows, self.cols)

        for r, cols_dict in self.data.items():
            new_row = SortedDict()
            for c, val in cols_dict.items():
                new_val = val * scalar
                if new_val != 0:
                    new_row[c] = new_val

            if len(new_row) > 0:
                result.data[r] = new_row

        return result

    def _matrix_mul(self, other):
        if self.cols != other.rows:
            raise ValueError("Incompatible dimensions for matrix multiplication.")

        result = SparseMatrix(self.rows, other.cols)

        for a_row, a_cols in self.data.items():
            accumulator = SortedDict()

            for a_col, a_val in a_cols.items():
                if a_col not in other.data:
                    continue

                for b_col, b_val in other.data[a_col].items():
                    accumulator[b_col] = accumulator.get(b_col, 0) + a_val * b_val

            non_zero = SortedDict({c: v for c, v in accumulator.items() if v != 0})

            if len(non_zero) > 0:
                result.data[a_row] = non_zero

        return result

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self._scalar_mul(other)
        if isinstance(other, SparseMatrix):
            return self._matrix_mul(other)
        raise NotImplementedError("Unsupported multiplication type.")

    def __rmul__(self, other):
        return self.__mul__(other)
