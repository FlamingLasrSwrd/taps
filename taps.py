from scipy.io.wavfile import read
import numpy as np
import csv
import peakutils

file_list = ['output.wav', 'output.wav']  # add input filenames here
output_file = 'outfile.csv' # output filename


big_data = []

for f in file_list:
	audio_file = f

	min_time = .1  # minimum time (s) between taps

	thres = 0.6  # threshold 0-1

	rate, data = read(audio_file)

#	plt.plot(data)

	y = data[...,1]
	x = np.arange(len(y))
	indexes = peakutils.indexes(y, thres=thres, min_dist=rate*min_time)

	print(f'For file: {f}')
	print(f'Time at each tap (s): {indexes/rate}')
	diff = np.diff(indexes/rate)
	print(f'Time between taps (s): {diff}')
	print(f'Average +- std. dev.(s): {np.mean(diff):.2} +- {np.std(diff):.2}')
	print()
	data = [f]
	[data.append(d) for d in diff]
	big_data.append(data)

with open(output_file, 'w') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow(['filename', 'Time between taps in seconds'])
	for d in big_data:
		writer.writerow(d)
