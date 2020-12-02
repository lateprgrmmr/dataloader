# names.py>
import sys
import os
# import csv
# import re
# from removals import remove
# import petl as etl
from nameparser import HumanName as hn
import pandas as pd


# -- print("dumb fuck")
# -- etl.transform.regex.capture() <-- WILL be useful, learn REGEX!!!
# -- https://petl.readthedocs.io/en/stable/transform.html

# -- Prints a note about acceptable file types/format and prompts user for input file
# -- print('NOTE: Accepts .xlsx files with a single column (Name) of names to be fixed
# -- \n and split into separate parts.')
file = input('Enter filename to process: ')

cols = input('Enter the name of the column(s) that contain' +
             '\n' + 'names you would like to parse: ')


def SplitNames(file, cols):

    # -- Define variables for the output file we'll create at the end
    fn = 'FixedNames'
    ext = '.csv'
    n = ''

    # -- Read in the file entered at prompt
    df = pd.read_excel(file)
    avail_head = list(df.columns)
    #split_col = list(avail_head)
    try:
        if cols in avail_head:
            print('All columns entered are valid. Please Wait...')

        names = []

        for row in df[cols]:
            # -- Removes current known portions of unformatted names -- Need to
            # -- figure out how to pass this as a list
            # -- ['Rev.','Sr.','Sr',' sr','Jr.','Jr','jr','III','II','-DEL']
            a = row.replace('Rev.', '').replace(
                'Sr.,', '').replace('Sr.', '').replace('Sr', '').replace(' sr', '') \
                    .replace('Jr.', '').replace('Jr', '').replace('jr', '') \
                        .replace('III', '').replace('II', '').replace('-DEL', '')
        # .replace(' , ','')
            a2 = a.replace('(', '').replace(')', '')
        # -- Apply the HumanName parser
            b = hn(a2)
        # -- Pull out and name the appropriate columns
            w = [b.first, b.middle, b.last, b.nickname]
            names.append(w)
            fixed = pd.DataFrame(names, columns=['deathcertificate.about.firstName',
                                                 'deathcertificate.about.middleName',
                                                 'deathcertificate.about.lastName',
                                                 'deathcertificate.about.aka'])

        # -- Check if pre-formatted output file exists, if it does, this will
        # -- make a sequential filename like "filename#" where # is the sequence
            while os.path.exists('%s%s%s' % (fn, n, ext)):
                if isinstance(n, str):
                    n = -1
                n += 1
            xx = '%s%s%s' % (fn, n, ext)
    except KeyError:
        print('Invalid column name, check file and try again.')
        sys.exit()

    # -- Write output of function to newly created filename

    return fixed.to_csv(xx)


if __name__ == '__main__':
    SplitNames(file, cols)
