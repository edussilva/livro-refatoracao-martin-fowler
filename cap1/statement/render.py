def render_plained_text(data):
    def usd(number):
        return f'{number / 100:0,.2f}'
    
    result = f'Statement for {data["customer"]}\n'
    for perf in data['performances']:
        #  Exibe a linha para esta requisição
        result += f' {perf["play"]["name"]}: {usd(perf["amount"])} ({perf["audience"]} seats)\n'

    result += f'Amount owed is {usd(data["total_amount"])}\n'
    result += f'You earned {data["total_volume_credits"]} credits\n'
    return result
