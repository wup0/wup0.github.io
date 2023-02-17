import csv

COUNTRY_OF_ORIGIN = 9
COMMERCIAL_ENTITY = 8
COUNTRY_OF_DEPLOYMENT = 0
COLOR_CODE_RED = 10
COLOR_CODE_BLACK = 0
COUNTRY = 'Country'
COLOR = 'Color'


def add_country_entry(origin, deployment):
    if ',' in origin:
        origins = origin.split(', ')
        for origin in origins:
            add_country_entry(origin, deployment)
    else:
        entry = [deployment, COLOR_CODE_RED]
        if origin in data:
            self_deployment = [deployment, COLOR_CODE_BLACK]
            if entry not in data[origin] and self_deployment not in data[origin]:
                data[origin].append(entry)
        else:
            data[origin] = [[COUNTRY, COLOR], [origin, COLOR_CODE_BLACK]]
            data[origin].append(entry)


def add_product_entry(product, origin, deployment):
    if ',' in origin:
        origins = origin.split(', ')
    else:
        origins = [origin]
    entry = [deployment, COLOR_CODE_RED]
    if product in data:
        if entry[0] not in [d[0] for d in data[product]]:
            data[product].append(entry)
    else:
        data[product] = [[COUNTRY, COLOR]]
        for origin in origins:
            data[product].append([origin, COLOR_CODE_BLACK])
        if entry[0] not in [d[0] for d in data[product]]:
            data[product].append(entry)


# Create country mapping
data = {}
with open('spyware_countries.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    count = 0
    for row in csv_reader:
        if count > 0:
            add_country_entry(row[COUNTRY_OF_ORIGIN], row[COUNTRY_OF_DEPLOYMENT])
        count += 1

print(data)
# Create commercial entity mapping
data = {}
with open('spyware_countries.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    count = 0
    for row in csv_reader:
        if count > 0:
            add_product_entry(row[COMMERCIAL_ENTITY], row[COUNTRY_OF_ORIGIN], row[COUNTRY_OF_DEPLOYMENT])
        count += 1

print(data)
