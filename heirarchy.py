import re
import argparse
import os

def modify(filename):
    os.system("cp " + filename + " " + filename + ".bak")    
    flag = False

    with open(filename, "r") as infile:
        text = infile.readlines()

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
    with open(filename, "r") as infile:
        text = infile.readlines()
        # os.system("rm " + filename)
        for i in range(len(text)-1, -1, -1):
            modline = ""
            if loc[i]:
                modline = "[] " + text[::-1][i]
            else:
                modline = text[::-1][i]
            finaltext += modline
    with open(filename, "w") as outfile:
        outfile.write(finaltext)

if __name__ == "__main__":
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required=True,
        help="path/name of the file")
    args = vars(ap.parse_args())
    
    modify(args["file"])