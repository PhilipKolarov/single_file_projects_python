def transform_seconds(n, new_metric):
    result = n

    if new_metric == 'minutes':
        result //= 60
        extra_result = result % 60
        return [result, extra_result]

    elif new_metric == 'hours':
        result //= 60
        first_extra_result = result % 60
        second_extra_result = result % 60
        return [result, first_extra_result, second_extra_result]

    return result


def transform_minutes(n, new_metric):
    result = n

    if new_metric == 'hours':
        result //= 60
        extra_result = result % 60
        return [result, extra_result]

    elif new_metric == 'seconds':
        result *= 60
        return result


def transform_hours(n, new_metric):
    result = n

    if new_metric == 'minutes':
        result *= 60

    elif new_metric == 'seconds':
        result *= 3600

    return result


def time_calculator(num, current_metric, wanted_metric):
    if current_metric == 'seconds':
        transform_seconds(num, wanted_metric)

    elif current_metric == 'minutes':
        transform_minutes(num, wanted_metric)

    elif current_metric == 'hours':
        transform_hours(num, wanted_metric)
