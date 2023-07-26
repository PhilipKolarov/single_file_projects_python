HOURS_DISPLAY = 'h'
MINUTES_DISPLAY = 'm'
SECONDS_DISPLAY = 's'


def transform_seconds(n, new_metric):
    result = n

    if new_metric == 'minutes':
        result //= 60
        extra_result = n % 60
        return [result, MINUTES_DISPLAY, extra_result, SECONDS_DISPLAY]

    elif new_metric == 'hours':
        result //= 60
        first_extra_result = n % 60
        second_extra_result = n % 60
        return [result, HOURS_DISPLAY, first_extra_result, MINUTES_DISPLAY, second_extra_result, SECONDS_DISPLAY]


def transform_minutes(n, new_metric):
    result = n

    if new_metric == 'hours':
        result //= 60
        extra_result = result % 60
        return [result, HOURS_DISPLAY, extra_result, MINUTES_DISPLAY]

    elif new_metric == 'seconds':
        result *= 60
        return [result, SECONDS_DISPLAY]


def transform_hours(n, new_metric):
    result = n

    if new_metric == 'minutes':
        result *= 60
        return [result, MINUTES_DISPLAY]

    elif new_metric == 'seconds':
        result *= 3600
        return [result, SECONDS_DISPLAY]


def time_calculator(num, current_metric, wanted_metric):
    result = ''

    if current_metric == 'seconds':
        result = transform_seconds(num, wanted_metric)

    elif current_metric == 'minutes':
        result = transform_minutes(num, wanted_metric)

    elif current_metric == 'hours':
        result = transform_hours(num, wanted_metric)

    string_to_return = ''

    for el in result:
        if isinstance(el, str) and el != result[-1]:
            string_to_return += f'{el} '
        else:
            string_to_return += f'{el}'
    return string_to_return


print(time_calculator(150, 'seconds', 'minutes'))
print(time_calculator(6080, 'seconds', 'hours'))
print(time_calculator(3, 'minutes', 'seconds'))
print(time_calculator(68, 'minutes', 'hours'))
print(time_calculator(3, 'hours', 'seconds'))
print(time_calculator(1, 'hours', 'minutes'))
