from collections import defaultdict, Counter
from dataclasses import dataclass
from typing import List, Set, Dict, Tuple
from operator import eq




def load(filename: str) -> Tuple[Set[str], Dict[str, List[str]]]:
    with open(filename, 'r') as f:
        lines = f.readlines()
    caves: Set[str] = set()
    links: Dict[str, List[str]] = defaultdict(list)
    for line in lines:
        [p1, p2] = line.strip().split("-")
        if p1 not in caves:
            caves.add(p1)
        if p2 not in caves:
            caves.add(p2)
        links[p1].append(p2)
        links[p2].append(p1)
    return caves, links


def solve_1(caves: Set[str], links: Dict[str, List[str]]) -> int:
    def find_paths(caves: Set[str], links: Dict[str, List[str]], current_cave: str, current_path: List[str]) -> List[List[str]]:
        if current_cave == "end":   
            return [current_path]
        paths: List[List[str]] = []
        for cave in links[current_cave]:
            if (cave.islower() and cave not in current_path) or cave.isupper():
                paths += find_paths(caves, links, cave, current_path + [cave])
        return paths

    paths: List[List[str]] = []
    for cave in links["start"]:
        paths += find_paths(caves, links, cave, ["start", cave])
    return len(paths)
    

def solve_2(caves: Set[str], links: Dict[str, List[str]]) -> int:
    def find_paths(caves: Set[str], links: Dict[str, List[str]], current_cave: str, current_path: List[str]) -> List[List[str]]:
        if current_cave == "end":   
            return [current_path]
        cur_paths: List[List[str]] = []
        for cave in list(filter(lambda s: s != "start", links[current_cave])):
            if cave.islower():
                counter = Counter(filter(lambda s: s.islower(), current_path))
                if counter.most_common()[0][1] < 2 or cave not in counter:
                    cur_paths += find_paths(caves, links, cave, current_path + [cave])
            elif cave.isupper():
                cur_paths += find_paths(caves, links, cave, current_path + [cave])
        return cur_paths
    paths: List[List[str]] = []
    for cave in links["start"]:
        res = find_paths(caves, links, cave, ["start", cave])
        print(res)
        paths += res
    for path in paths:
        print(path)
    return len(paths)
    

if __name__ == "__main__":
    caves, links = load("input.txt")
    print(solve_1(caves, links))
    print(solve_2(caves, links))