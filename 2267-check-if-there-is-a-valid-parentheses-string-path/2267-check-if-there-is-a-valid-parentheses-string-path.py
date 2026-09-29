class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        path_len = rows + cols - 1
        if path_len % 2 == 1:
            return False
        if grid[0][0] == ")":
            return False
        path = []
        path.append((0, 0, 1))
        visited = set()
        while len(path) > 0:
            row, col, balance = path.pop()
            if balance < 0:
                continue
            state = (row, col, balance)
            if state in visited:
                continue
            visited.add(state)
            if row == rows - 1 and col == cols - 1:
                if balance == 0:
                    return True
                continue
            if col + 1 < cols:
                new_balance = balance
                if grid[row][col + 1] == "(":
                    new_balance += 1
                else:
                    new_balance -= 1
                path.append((row, col + 1, new_balance))
            if row + 1 < rows:
                new_balance = balance
                if grid[row + 1][col] == "(":
                    new_balance += 1
                else:
                    new_balance -= 1
                path.append((row + 1, col, new_balance))
        return False