#!/usr/bin/python3

from operator import itemgetter

from __helpers__ import get_file_content

def parse_fabric_cfgs(raw_fabric_cfgs):
    fabric_cfg = []
    for cfg in raw_fabric_cfgs:
        temp = cfg.split(" ")
        for idx in range(len(temp)):
            temp[idx] = temp[idx].replace(":", "")
            temp[idx] = temp[idx].replace(",", " ")
            temp[idx] = temp[idx].replace("x", " ")
            temp[idx] = temp[idx].split(" ")
        fabric_cfg.append(dict(zip(("coords", "size"), [temp[2], temp[3]])))
    return fabric_cfg

def build_matrix(fabric_cfgs):
    coords = list((cfg["coords"] for cfg in fabric_cfgs))
    max_x = int(max(coords, key=lambda x: x[0])[0])
    max_y = int(max(coords, key=lambda y: y[1])[0])

    from IPython import embed; embed()

if __name__ == "__main__":
    raw_fabric_cfg = [line.strip() for line in get_file_content("inputs/day_3.txt")]

    fabric_cfgs = parse_fabric_cfgs(raw_fabric_cfg)

    matrix = build_matrix(fabric_cfgs)

