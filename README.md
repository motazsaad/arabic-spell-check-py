# arabic-spell-check-py
Spell check for Arabic text using python 

## Installation 
For hunspell, you need to install the following packages 
```
sudo apt install hunspell-ar
sudo apt install libhunspell-dev
```
## Usage 
```hunspell-check.py [-h] -i INFILE -o OUTFILE```

Arabic spell checker based on hunspell. The input is a file and the output is errors with
frequencies.

## Arguments:
  -h, --help            show this help message and exit
  
  -i INFILE, --infile INFILE (input file).
                        
  -o OUTFILE, --outfile OUTFILE (output file).



## references 
1. https://github.com/blatinier/pyhunspell docs: https://hunspell.github.io/ and https://en.wikipedia.org/wiki/Hunspell
2. https://github.com/barrust/pyspellchecker and https://github.com/hermitdave/FrequencyWords docs: https://pyspellchecker.readthedocs.io/en/latest/quickstart.html
3. https://github.com/linuxscout/yaraspell
4. https://github.com/WojciechMula/aspell-python
