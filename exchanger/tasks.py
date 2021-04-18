
"""Tasks."""
from celery import shared_task

import requests

from hillel_lesson.settings import EXCHANGE_RATES_SOURCE

from exchanger.models import ExchangeRate


BASE_CCY = ['UAH']
UPDATE_FIELDS = ['sale', 'buy', 'created', 'trend_buy', 'trend_sale']


@shared_task
def get_exchange_rates():
    """get_exchange_rates function."""
    resp = requests.get(EXCHANGE_RATES_SOURCE)
    resp = resp.json()
    exchange_rates = [get_exchange_rate(d) for d in filter_out_rates(resp)]
    ExchangeRate.objects.bulk_update_or_create(exchange_rates, UPDATE_FIELDS, match_field='currency_id')


def filter_out_rates(rates):
    """filter_out_rates function."""
    for r in rates:
        if r['base_ccy'] not in BASE_CCY:
            continue
        else:
            yield r


def get_exchange_rate(rate):
    """get_exchange_rate function."""
    currency_id = rate['ccy'] + rate['base_ccy']
    old_exchange_rate = ExchangeRate.objects.get(currency_id = currency_id)
    return ExchangeRate(
        currency_id = currency_id,
        currency_ccy = rate['ccy'],
        currency_base_ccy = rate['base_ccy'],
	    buy = rate['buy'],
        sale = rate['sale'],
        trend_buy = comparison_rate(old_exchange_rate.buy, rate['buy']),
        trend_sale = comparison_rate(old_exchange_rate.sale, rate['sale'])
    )


def comparison_rate(rate_old, rate_new):
    """comparison_rate function."""
    rate_old = float(rate_old)
    rate_new = float(rate_new)
    if rate_old == rate_new:
        return '0'
    elif rate_old > rate_new:
        return '-1'
    else:
        return '1' 