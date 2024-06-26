from dotenv import load_dotenv
import os
import requests
import sqlite3
import utils

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
            (?, ?, ?, ?, ?, ?, ?, ?)
            '''

    for route in routes['root']['routes']['route']:
        cur.execute(insert, (
            int(utils.parse_date(date) + utils.standardize_num(int(route['number']))),
            route['name'],
            route['abbr'],
            int(route['number']),
            route['hexcolor'],
            route['color'],
            route['direction'],
            date
        ))

    conn.commit()
    conn.close()

