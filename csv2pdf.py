import pandas as pd
import glob
import pdfkit

input_file = 'pdfTest.csv'
pathname = '/Users/kevinbratt/dataloader/PDFTest/'
input_pathname = '/Users/kevinbratt/dataloader/'


def main(input_file, pathname):
    columns = ['Case Number', 'Created Time', 'Item Num', 'Item Category',
               'Item Description', 'Quantity', 'Cost', 'Price']
    df = pd.read_csv(input_pathname + input_file, names=columns)

    unique_case_number = df['Case Number'].unique()
    for case in unique_case_number[1:]:
        case_table = df[df['Case Number'] == case]

        filename = pathname + case + '.html'
        with open(filename, 'w'):
            case_table.to_html(filename, index=False)

        for filepath in glob.iglob(pathname + '*.html'):
            stripped_filename = filepath[:-5]
            pdfkit.from_file(filepath, stripped_filename + '.pdf')


if __name__ == "__main__":
    main(input_file, pathname)
