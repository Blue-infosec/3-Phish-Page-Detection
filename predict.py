#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import numpy as np
from sklearn import decomposition
from sklearn.externals import joblib

# concurrent preidction
# from concurrent.futures import TimeoutError


try:
    import cPickle as pickle
except:
    print ("No cpickle?")
    import pickle


def parse_options():
    parser = argparse.ArgumentParser(description="running analysis...", prefix_chars='-+/')
    parser.add_argument('-t', '--html', type=str,
                        help='A html source data to extract features')
    parser.add_argument('-i', '--img', type=str,
                        help='A image data to extract features')
    args = parser.parse_args()
    return args


def run_single_candidate(arg):
    idx, v, pca, forest = arg['c_idx'], arg['v'], arg['pca'], arg['clf']
    new_v = pca.transform(np.asarray(v).reshape(1, -1))
    p_prob = forest.predict_proba(new_v)
    p = forest.predict(new_v)
    print (str(idx) + "----" + str(p.tolist()[0]) + "----" + str(p_prob.tolist()[0]))
    return str(idx) + "----" + str(p.tolist()[0]) + "----" + str(p_prob.tolist()[0])

# Multiple process version

"""
def muliple_process_run(args_list, n_core, output_file, redirection_folder):
    results = []

    with ProcessPool(max_workers=n_core) as pool:

        future = pool.map(run_single_candidate, args_list, timeout=20)

        iterator = future.result()

        # iterate over all results, if a computation timed out
        # print it and continue to the next result
        while True:
            try:
                result = next(iterator)
                results.append(result)
            except StopIteration:
                break
            except TimeoutError as error:
                print "function took longer than %d seconds" % error.args[1]

    file = open(output_file, "w+")
    print ("the type of the results is ", type(results))
    for re in results:
        idx = re.split("----")[0]
        redirec_file = redirection_folder + idx + "..redirect"
        pre = re.split("----")[1]
        if pre == "1.0":
            #print (redirec_file)
            if not redirect_identify.is_redirected_to_original(redirec_file):
                file.write(re)
                file.write("\n")
            else:
                print ("false positive", idx)
    file.flush()
    file.close()
    print ("[Done]we finish recording the results at " + output_file)
"""


def test_predict():
    X = np.loadtxt("./data/X.txt")
    print (X.shape)

    # X = np.delete(X, np.s_[988:], axis=1)  # remove columns 1 and 2
    # print (X.shape)
    pca = decomposition.PCA(n_components=100)
    pca.fit(X)

    forest = joblib.load('./saved_models/forest_pca.pkl')
    f = open("pre/243_web.p", 'r')  # 'r' for reading; can be omitted
    mydict = pickle.load(f)

    for i in mydict:
        v = mydict[i]
        new_v = pca.transform(np.asarray(v).reshape(1, -1))
        print (i, forest.predict(new_v), forest.predict_proba(new_v))



if __name__ == "__main__":

    pass
    sys.exit(0)
