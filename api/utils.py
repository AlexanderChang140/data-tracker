def parse_date(date):
    date = date.split('/')
    parsed = date[0] + date[1] + date[2]
    return parsed

def standardize_num(num):
    if num < 10:
        return f'0{num}'
    else:
         return str(num)