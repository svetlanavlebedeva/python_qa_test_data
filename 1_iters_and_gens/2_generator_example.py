from datetime import datetime, timedelta


def generate_date_range(start_date, end_date, step_days=1):
    """
    Generates a range of dates from start_date to end_date with a given step.
    """
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    step = timedelta(days=step_days)

    while current_date <= end_date:
        yield current_date.strftime("%Y-%m-%d")
        current_date += step


start_date = '2023-01-01'
end_date = '2023-01-10'
for date in generate_date_range(start_date, end_date, 2):
    print(date)
