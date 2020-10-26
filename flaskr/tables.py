from flask_table import Table, Col

class Results(Table):
    name = Col('Name')
    ticker = Col('Ticker')
    slope = Col('Slope')