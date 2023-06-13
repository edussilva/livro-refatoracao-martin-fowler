import math


class PerformanceCalculator:
    def __init__(self, performance, play):
        self.performance = performance
        self.play = play


def create_statement_data(invoice, plays):
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
        return sum([item['volume_credits'] for item in statement_data['performances']])
    
    def total_amount(statement_data):
        return sum([item['amount'] for item in statement_data['performances']])

    def enrich_performance(performance):
        calculator = PerformanceCalculator(performance, play_for(performance))

        result = performance.copy()
        result['play'] = calculator.play
        result['amount'] = amount_for(result)
        result['volume_credits'] = volume_credits_for(result)
        return result

    statement_data = {}
    statement_data['customer'] = invoice['customer']
    statement_data['performances'] = list(map(enrich_performance, invoice['performances']))
    statement_data['total_volume_credits'] = total_volume_credits(statement_data)
    statement_data['total_amount'] = total_amount(statement_data)
    return statement_data
