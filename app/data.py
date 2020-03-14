""" Data related functions """
import csv
import datetime
import config
import json

def generate_data():
    """ Read the csv file and extract what is requested and put it into json """

    # read the csv file and return the requested data
    data = read_csv()

    # put everything in a json array
    json_data = create_blob(data)

    return json_data

def read_csv():
    """ Read the csv file """

    # Set these make parsing a little neater
    country = 'Country/Region'
    state = 'Province/State'

    # Set this to a list of Province/State that need to be collected
    locations = ['New Hampshire', 'Massachusetts']

    # The totals for everything in a string format
    local_totals = []

    # The file we are using for the data points
    data_dir = config.COVID_19_DIR + 'csse_covid_19_data/csse_covid_19_daily_reports/'

    # The data is stored in csv files named like MM-DD-YYYY.csv The datetime here is used to build the filename for the current file. The files are only updated once a day at around 7:30pm EST.
    d = datetime.datetime.today()
    year = str(d.year)
    month = d.strftime('%m')
    day = d.strftime('%d')

    daily_file = data_dir + month + '-'+ day + '-' + year + '.csv'
    daily_file = data_dir + month + '-'+ str('13') + '-' + year + '.csv'

    # DATA POINTS WE WANT
    confirmed = 0
    dead = 0
    recovered = 0
    active = 0

    with open(daily_file, newline='', encoding='utf-8-sig') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            print(row)
            if row[country] == 'US': # Use other countries here if desired
                confirmed = confirmed + int(row['Confirmed'])
                dead = dead + int(row['Deaths'])
                recovered = recovered + int(row['Recovered'])

            for l in locations:
                if row[state] == l:
                    s = {'location': l, 'confirmed': row['Confirmed'], 'dead': row['Deaths'], 'recovered': row['Recovered'], 'active': str(int(row['Confirmed']) - (int(row['Deaths']) + int(row['Recovered'])))}
                    local_totals.append(s)

    # calculate the number of active cases
    active = confirmed - (dead + recovered)

    # append the data to an array
    s = {'location': 'US', 'confirmed': str(confirmed), 'dead': str(dead), 'recovered': str(recovered), 'active': str(active)}
    local_totals.append(s)

    return local_totals

def create_blob(data):
    """Put the dasta into json format"""

    json_data = json.dumps(data)

    return json_data
