from typing import List


def read_input(fpath: str) -> List[str]:
    with open(fpath) as f:
        return [line.replace('\n', '') for line in f.readlines()]