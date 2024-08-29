from dataclasses import dataclass
from typing import Dict, Union


with open("data/day7.txt") as f:
    data = f.read()
    data = data.strip()


@dataclass
class File:
    name: str
    size: int   

@dataclass
class Directory:
    path: str
    files: Dict[str, Union[File, 'Directory']]
    parent: Union[None, 'Directory'] = None
    size: int = -1

def compute_sizes(dir: Directory) -> int:
    dir_size = 0
    for file in dir.files.values():
        match file:
            case File(_, size):
                dir_size += size
            case Directory():
                dir_size += compute_sizes(file)
    dir.size = dir_size

    return dir_size

def load_fs(data: str) -> Directory:
    root = Directory("/", {})
    pwd = root
    
    lines = [x.strip() for x in data.split("$ ") if x.strip()]

    for line in lines:
        if line.startswith("cd"):
            path = line.split(" ")[1]
            if path == "/":
                pwd = root
            elif path == "..":
                pwd = pwd.parent
            else:
                pwd = pwd.files[path]
        elif line.startswith("ls"):
            parts = line.split("\n")[1:]
            for part in parts:
                file = part.split(" ")
                if file[0] == 'dir':
                    name = file[1]
                    if pwd.path == '/':
                        pwd.files[name] = Directory(pwd.path + name, {}, pwd)
                    else:
                        pwd.files[name] = Directory(pwd.path + '/' + name, {}, pwd)
                else:
                    size, name = file
                    pwd.files[name] = File(name, int(size))

    compute_sizes(root) 
    return root

# add directory sizes to root
def all_dirs_less(root: Directory, max_size: int) -> int:
    total = 0
    for file in root.files.values():
        match file:
            case File(_, _):
                continue
            case Directory(_, _, _, dir_size):
                if dir_size < max_size:
                    total += dir_size
                total += all_dirs_less(file, max_size)
    return total

fs = load_fs(data)
print(all_dirs_less(fs, 100_000))

TOTAL_DISK = 70_000_000
SPACE_NEEDED = 30_000_000

SPACE_AVAILABLE = TOTAL_DISK - fs.size
FREE = SPACE_NEEDED - SPACE_AVAILABLE

def all_dirs_larger(root: Directory, min_size: int) -> int:
    dirs = []
    for file in root.files.values():
        match file:
            case File(_, _):
                continue
            case Directory(path, _, _, dir_size):
                if dir_size > min_size:
                    dirs.append((path, dir_size))
                dirs.extend(all_dirs_larger(file, min_size))
    return dirs

print(sorted(all_dirs_larger(fs, FREE), key=lambda x: x[1]))