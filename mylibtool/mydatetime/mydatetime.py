import re
from mylibtool.mydatetime import core


# def get_datetime(text, custom_timezones=None, day_first=False):
#     """
#     Automatically convert/extract datetime from a text,
#     If you not sure about the format you can use this function,
#     Otherwise please use directly_datetime()/extract_datetime(), that's faster
#     ** Beware of that extract can't get tzinfo **
#     """
#     the_datetime = directly_datetime(text, custom_timezones, day_first=day_first)
#     if the_datetime:
#         # 直接转换时间
#         return the_datetime
#     else:
#         # 从文本抽取时间
#         return core.extract(text, day_first=day_first, method='datetime')


def directly_datetime(text, custom_timezones=None, day_first=False):
    """
    Convert a pure time string to datetime
    :param text: a pure datetime text
    :param custom_timezones: 自定义时区偏移字典，用来覆盖 timezone.py 里面的数据，列如 timezones_dic = {"CST": 8 * 3600}
    :param day_first:
    :return: datetime with tzinfo
    """
    return core.str2datetime(text, custom_timezones, day_first)


def extract_datetime(text, day_first=False):
    """
    Extract datetime from a text
    Beware of that extract can't get tzinfo
    :param text: a content include datetime text
    :param day_first:
    :return: datetime without tzinfo
    """
    return core.extract(text, day_first=day_first, method='datetime')


def extract_date(text, date_only=False, day_first=False):
    """
    Extract only date from a text
    :param text: a content include date/datetime text
    :param date_only: only return date string, or else with zero time
    :param day_first:
    :return: datetime without time and tzinfo
    """
    datetime_tmp = core.extract(text, day_first=day_first, method='date')

    if date_only:
        date = datetime_tmp.date()
        return date
    else:
        return datetime_tmp.replace(hour=0, minute=0, second=0)
