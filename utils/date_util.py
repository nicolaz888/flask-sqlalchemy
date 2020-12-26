from datetime import date, datetime


def get_date(date_str: str):
    return datetime.strptime(date_str, '%d/%m/%Y')
