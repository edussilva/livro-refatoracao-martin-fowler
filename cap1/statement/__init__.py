from .render import render_plained_text, render_html
from .resources import create_statement_data


def statement(invoice, plays):
    return render_plained_text(create_statement_data(invoice, plays))


def html_statement(invoice, plays):
    return render_html(create_statement_data(invoice, plays))
