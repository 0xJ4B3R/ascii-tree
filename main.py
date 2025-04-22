import argparse
import os
import logging
from src.exporter import save_tree_to_file

logging.basicConfig(level=logging.INFO, format="%(message)s")


def main():
    parser = argparse.ArgumentParser(
        description="Generate an ASCII tree representation of a directory structure."
    )
    parser.add_argument(
        "path", help="Root directory to generate tree from (wrap in quotes if it contains spaces)"
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output file name (default: directory_structure.txt)",
        default="directory_structure.txt",
    )
    parser.add_argument(
        "-e",
        "--exclude",
        nargs="*",
        default=[],
        help="List of folder/file names to exclude",
    )

    args = parser.parse_args()

    try:
        save_tree_to_file(
            os.path.abspath(args.path), args.output, exclude=set(args.exclude)
        )
        logging.info(f"Directory structure saved to '{args.output}'.")
    except Exception as e:
        logging.error(f"Error: {e}")


if __name__ == "__main__":
    main()
