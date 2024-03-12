import os
import csv
import lxml
from bs4 import BeautifulSoup


dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'force-app/main/default/connectedApps')

# path = 'force-app/main/default/connectedApps'

allConnectedApps = []
attributes = ['label', 'description', 'contactEmail', 'consumerKey', 'certificate']

for connectedAppMetadata in os.listdir(path):
    
    if connectedAppMetadata.endswith('.xml'):
        
        f = open(f'{path}/{connectedAppMetadata}', 'r', encoding='utf-8')
        xml_file = f.read()
        xml_data = BeautifulSoup(xml_file, features='xml')

        thisConnectedApp = []

        for attribute in attributes:
            thisConnectedApp.append(xml_data.find(attribute).text if xml_data.find(attribute) is not None else '')

        allConnectedApps.append(thisConnectedApp)

with open('connected_apps.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(attributes)
    writer.writerows(allConnectedApps)