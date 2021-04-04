# import pandas as pd

# begin the table
print("<table>")

# column headers
print("<th>")
print("<td>Case Number</td>")
print("<td>Created Time</td>")
print("<td>Item Num</td>")
print("<td>Item Category</td>")
print("<td>Item Description</td>")
print("<td>Quantity</td>")
print("<td>Cost</td>")
print("<td>Price</td>")
print("</th>")

infile = open("pdfTest.csv", "r")

for line in infile:
    row = line.split(",")
    case_number = row[0]
    created_time = row[1]
    item_num = row[2]
    item_cat = row[3]
    item_desc = row[4]
    quantity = row[5]
    cost = row[5]
    price = row[5]

    if case_number == '2009-0096':
        print("<tr>")
        print("<td>%s</td>" % created_time)
        print("<td>%s</td>" % item_num)
        print("<td>%s</td>" % item_cat)
        print("<td>%s</td>" % item_desc)
        print("<td>%s</td>" % quantity)
        print("<td>%s</td>" % cost)
        print("<td>%s</td>" % price)
        print("</tr>")

# end the table
print("</table>")

# columns = ['case_number', 'created_time', 'item_num',
#            'item_cat', 'item_desc', 'quantity', 'cost', 'price']
# df = pd.read_csv('pdfTest.csv', names=columns)

# # This you can change it to whatever you want to get
# age_15 = df[df['age'] == 'U15']
# # Other examples:
# bye = df[df['opp'] == 'Bye']
# crushed_team = df[df['ACscr'] == '0']
# crushed_visitor = df[df['OPPscr'] == '0']
# # Play with this

# # Use the .to_html() to get your table in html
# print(crushed_visitor.to_html())
