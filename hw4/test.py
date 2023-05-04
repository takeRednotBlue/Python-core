from pathlib import Path

# path = Path.cwd() / "hw4" / "shopping_list.md"

"""Two ways to open file and print only some specific lines"""

# with path.open(mode="r", encoding="utf-8") as md_file:
#     content = md_file.read()
#     groceries = [line for line in content.splitlines() if line.startswith("*")]

# content = path.read_text(encoding="utf-8")
# groceries = [line for line in content.splitlines() if line.startswith("*")]

# print("\n".join(groceries))

"""You can specify paths directly as filenames, in which case they’re 
interpreted relative to the current working directory."""

# content = Path("hw4\shopping_list.md").read_text(encoding="utf-8")
# groceries = [line for line in content.splitlines() if line.startswith("*")]

# Path("hw4\plain_list.md").write_text("\n".join(groceries), encoding="utf-8")

# print("\n".join(groceries))

"""
Path doesn’t have a method to copy files. But we can create the same functionality with a few lines of code.
We may also consider using 'shutil' library for copying files.
"""

# source = Path("shopping_list.md")
# destination = source.with_stem("shopping_list_02")
# destination.write_bytes(source.read_bytes())

"""The way to move file excluding possibility for race condition"""

# source = Path("hello.py")
# destination = Path("goodbye.py") 

# try:
#     with source.open(mode="xb") as file:
#         destination.write_bytes(source.read_bytes)
# except FileExistsError:
#     print(f"File {destination} exists already.")
# else:
#     source.unlink()
 

"""Creating empty files.
touch() method  is intended to update a file’s modification time but 
in this example we use it's side effect.
"""

# filename = Path("hello.txt")
# # rase an FileExistsError if file already exists
# filename.touch(exist_ok=False) 

"""
To properly discard paths that are in a junk directory, you can check if any of the elements in the 
path match with any of the elements in a list of directories to skip. You can get all the elements 
in the path with the .parts attribute, which contains a tuple of all the elements in the path. 
You can check if any two iterables have an item in common by taking advantage of sets. If you cast one of the 
iterables to a set, then you can use the .isdisjoint() method to determine whether they have any elements in common.
"""

# SKIP_DIRS = ["temp", "temporary_files", "logs"]
# large_dir = Path("large_dir")

# for item in large_dir.rglob("*"):
#     if set(item.parts).isdisjoint(SKIP_DIRS):
#         print(item)

# # Comprehension
# item_list = [
#     item
#     for item in large_dir.rglob("*")
#     if set(item.parts).isdisjoint(SKIP_DIRS)
# ]

# # With filter()
# item_list = list(
#     filter(
#     lambda item: set(item.parts).isdisjoint(SKIP_DIRS),
#     large_dir.rglob("*")
#     )
# )

"""
Recursive .iterdir() Function
"""

SKIP_DIRS = ["temp", "temporary_files", "logs"]

def get_all_items(root: Path, exclude=SKIP_DIRS):
    for item in root.iterdir():
        if item.name in exclude:
            continue
        yield item
        if item.is_dir():
            yield from get_all_items(item)
        # else:
        #     yield item

path = Path.cwd()

# for item in get_all_items(path):
#     print(item)


"""
Display a Directory Tree
"""

def tree(directory: Path):
    print(f"+ {directory}")
    for path in get_all_items(directory):
        depth = len(path.relative_to(directory).parts)
        spacer =  "    " * depth
        print(f"{spacer} + {path.name}")

# tree(path)

"""
Finding the Most Recently Modified File
"""

from datetime import datetime

directory = Path.cwd()
time, file_path = max((f.stat().st_mtime, f) for f in directory.iterdir())
print(datetime.fromtimestamp(time), file_path)