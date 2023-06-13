from cap1.statement import html_statement


def test_success_html_statement_function():
    plays = {
        "hamlet": {"name": "Hamlet", "type": "tragedy"},
        "as-like": {"name": "As You Like It", "type": "comedy"},
        "othello": {"name": "Othello", "type": "tragedy"}
    }
    invoice = {
        "customer": "BigCo",
        "performances": [
            {
                "playID": "hamlet",
                "audience": 55
            },
            {
                "playID": "as-like",
                "audience": 35
            },
            {
                "playID": "othello",
                "audience": 40
            }
        ]
    }
    
    result = (
        '<h1>Statement for BigCo</h1>\n'
        '<table>\n'
        '  <tr><th>play</th><th>seats</th><th>cost</th></tr>\n'
        '  <tr><td>Hamlet</td><td>55</td><td>650.00</td></tr>\n'
        '  <tr><td>As You Like It</td><td>35</td><td>580.00</td></tr>\n'
        '  <tr><td>Othello</td><td>40</td><td>500.00</td></tr>\n'
        '</table>\n'
        '<p>Amount owed is <em>1,730.00</em></p>\n'
        '<p>You earned <em>47</em> credits</p>\n'
    )

    assert html_statement(invoice, plays) == result
