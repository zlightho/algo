from typing import List

def TreeOfLife(H: int, W: int, N: int, tree: List[str]) -> List[str]:
    """
    Simulate the growth of a tree for N years and return the final state as a list of strings.
    
    Args:
        H (int): The height of the tree.
        W (int): The width of the tree.
        N (int): The number of years to simulate.
        tree (List[str]): The initial state of the tree as a list of strings with "." and "+" characters.
        
    Returns:
        List[str]: The final state of the tree after N years as a list of strings with "." and "+" characters.
    """
    def increment_ages(int_tree: List[List[int]]) -> None:
        """
        Increment the age of each cell in the tree by 1.
        
        Args:
            tree (List[List[int]]): The current tree state as a list of lists with integer values.
        """
        for row in range(H):
            for col in range(W):
                int_tree[row][col] += 1

    def add_new_branches(int_tree: List[List[int]]) -> None:
        """
        Add new tree branches with an age of 1 in empty cells.
        
        Args:
            tree (List[List[int]]): The current tree state as a list of lists with integer values.
        """
        for row in range(H):
            for col in range(W):
                if int_tree[row][col] == 0:
                    int_tree[row][col] = 1

    def kill_trees(int_tree: List[List[int]]) -> None:
        """
        Remove tree branches that are 3 or more years old, along with their neighbors.
        
        Args:
            tree (List[List[int]]): The current tree state as a list of lists with integer values.
        """
        to_kill = []

        for row in range(H):
            for col in range(W):
                if int_tree[row][col] >= 3:
                    to_kill.append((row, col))
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        r, c = row + dr, col + dc
                        if 0 <= r < H and 0 <= c < W:
                            to_kill.append((r, c))

        for row, col in to_kill:
            int_tree[row][col] = 0

    def int_tree_to_str_list(int_tree: List[List[int]]) -> List[str]:
        """Convert the integer tree representation to a list of strings with '+' and '.' symbols."""
        return [''.join('+' if cell > 0 else '.' for cell in row) for row in int_tree]

    int_tree = [[1 if cell == '+' else 0 for cell in row] for row in tree]

    for year in range(1, N + 1):
        increment_ages(int_tree)
        if year % 2 == 0:
            add_new_branches(int_tree)
        kill_trees(int_tree)

    return int_tree_to_str_list(int_tree)
