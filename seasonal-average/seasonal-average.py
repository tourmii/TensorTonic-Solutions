
def seasonal_average(series: list, period: int) -> list:
    """
    Returns the average for each position in the seasonal cycle.
    """
    # Write code here
    res = []
    for i in range(period):
        cur_sum = 0
        count = 0
        for j in range(i, len(series), period):
            cur_sum += series[j]
            count += 1
        res.append(cur_sum/count)
    return res