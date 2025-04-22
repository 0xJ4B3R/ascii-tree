# ASCII Tree

ASCII Tree is a simple and efficient command-line utility to generate a visual representation of a directory structure in plain-text ASCII format. Useful for documentation, visualization, or archiving project layouts.

## Features

- Recursive traversal of any directory path.
- Output formatted as an easy-to-read ASCII tree.
- Option to exclude specific files or folders.
- Works on all major platforms (Linux, macOS, Windows).
- No external dependencies.

## Installation

Clone this repository:

```bash
git clone https://github.com/0xJ4B3R/ascii-tree.git
cd ascii-tree
```

## Usage

Run the script directly with Python:

```bash
python main.py "C:\Path\To\Directory" -o output.txt -e <name1> <name2> <name3>
```

### Arguments

- `path` (required): The root directory to analyze.
- `-o, --output` (optional): Name of the output file. Default is `directory_structure.txt`.
- `-e, --exclude` (optional): List of file or directory names to exclude from the tree.

### Example

```bash
python main.py "/Users/jr/Projects/my-app" -e node_modules .git build
```

This command will generate a tree of the project, ignoring the `node_modules`, `.git`, and `build` directories.

## Output Sample

```
/Users/jr/Projects/my-app
├── public
│   └── index.html
├── src
│   ├── App.js
│   └── components
└── package.json
```

## License

MIT License
