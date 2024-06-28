from dotenv import load_dotenv
import os
import requests
import sqlite3

def get_routes():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    date = '6/25/2024' # Date should be in <mm/dd/yyyy> format
    api_url = f'https://api.bart.gov/api/route.aspx?cmd=routes&key={api_key}&date={date}&json=y'

    response = requests.get(api_url)
    routes = response.json()  

    conn = sqlite3.connect('bart.db')
    cur = conn.cursor()

    insert = '''
            INSERT OR IGNORE INTO route VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''

    for route in routes['root']['routes']['route']:
        name = parse_name(route['name'])
        cur.execute(insert, (
            int(parse_date(date) + standardize_num(int(route['number']))),
            name[0],
            name[1],
            route['abbr'],
            int(route['number']),
            route['hexcolor'],
            route['color'],
            route['direction'],
            date
        ))

    conn.commit()
    conn.close()

def parse_name(name):
    name = name.split(' to ')
    if len(name) > 2:
        raise Exception('Route name parsing error')
    return name
    
def parse_date(date):
    date = date.split('/')
    parsed = date[0] + date[1] + date[2]
    return parsed

def standardize_num(num):
    if num < 10:
        return f'0{num}'
    else:
         return str(num)
