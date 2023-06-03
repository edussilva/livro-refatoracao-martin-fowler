import math


def amount_for(performance, play):
    result = 0

    if play['type'] == 'tragedy':
        result = 40000

        if performance['audience'] > 30:
            result += 1000 * (performance['audience'] - 30)
    elif play['type'] == 'comedy':
        result = 30000

        if performance['audience'] > 20:
            result += 10000 + 500 * (performance['audience'] - 20)
        
        result += 300 * performance['audience']
    else:
        raise Exception(f'unknown type {play["type"]}')

    return result


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    for perf in invoice['performances']:
        play = plays[perf['playID']]
    
        this_amount = amount_for(perf, play)

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
