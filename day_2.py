#!/usr/bin/python3

from __helpers__ import get_file_content

def get_checksum_of_box_ids(box_ids):
    parts = []

    for box_id in box_ids:
        unique = set(box_id)

        part = set()
        for char in unique:
            count = box_id.count(char)
            if count == 2 or count == 3:
                part.add(count)

        if part:
            parts.extend(set(part))

    checksum = 1
    unique_parts = set(parts)
    for unique_part in unique_parts:
        checksum *= parts.count(unique_part)

    return checksum

def get_common_part_of_almost_equal_strings(a, b):
    assert len(a) == len(b)

    diff_idx = 0
    diffs = 0
    for idx, char in enumerate(a):
        if char != b[idx]:
            diffs += 1
            diff_idx = idx
        if diffs >= 2:
            return None
    return a[:diff_idx] + a[diff_idx + 1:]

def find_common_part_in_ids(box_ids):
    while True:
        cur_id = box_ids.pop(0)
        for box_id in box_ids:
            common_part = get_common_part_of_almost_equal_strings(cur_id, box_id)
            if common_part:
                return common_part
        if not len(box_ids):
            return None

if __name__ == "__main__":
    box_ids = [box_id.strip() for box_id in get_file_content("inputs/day_2.txt")]

    checksum = get_checksum_of_box_ids(box_ids)
    print("Checksum of box IDs: {}".format(checksum))

    common_part = find_common_part_in_ids(box_ids)
    print("Unique part of almost equal ids: {}".format(common_part))
