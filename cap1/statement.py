import math


def statement(invoice, plays):
    def play_for(performance):
        return plays[performance['playID']]
    
    def enrich_performance(performance):
        result = performance.copy()
        result['play'] = play_for(performance)
        return result

    statement_data = {}
    statement_data['customer'] = invoice['customer']
    statement_data['performances'] = list(map(enrich_performance, invoice['performances']))
    return render_plained_text(statement_data, invoice, plays)


def render_plained_text(data, invoice, plays):
    def usd(number):
        return f'{number / 100:0,.2f}'

    def amount_for(performance):
        result = 0

        if performance['play']['type'] == 'tragedy':
            result = 40000

            if performance['audience'] > 30:
                result += 1000 * (performance['audience'] - 30)
        elif performance['play']['type'] == 'comedy':
            result = 30000

            if performance['audience'] > 20:
                result += 10000 + 500 * (performance['audience'] - 20)
            
            result += 300 * performance['audience']
        else:
            raise Exception(f'unknown type {play_for(performance)["type"]}')

        return result


    def volume_credits_for(performance):
        result = 0
        result += max([performance['audience'] - 30, 0])

        if 'comedy' == performance['play']['type']:
            result += math.floor(performance['audience'] / 5)

        return result

    def total_volume_credits():
        result = 0
        for perf in data['performances']:
            result += volume_credits_for(perf)
        
        return result
    
    def total_amount():
        result = 0

        for perf in data['performances']:
            result += amount_for(perf)

        return result

    result = f'Statement for {data["customer"]}\n'
    for perf in data['performances']:
        #  Exibe a linha para esta requisição
        result += f' {perf["play"]["name"]}: {usd(amount_for(perf))} ({perf["audience"]} seats)\n'

    result += f'Amount owed is {usd(total_amount())}\n'
    result += f'You earned {total_volume_credits()} credits\n'
    return result
