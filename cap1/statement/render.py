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


def render_html(data):
    def usd(number):
        return f'{number / 100:0,.2f}'
    
    result = f'<h1>Statement for {data["customer"]}</h1>\n'
    result += '<table>\n'
    result += '  <tr><th>play</th><th>seats</th><th>cost</th></tr>\n'
    for perf in data['performances']:
        result += f'  <tr><td>{perf["play"]["name"]}</td><td>{perf["audience"]}</td><td>{usd(perf["amount"])}</td></tr>\n'
    result += '</table>\n'

    result += f'<p>Amount owed is <em>{usd(data["total_amount"])}</em></p>\n'
    result += f'<p>You earned <em>{data["total_volume_credits"]}</em> credits</p>\n'
    return result
