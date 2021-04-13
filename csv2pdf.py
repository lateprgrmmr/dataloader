import pandas as pd
import glob
import pdfkit

contract_file = 'contract_total_test.csv'
merchandise_file = 'merchandise_test.csv'
services_file = 'services_test.csv'
pathname = '/Users/kevinbratt/dataloader/PDFTest/'
input_pathname = '/Users/kevinbratt/dataloader/'


def contract_report(merchandise_file, services_file, contract_file, pathname):
    merch = pd.read_csv(input_pathname + merchandise_file).fillna(0)
    contract_id = merch['ContractID'].unique()
    for contract in contract_id:
        filtered_merch = merch[merch['ContractID'] == contract]
        merchReportOut = filtered_merch[['ContractID', 'MerchandiseCategoryID',
                                         'Name', 'SerialNumber', 'Quantity', 'Price']].to_html(index=False, border=0)

<<<<<<< HEAD
    services = pd.read_csv(input_pathname + services_file).fillna(0)
    serv_contract_id = services['ContractID'].unique()
    for serv_contract in serv_contract_id:
        filtered_services = services[services['ContractID'] == contract]
        serviceReportOut = filtered_services[['ContractID', 'ServiceCategoryID',
                                              'Name', 'Description', 'Price',
                                              'IsTaxable', 'Quantity']].to_html(index=False, border=0)

    contract_totals = pd.read_csv(input_pathname + contract_file).fillna(0)
    contract_total_id = contract_totals['ContractID'].unique()
    for case in contract_total_id:
        case_table = contract_totals[contract_totals['ContractID'] == contract]
        # add_total = case_table.append(
        #     case_table[3:].astype(
        #         float).sum(),
        #     ignore_index=True).fillna('')
        report_table = case_table[['ContractID', 'FirstName', 'MiddleName', 'LastName',
                                   'Date of Death', 'Statement Date',
                                   'ContractTypeID', 'ContractTemplateName',
                                   'Total Services', 'Total Merchandise',
                                   'Total Cash Advances', 'Total Credits',
                                   'Total Pending Payments', 'Total Payments',
                                   'Total Tax', 'Contract Total', 'Balance Due']].to_html(index=False, border=0)
        case = case_table.iloc[0]['Case ID']
        decedentFirst = case_table.iloc[0]['FirstName']
        decedentLast = case_table.iloc[0]['LastName']
        decedent = decedentFirst + ' ' + decedentLast
=======
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
>>>>>>> 1da574d3f789f9d706ef90b9962276232ecd83ca

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
                </body><br>
                <body>
                    %s
                </body><br>
                <body>
                    %s
                </body>
            </main>
        </html>
<<<<<<< HEAD
        ''' % (case, decedent, merchReportOut, serviceReportOut, report_table)
=======
        ''' % (case, decedent, report_table.to_html(index=False,
                                                    border=0))
>>>>>>> 1da574d3f789f9d706ef90b9962276232ecd83ca
    # print(report)
    # print(case)
    # print(decedent)
<<<<<<< HEAD
    filename = pathname + 'contract_' + case + '.html'
=======
    filename = pathname + case + '.html'
>>>>>>> 1da574d3f789f9d706ef90b9962276232ecd83ca
    with open(filename, 'w') as fo:
        fo.write(report)

    for filepath in glob.iglob(pathname + '*.html'):
        stripped_filename = filepath[:-5]
        pdfkit.from_file(filepath, stripped_filename + '.pdf')


if __name__ == "__main__":
    contract_report(merchandise_file, services_file, contract_file, pathname)
