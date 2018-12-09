# Taps
A short script to detect the time between taps from an audio file.

Taps searches the input wavefile for peaks. The time differential is exported to a csv file.

# Installation

```bash
git clone https://github.com/FlamingLasrSwrd/taps.git
cd taps
pip install -r requirements.txt
```

# Use
From the `taps.py` directory:

```bash
python taps.py
```
The basic use of `taps.py` will scan the calling directory for any file with the `.wav` extension and attempt to find the peaks. A `.csv` file will be made with the time differential of the detected taps.

```bash
python taps.py -o new_filename.csv
```
Outputs to `new_filename.csv` instead of the default file: `output.csv`.

```bash
python taps.py -i file1.wav file2.wav
```
Only processes `file1.wav` and `file2.wav`.

```bash
python taps.py -i 'file3.wave' -a
```
Append the results of `file3.wav` processing to the `output.csv` file instead of overwriting. Useful for processing files individually without losing all your work.

```bash
python taps.py -v
```
Prints some information about the analysis of each file to the screen.
