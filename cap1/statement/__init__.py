from .render import render_plained_text
from .resources import create_statement_data


def statement(invoice, plays):
    return render_plained_text(create_statement_data(invoice, plays))
