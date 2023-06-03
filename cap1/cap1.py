import math
import json
import os


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        this_amount = 0

        if play['type'] == 'tragedy':
            this_amount = 40000

            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == 'comedy':
            this_amount = 30000

            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)
            
            this_amount += 300 * perf['audience']
        else:
            raise Exception(f'unknown type {play["type"]}')
        
        # Soma créditos por volume
        volume_credits += max([perf['audience'] - 30, 0])

        # Soma um crédito extra para cada dez espectadores de comédia
        if 'comedy' == play['type']:
            volume_credits += math.floor(perf['audience'] / 5)

        #  Exibe a linha para esta requisição
        result += f' {play["name"]}: {this_amount / 100:0,.2f} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f'Amount owed is {total_amount / 100:0,.2f}\n'
    result += f'You earned {volume_credits} credits\n'
    return result



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
