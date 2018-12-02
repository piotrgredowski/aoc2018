#!/usr/bin/python3

def get_file_content(path):
    with open(path, "r+t") as f:
        for line in f:
            yield line

def calculate_change_of_fq(base_fq, changes_of_fq):
    for change_of_fq in changes_of_fq:
        base_fq += change_of_fq
    return base_fq

def get_first_fq_reached_twice(changes_of_fq):
    fq = 0
    seen = set()
    while True:
        for change_of_fq in changes_of_fq:
            seen.add(fq)
            fq += change_of_fq
            if fq in seen:
                return fq
    return None


if __name__ == "__main__":
    base_fq = 0
    changes_of_fq = [int(change) for change in get_file_content("input.txt")]

    final_fq = calculate_change_of_fq(base_fq, changes_of_fq)
    print("Final frequency: {}".format(final_fq))

    first_fq_reached_twice = get_first_fq_reached_twice(changes_of_fq)
    print("First frequency reached twice: {}".format(first_fq_reached_twice))
