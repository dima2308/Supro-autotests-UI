import datetime


def get_start_and_end_dates():
    start_date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    end_date = (datetime.datetime.today() +
                datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
    return start_date, end_date
