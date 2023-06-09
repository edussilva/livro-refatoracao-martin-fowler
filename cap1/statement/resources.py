import math


class PerformanceCalculator:
    def __init__(self, performance, play):
        self.performance = performance
        self.play = play

    @property
    def amount(self):
        raise NotImplementedError('Not implemented yet')
    
    @property
    def volume_credits(self):
        return max([self.performance['audience'] - 30, 0])


class TragedyCalculator(PerformanceCalculator):
    @property
    def amount(self):
        result = 40000
        if self.performance['audience'] > 30:
            result += 1000 * (self.performance['audience'] - 30)        
        return result


class ComedyCalculator(PerformanceCalculator):
    @property
    def amount(self):
        result = 30000
        if self.performance['audience'] > 20:
            result += 10000 + 500 * (self.performance['audience'] - 20)
        result += 300 * self.performance['audience']
        return result

    @property
    def volume_credits(self):
        return super().volume_credits + math.floor(self.performance['audience'] / 5)
    

def create_performance_calculator(performance, play):
    if play['type'] == 'tragedy':
        return TragedyCalculator(performance, play)
    elif play['type'] == 'comedy':
        return ComedyCalculator(performance, play)
    
    raise Exception(f'unknown type {play["type"]}')

    
def create_statement_data(invoice, plays):
    def play_for(performance):
        return plays[performance['playID']]

    def total_volume_credits(statement_data):
        return sum([item['volume_credits'] for item in statement_data['performances']])
    
    def total_amount(statement_data):
        return sum([item['amount'] for item in statement_data['performances']])

    def enrich_performance(performance):
        calculator = create_performance_calculator(performance, play_for(performance))

        result = performance.copy()
        result['play'] = calculator.play
        result['amount'] = calculator.amount
        result['volume_credits'] = calculator.volume_credits
        return result

    statement_data = {}
    statement_data['customer'] = invoice['customer']
    statement_data['performances'] = list(map(enrich_performance, invoice['performances']))
    statement_data['total_volume_credits'] = total_volume_credits(statement_data)
    statement_data['total_amount'] = total_amount(statement_data)
    return statement_data
