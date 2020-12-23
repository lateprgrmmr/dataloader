
import os
import sys

import click
import pandas as pd
from nameparser import HumanName as hn


@click.command()
@click.argument('file', type=click.File('r'))
def s_names(file):
    """Takes a csv document with a single column of names
    and parses it into First, Middle and Last names while
    omitting any titles, suffixes, etc.
    
    FILE is the name of the XLSX document to process. Enter it
    after the program name (i.e. names.py abc.csv)
    """
    file_name = 'FixedNames'
    ext = '.csv'
    n = ''

    df = pd.read_csv(file)
    head = list(df.columns)

    try:
        # if cols in avail_head:
        #     print('All columns entered are valid. Please Wait...')

        names = []

        for row in df[head[0]]:
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

            while os.path.exists('%s%s%s' % (file_name, n, ext)):
                if isinstance(n, str):
                    n = -1
                n += 1
            xx = '%s%s%s' % (file_name, n, ext)
    except KeyError:
        print('Invalid column name, check file and try again.')
        sys.exit()

    # -- Write output of function to newly created filename

    return fixed.to_csv(xx)


if __name__ == '__main__':
    s_names()
