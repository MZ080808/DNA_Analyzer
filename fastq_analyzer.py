from os.path import isfile
import matplotlib.pyplot as plt
from numpy import isin


def convert_ascii(char):
    return ord(char) - 33


def fastq_analyze(file):
    sequences = []
    qualities = []
    with open(file, encoding='utf-8') as fh:
        while True:
            fh.readline()  # skip name line
            seq = fh.readline().rstrip()  # read base sequence
            fh.readline()  # skip placeholder line
            qual = fh.readline().rstrip()  # base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)

    return sequences, qualities


def fastq_in():
    # prompts the user to input a fastq file
    while True:
        fastq = input(
            "Please insert a fastq file for analyzing or type q to quit:")
        if fastq.lower() == 'q':
            print("Session Terminated on user's request")
            return None
        if not isfile(fastq):
            print("--<ERROR>-- \n File doesn't exist \n >===========<")
            continue
        break

    seq, qua = fastq_analyze(fastq)

    Q = []
    for read in qua:
        qual = []
        for char in read:
            qual.append(str(convert_ascii(char)))
        Q.append(','.join(qual))

    hist_y = [0] * 100
    for i in range(len(Q)):
        r = Q[i].split(",")
        for j in range(100):
            hist_y[j] += int(r[j])

    bar_plt = plt.bar(range(len(hist_y)), hist_y, width=0.5)
    line_grph = plt.plot(range(len(hist_y)), hist_y)
    plt.show()


fastq_in()
