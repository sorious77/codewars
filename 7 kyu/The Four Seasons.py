def four_seasons(d):
    if d > 365:
        return 'The year flew by!'
    elif 80 <= d and d <= 171:
        return 'Spring Season'
    elif 172 <= d and d <= 263:
        return 'Summer Season'
    elif 264 <= d and d <= 354:
        return 'Autumn Season'
    else:
        return 'Winter Season'
    pass
