import math




def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def amount_for(performance):
        result = 0

        if play_for(performance)['type'] == 'tragedy':
            result = 40000

            if performance['audience'] > 30:
                result += 1000 * (performance['audience'] - 30)
        elif play_for(performance)['type'] == 'comedy':
            result = 30000

            if performance['audience'] > 20:
                result += 10000 + 500 * (performance['audience'] - 20)
            
            result += 300 * performance['audience']
        else:
            raise Exception(f'unknown type {play_for(performance)["type"]}')

        return result

    def play_for(performance):
        return plays[performance['playID']]
    
    for perf in invoice['performances']:
        # Soma créditos por volume
        volume_credits += max([perf['audience'] - 30, 0])

        # Soma um crédito extra para cada dez espectadores de comédia
        if 'comedy' == play_for(perf)['type']:
            volume_credits += math.floor(perf['audience'] / 5)

        #  Exibe a linha para esta requisição
        result += f' {play_for(perf)["name"]}: {amount_for(perf) / 100:0,.2f} ({perf["audience"]} seats)\n'
        total_amount += amount_for(perf)

    result += f'Amount owed is {total_amount / 100:0,.2f}\n'
    result += f'You earned {volume_credits} credits\n'
    return result
