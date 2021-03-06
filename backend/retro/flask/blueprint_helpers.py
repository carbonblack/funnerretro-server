import datetime
import decimal
import json
from flask import make_response
from retro.utils import timedelta_total_seconds, unix_time_millis


def default_encoder(obj):
    """
    JSON encoder function for special classes.
    """
    if isinstance(obj, datetime.datetime):
        return unix_time_millis(obj.timestamp())
    if isinstance(obj, datetime.timedelta):
        return timedelta_total_seconds(obj)
    elif isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError(repr(obj) + " is not JSON serializable")


# wrapper around the flask make_response method that includes encoding to json
def make_response_json(data, *args, **kwargs):
    if not data:
        response = make_response_empty()
    else:
        json_kwargs = {"default": default_encoder}
        json_kwargs.update(kwargs)
        response = make_response(json.dumps(data, *args, **json_kwargs))
    response.headers['Content-Type'] = "application/json; charset=utf-8"
    return response


def make_response_success_json():
    return make_response_json({"result": "success"})


def make_response_empty(status=204):
    return make_response("", status)
