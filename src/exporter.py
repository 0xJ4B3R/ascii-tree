import os
from typing import List, Optional


def generate_tree(
    start_path: str, prefix: str = "", exclude: Optional[set] = None
) -> List[str]:
    """
    Recursively generate an ASCII representation of a directory tree.
    """
    if exclude is None:
        exclude = set()

    tree_lines = []
    try:
        items = sorted(os.listdir(start_path))
    except PermissionError:
        return [f"{prefix}└── [Permission Denied]"]

    entries = [
        item for item in items if item not in exclude and not item.startswith(".")
    ]

    for index, item in enumerate(entries):
        path = os.path.join(start_path, item)
        connector = "├── " if index < len(entries) - 1 else "└── "
        tree_lines.append(f"{prefix}{connector}{item}")

        if os.path.isdir(path):
            extension = "│   " if index < len(entries) - 1 else "    "
            tree_lines += generate_tree(path, prefix + extension, exclude)

    return tree_lines


def save_tree_to_file(
    root_path: str, output_file: str = "directory_structure.txt", exclude: Optional[set] = None
):
    """
    Save the ASCII directory tree to a file.
    """
    if not os.path.exists(root_path):
        raise FileNotFoundError(f"The path '{root_path}' does not exist.")

    tree_lines = [os.path.abspath(root_path)]
    tree_lines += generate_tree(root_path, exclude=exclude)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(tree_lines))
