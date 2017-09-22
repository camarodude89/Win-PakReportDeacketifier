#!/usr/bin/env python

import csv
from Record import Record

class Report:

    # Column indices
    cols = {
        'Card Number': 0,
        'First Name': 1,
        'Last Name': 2,
        'Access Levels': range(3, 11)
    }

    # Long header titles
    ALL_DOORS_STR = 'All Doors 24/7 365 Days a Year'
    OFFICE_PERSONAL_STR = 'Office Personal'
    PLANT_ACCESS_STR = 'Plant 24-7 access'

    # Report headers
    col_headers = ["Card Number", "First Name", "Last Name"]
    col_headers_full = ["Card Number", "First Name", "Last Name", ALL_DOORS_STR, OFFICE_PERSONAL_STR,
                        PLANT_ACCESS_STR]

    record_list = []

    def __init__(self, filename):
        self.filename = filename
        self._process_csv()

    def _process_csv(self):

        with open(self.filename, 'r') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)

            for row in csv_reader:

                card_num = row[self.cols['Card Number']]
                first_name = row[self.cols['First Name']]
                last_name = row[self.cols['Last Name']]

                all_doors = ''
                office_personal = ''
                plant_access = ''

                for cell in self.cols['Access Levels']:

                    if row[cell] == "":
                        break
                    if row[cell] == self.ALL_DOORS_STR:
                        all_doors = 'Yes'
                        continue
                    if row[cell] == self.OFFICE_PERSONAL_STR:
                        office_personal = 'Yes'
                        continue
                    if row[cell] == self.PLANT_ACCESS_STR:
                        plant_access = 'Yes'

                self.record_list.append(Record(card_num, first_name=first_name, last_name=last_name,
                                               all_doors=all_doors, office_personal=office_personal,
                                               plant_access=plant_access))

    def generate_winpak_report(self):

        with open('Front_Door_and_Break_Room_Access.csv', 'w', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(self.col_headers)

            for record in self.record_list:
                csv_writer.writerow([str(record.card_num), record.first_name, record.last_name])

    def generate_winpak_report_full(self):

        with open('Front_Door_and_Break_Room_Access_Full.csv', 'w', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(self.col_headers_full)

            for record in self.record_list:
                csv_writer.writerow([str(record.card_num), record.first_name, record.last_name, record.all_doors,
                                    record.office_personal, record.plant_access])