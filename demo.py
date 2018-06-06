#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util
import os

DEFAULT_DIR = "./test/"

def read_candidates():
    files =  os.listdir(DEFAULT_DIR)

    candidate_idxs = list()
    Candidates = list()

    for f in files:
        if not f.endswith("png") and not f.endswith("txt"):
            continue
        idx = f.split("..")[0]
        candidate_idxs.append(idx)
        img = DEFAULT_DIR + idx + "..screen.png"
        source = DEFAULT_DIR + idx + "..source.txt"
        c = util.Candidate(idx=idx, img_path=img, source_html=source)
        Candidates.append(c)

    return Candidates


def read_model():
    pass


def prediction():
    pass


if __name__ == "__main__":
    cs = read_candidates()
    for c in cs:
        c.print_info()
