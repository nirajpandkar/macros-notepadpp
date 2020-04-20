import re
import argparse
import os
import sys

def modify(text):  
    flag = False

    loc = dict()
    inv_text = text[::-1]
    for i, line in enumerate(text[::-1]):
        if re.findall(r"\[\]", line):
            n_hashes = 10
            for j in range(i, len(text)):
                if j not in loc.keys():
                    loc[j] = 0
                if re.findall(r"#", inv_text[j]) and len(re.findall(r"#", inv_text[j])) < n_hashes:
                    n_hashes = len(re.findall(r"#", inv_text[j]))
                    loc[j] += 1
                    print(inv_text[j])


    finaltext = ""
    for i in range(len(text)-1, -1, -1):
        modline = ""
        if loc[i]:
            modline = "[] " + text[::-1][i]
        else:
            modline = text[::-1][i]
        finaltext += modline + "\n"
    sys.stdout.write(finaltext)

if __name__ == "__main__":
    text = sys.stdin.read()
    modify(text.split("\n"))