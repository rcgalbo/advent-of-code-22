from dataclasses import dataclass
from typing import Union, Iterator

@dataclass
class File:
    name: str
    size: int

@dataclass
class Directory:
    path: list[str]
    files: dict[str, Union[File, 'Directory']]
    parent: Union[None, 'Directory'] = None
    size: int = -1

def learn_filesystem(raw: str) -> Directory:
    root = Directory([], {})
    pwd: Directory = root
    commands = [x.strip() for x in raw.split("$ ") if x.strip()]
    
    for command in commands:
        lines = command.split("\n")
        match lines:
            case ['ls', *rest]:
                for listing in rest:
                    match listing.split():
                        case ['dir', dirname]:
                            if "dirname" not in pwd.files:
                                pwd.files[dirname] = Directory(pwd.path + [dirname], {}, pwd)
                        case [size, filename]:
                            pwd.files[filename] = File(filename, int(size))
            case [cd]:
                match cd.split():
                    case ["cd", "/"]:
                        pwd = root
                    case ["cd", '..']:
                        pwd = pwd.parent if pwd.parent else pwd
                    case ['cd', dirname]:
                        if dirname in pwd.files:
                            newdir = pwd.files[dirname]
                            assert isinstance(newdir, Directory)
                            pwd = newdir
                        else:
                            pwd.files[dirname] = Directory(pwd.path + [dirname], {}, pwd)
    compute_sizes(root)
    return root

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


def all_directories_below(root: Directory, size: int = 100000) -> Iterator[Directory]:
    if root.size <= size:
        yield root
    for file in root.files.values():
        match file:
            case Directory():
                yield from all_directories_below(file, size)
            case _:
                pass

if __name__ == "__main__":
        
    dat = """$ cd /
    $ ls
    dir a
    14848514 b.txt
    8504156 c.dat
    dir d
    $ cd a
    $ ls
    dir e
    29116 f
    2557 g
    62596 h.lst
    $ cd e
    $ ls
    584 i
    $ cd ..
    $ cd ..
    $ cd d
    $ ls
    4060174 j
    8033020 d.log
    5626152 d.ext
    7214296 k"""

    fs = learn_filesystem(dat)

    assert sum(dir.size for dir in all_directories_below(fs)) == 95437

    # part 1
    with open('data/day7.txt') as f:
        fs = learn_filesystem(f.read())
    print(sum(dir.size for dir in all_directories_below(fs)))

    Total_Disk_Size = 70_000_000
    Need_Unused_Size = 30_000_000
    Max_Size = Total_Disk_Size - Need_Unused_Size

    Used_Size = fs.size
    Need_To_Free = Used_Size - Max_Size 
    assert Need_To_Free == 8_381_165