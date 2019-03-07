import requests
from bs4 import BeautifulSoup

import os
import csv

# Specify the file to write to
output_path = os.path.join("output", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','District of Columbia','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']

    for state in states:
        source = requests.get("https://www.indeed.com/jobs?l=" + str(state) +"&jt=fulltime").text

        soup = BeautifulSoup(source, 'lxml')

        counts = soup.find("div", {"id": "searchCount"}).text

        counts = counts.split()[3]

        csvwriter.writerow([state, counts])