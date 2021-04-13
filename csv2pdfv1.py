import pandas as pd
import glob
import pdfkit

input_file = 'pdfTest.csv'
pathname = '/Users/kevinbratt/dataloader/PDFTest/'
input_pathname = '/Users/kevinbratt/dataloader/'


def main(input_file, pathname):
    columns = ['Case Number', 'Decedent Name', 'Created Time', 'Item Num',
               'Item Category', 'Item Description', 'Quantity', 'Cost',
               'Price']
    df = pd.read_csv(input_pathname + input_file, names=columns)

    unique_case_number = df['Case Number'].unique()
    for case in unique_case_number[1:]:
        case_table = df[df['Case Number'] == case]
        add_total = case_table.append(
            case_table[['Quantity', 'Cost', 'Price']].astype(
                float).sum(),
            ignore_index=True).fillna('')
        report_table = add_total[['Created Time', 'Item Num',
                                  'Item Category', 'Item Description',
                                  'Quantity', 'Cost',
                                  'Price']]
        decedent = case_table.iloc[0]['Decedent Name']

        report = '''
        <!DOCTYPE html>
        <html>
            <head>
                <style>
                    main {
                        font-family: "Arial";
                    }
                    thead tr {
                        text-align: center !important;
                    }
                    table {
                        font-family: "Arial";
                    }
                    th, td {
                        border-bottom: 1px solid #ddd !important;
                    }
                    tr:hover {
                        background-color: #f5f5f5;
                    }

                </style>
            </head>
            <main>
                <div>
                    %s: %s
                </div><br>
                <body>
                    %s
                </body>
            </main>
        </html>
        ''' % (case, decedent, report_table.to_html(index=False,
                                                    border=0))
    # print(report)
    # print(decedent)
    filename = pathname + case + '.html'
    with open(filename, 'w') as fo:
        fo.write(report)

    for filepath in glob.iglob(pathname + '*.html'):
        stripped_filename = filepath[:-5]
        pdfkit.from_file(filepath, stripped_filename + '.pdf')


if __name__ == "__main__":
    main(input_file, pathname)
