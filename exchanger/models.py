"""Models."""
from django.db import models

from django.utils import timezone

from bulk_update_or_create import BulkUpdateOrCreateQuerySet


class ExchangeRate(models.Model):
    """ExchangeRate class."""

    objects = BulkUpdateOrCreateQuerySet.as_manager()

    currency_id = models.CharField(max_length=6, primary_key=True)

    currency_ccy = models.CharField(max_length=3)
    currency_base_ccy = models.CharField(max_length=3)

    buy = models.DecimalField(max_digits=8, decimal_places=2)
    trend_buy = models.CharField(max_length=2)

    sale = models.DecimalField(max_digits=8, decimal_places=2)
    trend_sale = models.CharField(max_length=2)

    created = models.DateTimeField(default=timezone.now)

    def to_dict(self):
        """ExchangeRate to_dict function."""
        return {
            f"{self.currency_ccy}_buy": self.buy,
            f"{self.currency_ccy}_trend_buy": self.trend_buy,
            f"{self.currency_ccy}_sale": self.sale,
            f"{self.currency_ccy}_trend_sale": self.trend_sale,
        }