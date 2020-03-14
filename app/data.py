import csv
import datetime
import config
import json

def generate_data():

    data = read_csv()
    json_data = create_blob(data)

    return json_data

def read_csv():
    """ read the csv file """

    country = 'Country/Region'
    state = 'Province/State'
    locations = ['New Hampshire', 'Massachusetts']
    local_totals = []

    data_dir = config.COVID_19_DIR + 'csse_covid_19_data/csse_covid_19_daily_reports/'

    d = datetime.datetime.today()
    year = str(d.year)
    month = d.strftime('%m')
    day = d.strftime('%d')

    daily_file = data_dir + month + '-'+ day + '-' + year + '.csv'
    daily_file = data_dir + month + '-'+ str('13') + '-' + year + '.csv'

    confirmed = 0
    dead = 0
    recovered = 0
    active = 0

    with open(daily_file, newline='', encoding='utf-8-sig') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            print(row)
            if row[country] == 'US':
                confirmed = confirmed + int(row['Confirmed'])
                dead = dead + int(row['Deaths'])
                recovered = recovered + int(row['Recovered'])

            for l in locations:
                if row[state] == l:
                    s = {'location': l, 'confirmed': row['Confirmed'], 'dead': row['Deaths'], 'recovered': row['Recovered'], 'active': str(int(row['Confirmed']) - (int(row['Deaths']) + int(row['Recovered'])))}
                    local_totals.append(s)

    active = confirmed - (dead + recovered)

    s = {'location': 'US', 'confirmed': str(confirmed), 'dead': str(dead), 'recovered': str(recovered), 'active': str(active)}
    local_totals.append(s)

    return local_totals

def create_blob(data):

    json_data = json.dumps(data)

    return json_data
