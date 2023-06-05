import math


def statement(invoice, plays):
    total_amount = 0
    result = f'Statement for {invoice["customer"]}\n'

    def usd(number):
        return f'{number / 100:0,.2f}'

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

    def volume_credits_for(performance):
        result = 0
        result += max([performance['audience'] - 30, 0])

        if 'comedy' == play_for(performance)['type']:
            result += math.floor(performance['audience'] / 5)

        return result

    def total_volume_credits():
        volume_credits = 0
        for perf in invoice['performances']:
            volume_credits += volume_credits_for(perf)
        
        return volume_credits
    
    for perf in invoice['performances']:
        #  Exibe a linha para esta requisição
        result += f' {play_for(perf)["name"]}: {usd(amount_for(perf))} ({perf["audience"]} seats)\n'
        total_amount += amount_for(perf)

    result += f'Amount owed is {usd(total_amount)}\n'
    result += f'You earned {total_volume_credits()} credits\n'
    return result
