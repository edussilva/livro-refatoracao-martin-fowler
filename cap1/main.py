import json
from statement import statement, html_statement

if __name__ == '__main__':
    with open('cap1/plays.json', 'r') as plays_file:
        plays_dict = plays_file.read()
        plays = json.loads(plays_dict)
    
    with open('cap1/invoices.json', 'r') as invoices_file:
        invoices_dict = invoices_file.read()
        invoices = json.loads(invoices_dict)
    
    for invoice in invoices:
        txt = statement(invoice, plays)
        print(txt)

    for invoice in invoices:
        html = html_statement(invoice, plays)
        print(html)
