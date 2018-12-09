from scipy.io.wavfile import read
import numpy as np
import csv
import peakutils
import os
import logging

from clargs import parser
args = parser.parse_args()

if args.verbose:
    logging.basicConfig(level=logging.INFO)
else:
    logging.basicConfig(level=logging.ERROR)

files = []
if args.input:
    [files.append(i) for i in args.input]
else:
    all_files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in all_files:
        root, ext = os.path.splitext(f)
        if ext == '.wav':
            files.append(f)

big_data = []
for f in files:
    audio_file = f

    min_time = .1  # minimum time (s) between taps

    thres = 0.6  # threshold 0-1

    rate, data = read(audio_file)

    y = data[..., 1]
    x = np.arange(y.size)
    indexes = peakutils.indexes(y, thres=thres, min_dist=rate*min_time)
    diff = np.diff(indexes/rate)

# some basic info about each file
    logging.info(f'For file: {f}')
    logging.info(f'Time at each tap (s): {indexes/rate}')
    logging.info(f'Time between taps (s): {diff}')
    logging.info(
        f'Average +- std. dev.(s): {np.mean(diff):.2} +- {np.std(diff):.2}')

    data = [f]
    [data.append(d) for d in diff]
    big_data.append(data)

if args.append:
    type = 'a'
else:
    type = 'w'
with open(args.out, type) as csv_file:
    writer = csv.writer(csv_file)
    if type is not 'a':
        writer.writerow(['filename', 'Time between taps in seconds'])
    for d in big_data:
        writer.writerow(d)
