from collections import defaultdict
from typing import List, Tuple, Dict

from common import read_input

raw_test_data = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
]

original_mapping = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdfeg",
    7: "acf",
    8: "abcdfeg",
    9: "abcdfg",
}


def sort_chars(chars: str) -> str:
    return "".join(sorted(chars))


def parse_raw_line(raw: str) -> Tuple[List[str], List[str]]:
    entries, entries_to_decode = raw.split(" | ")
    entries = entries.split(" ")
    entries = [sort_chars(entry) for entry in entries]
    entries_to_decode = entries_to_decode.split(" ")
    entries_to_decode = [sort_chars(entry) for entry in entries_to_decode]
    return entries, entries_to_decode


def parse_raw_lines(lines: List[str]) -> Tuple[List[List[str]], List[List[str]]]:
    line_entries = []
    line_entries_to_decode = []
    for line in lines:
        entries, entries_to_decode = parse_raw_line(line)
        line_entries.append(entries)
        line_entries_to_decode.append(entries_to_decode)
    return line_entries, line_entries_to_decode


class Decoder:

    def __init__(self, original_mapping: Dict[int, str]):
        self.original_mapping = original_mapping
        self.new_mapping = {}

        self.lengths_digit_map = defaultdict(list)
        for digit, chars in original_mapping.items():
            self.lengths_digit_map[len(chars)].append(digit)

        self.length_to_unique_digit_map = {
            k: v[0] for k, v in self.lengths_digit_map.items() if len(v) == 1
        }

    def fit(self, entries: List[str]):
        sorted_entries = [self._sort_chars(entry) for entry in entries]
        self.new_mapping.update(
            {
                sort_chars(chars): self.length_to_unique_digit_map[len(chars)]
                for chars in sorted_entries
                if len(chars) in self.length_to_unique_digit_map
            }
        )

    def transform(self, entries: List[str]) -> List[int]:
        sorted_entries = [self._sort_chars(entry) for entry in entries]
        decoded_digits = []
        for chars in sorted_entries:
            if chars in self.new_mapping:
                decoded_digits.append(self.new_mapping[chars])
            else:
                decoded_digits.append(None)
        return decoded_digits

    @staticmethod
    def _sort_chars(chars: str) -> str:
        return "".join(sorted(chars))


# Part 1 test
test_line_entries, test_line_entries_to_decode = parse_raw_lines(raw_test_data)
count = 0
for entries, entries_to_decode in zip(test_line_entries, test_line_entries_to_decode):
    decoder = Decoder(original_mapping=original_mapping)
    decoder.fit(entries)
    decoded = decoder.transform(entries_to_decode)
    count += sum([0 if el is None else 1 for el in decoded])
assert count == 26


if __name__ == "__main__":
    # Part 2
    raw_data = read_input("data/day8.txt")
    line_entries, line_entries_to_decode = parse_raw_lines(raw_data)
    count = 0
    for entries, entries_to_decode in zip(line_entries, line_entries_to_decode):
        decoder = Decoder(original_mapping=original_mapping)
        decoder.fit(entries)
        decoded = decoder.transform(entries_to_decode)
        count += sum([0 if el is None else 1 for el in decoded])
    print(f"Part 1: {count}")

    # Part 2
    # print(f"Part 1: {}")