from tortoise import fields
from tortoise.models import Model

from app.validators.user_validator import NullOrPositive


class User(Model):
    """
    Telegram user model
    """
    id = fields.BigIntField(pk=True)

    username = fields.CharField(max_length=32, null=True, default=None)
    is_admin = fields.BooleanField(default=False)
    notification = fields.BooleanField(default=False)
    percent = fields.FloatField(null=True, default=1.0, validators=[NullOrPositive()])

    modified_at = fields.DatetimeField(auto_now=True)


class TradingPair(Model):
    """
    Trading pair model
    """

    id = fields.BigIntField(pk=True)

    pair = fields.CharField(max_length=60)
    market = fields.CharField(max_length=16, default="futures")
    price = fields.FloatField(default=None, validators=[NullOrPositive()])

    publication_date = fields.DatetimeField(auto_now_add=True)
