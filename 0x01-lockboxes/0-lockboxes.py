def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes: A list of lists representing the boxes and their keys.

    Returns:
        True if all boxes can be opened,    else False.
    """
    n = len(boxes)
    opened = set()  # Set to keep track of opened boxes
    keys = set([0])  # Start with key to box 0

    def dfs(box):
        if box in opened:
            return
        opened.add(box)
        for key in boxes[box]:
            keys.add(key)
        for key in keys.copy():  # Use copy to avoid modifying set during iteration
            if key < n and key not in opened:
                dfs(key)

    dfs(0)  # Start DFS from box 0
    return len(opened) == n