import math


def statement(invoice, plays):
    def play_for(performance):
        return plays[performance['playID']]
    
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

    def total_volume_credits(statement_data):
        result = 0
        for perf in statement_data['performances']:
            result += perf['volume_credits']
        
        return result
    
    def total_amount(statement_data):
        result = 0
        for perf in statement_data['performances']:
            result += perf['amount']
        return result

    def enrich_performance(performance):
        result = performance.copy()
        result['play'] = play_for(result)
        result['amount'] = amount_for(result)
        result['volume_credits'] = volume_credits_for(result)
        return result

    statement_data = {}
    statement_data['customer'] = invoice['customer']
    statement_data['performances'] = list(map(enrich_performance, invoice['performances']))
    statement_data['total_volume_credits'] = total_volume_credits(statement_data)
    statement_data['total_amount'] = total_amount(statement_data)
    return render_plained_text(statement_data, invoice, plays)


def render_plained_text(data, invoice, plays):
    def usd(number):
        return f'{number / 100:0,.2f}'
    


    result = f'Statement for {data["customer"]}\n'
    for perf in data['performances']:
        #  Exibe a linha para esta requisição
        result += f' {perf["play"]["name"]}: {usd(perf["amount"])} ({perf["audience"]} seats)\n'

    result += f'Amount owed is {usd(data["total_amount"])}\n'
    result += f'You earned {data["total_volume_credits"]} credits\n'
    return result
