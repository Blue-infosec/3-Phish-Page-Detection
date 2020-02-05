#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


class Candidate(object):
    """
    Candidates are for the image and html source files
    """
    def __init__(self, idx, img_path, source_html):
        self.idx = idx
        self.img_path = img_path
        self.source_html = source_html

    def get_idx(self):
        return self.idx

    def get_img(self):
        return self.img_path

    def get_source(self):
        return self.source_html

    def print_info(self):
        print ("IDX is {}, Img is {} and souce is {}".format(self.idx, self.img_path, self.source_html))


# Support functions
def read_crawl_candidates(dire):
    files = os.listdir(dire)
    if not dire.endswith('/'):
        dire = dire + '/'

    idxs = list()
    candidates = list()

    def get_idx(f):
        return f.split("..")[0]

    for f in files:
        if f.startswith('.'):
            continue
        idx = get_idx(f)

        if idx not in idxs:
            img_txt = dire + idx + '..screen.png'
            source_html = dire + idx + '..source.txt'
            can = Candidate(idx, img_txt, source_html)
            candidates.append(can)
            idxs.append(idx)

    return candidates


PhishTank_BrandMap = {}
