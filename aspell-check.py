import aspell 
import argparse
import operator

parser = argparse.ArgumentParser(description='Arabic spell checker based on aspell. The input is a file and the output is errors with frequencies.')  # type: ArgumentParser

parser.add_argument('-i', '--infile', type=argparse.FileType(mode='r', encoding='utf-8'), help='input file.', required=True)
parser.add_argument('-o', '--outfile', type=argparse.FileType(mode='w', encoding='utf-8'), help='output file.', required=True)

if __name__ == '__main__':
    ar_spell = aspell.Speller('lang', 'ar')
    args = parser.parse_args()
    words = args.infile.read().split()
    outfile = args.outfile
    errors_count = dict()
    for word in words:
        if not ar_spell.check(word):
            if word not in errors_count:
                errors_count[word] = 1
            else:
                errors_count[word] += 1
    sorted_freq = sorted(errors_count.items(), key=operator.itemgetter(1), reverse=True)
    outfile.write('# word\tfreq\tsuggestion\n')
    for word, freq in sorted_freq:
        try: 
            outfile.write('{}\t{}\t{}\n'.format(word, freq, ar_spell.suggest(word)[0]))
        except IndexError:
            outfile.write('{}\t{}\n'.format(word, freq))
        
        

