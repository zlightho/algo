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
    def increment_ages(tree: List[List[int]]):
        """
        Increment the age of each cell in the tree by 1.
        
        Args:
            tree (List[List[int]]): The current tree state as a list of lists with integer values.
        """
        for row in range(H):
            for col in range(W):
                tree[row][col] += 1
                
    def kill_trees(tree: List[List[int]]):
        """
        Remove tree branches that are 3 or more years old, along with their neighbors.
        
        Args:
            tree (List[List[int]]): The current tree state as a list of lists with integer values.
        """
        to_kill = []
        for row in range(H):
            for col in range(W):
                if tree[row][col] >= 3:
                    to_kill.append((row, col))
                    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        r, c = row + dr, col + dc
                        if 0 <= r < H and 0 <= c < W:
                            to_kill.append((r, c))
        for r, c in to_kill:
            tree[r][c] = 0

    def add_new_branches(tree: List[List[int]]):
        """
        Add new tree branches with an age of 1 in empty cells.
        
        Args:
            tree (List[List[int]]): The current tree state as a list of lists with integer values.
        """
        for row in range(H):
            for col in range(W):
                if tree[row][col] == 0:
                    tree[row][col] = 1
                    
    def tree_to_str(tree: List[List[int]]) -> List[str]:
        """
        Convert the tree with integer values to a list of strings with "." and "+" characters.
        
        Args:
            tree (List[List[int]]): The current tree state as a list of lists with integer values.
            
        Returns:
            List[str]: The tree state as a list of strings with "." and "+" characters.
        """
        return [''.join('+' if cell > 0 else '.' for cell in row) for row in tree]

    int_tree = [[1 if cell == '+' else 0 for cell in row] for row in tree]

    for year in range(1, N + 1):
        increment_ages(int_tree)
        if year % 2 == 0:
            add_new_branches(int_tree)
        else:
            kill_trees(int_tree)
            
    return tree_to_str(int_tree)
