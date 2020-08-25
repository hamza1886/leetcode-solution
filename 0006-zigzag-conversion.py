# see: https://leetcode.com/problems/zigzag-conversion/

class Solution:
    is_print: bool = True

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            if self.is_print:
                print('   ', end='')
                [print(f'{i % 10} ', end='') for i in range(len(s))]
                print('\n0: ', end='')
                [print(f'{c} ', end='') for c in s]
                print()
            return s

        rows = numRows
        cols = len(s)
        idx = 0

        x = [[''] * cols for _ in range(rows)]

        for c in range(cols):
            for r in range(rows):
                if idx == len(s):
                    if self.is_print:
                        self.pretty_print(x)
                    return ''.join([''.join(x[r]) for r in range(len(x))])

                if c % (rows - 1) == 0:
                    x[r][c] = s[idx]
                    idx += 1
                else:
                    if (r + c) % (rows - 1) == 0:
                        x[r][c] = s[idx]
                        idx += 1
                        continue

    def pretty_print(self, x: list) -> None:
        rows = len(x)
        cols = len(x[0])

        print('   0 1 2 3 4 5 6')
        for i in range(rows):
            print(f'{i}: ', end='')
            for j in range(cols):
                c = x[i][j] if x[i][j] != '' else ' '
                print(f'{c} ', end='')
            print()


if __name__ == '__main__':
    solution = Solution()
    print(solution.convert('PAYPALISHIRING', 1))  # PAYPALISHIRING
    print(solution.convert('PAYPALISHIRING', 2))  # PYAIHRNAPLSIIG
    print(solution.convert('PAYPALISHIRING', 3))  # PAHNAPLSIIGYIR
    print(solution.convert('PAYPALISHIRING', 4))  # PINALSIGYAHRPI
    print(solution.convert('PAYPALISHIRING', 5))  # PHASIYIRPLIGAN
