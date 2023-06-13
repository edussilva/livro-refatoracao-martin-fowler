import pytest
from statement import statement, html_statement


# def test_ok_amount_for_play_tragedy():
#     performance = {
#         "playID": "hamlet",
#         "audience": 55
#     }
#     play = {"name": "Hamlet", "type": "tragedy"}

#     result = 65000
#     assert amount_for(performance, play) == result


# def test_ok_amount_for_play_comedy():
#     performance = {
#         "playID": "as-like",
#         "audience": 35
#     }
#     play = {"name": "As You Like It", "type": "comedy"}

#     result = 58000
#     assert amount_for(performance, play) == result


# def test_error_amount_for_play_other():
#     performance = {
#         "playID": "any",
#         "audience": 35
#     }
#     play = {"name": "Any", "type": "other"}

#     with pytest.raises(Exception):
#         amount_for(performance, play)


def test_success_statement_function():
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
        'Statement for BigCo\n'
        ' Hamlet: 650.00 (55 seats)\n'
        ' As You Like It: 580.00 (35 seats)\n'
        ' Othello: 500.00 (40 seats)\n'
        'Amount owed is 1,730.00\n'
        'You earned 47 credits\n'
    )

    assert statement(invoice, plays) == result


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
