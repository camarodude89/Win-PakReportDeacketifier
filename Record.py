#!/usr/bin/env python

class Record:
    # Yes, I know personnel is misspelled in __init__, that's because it's spelled that way in Win-Pak
    def __init__(self, card_num, first_name='N/A', last_name='N/A', all_doors='No', office_personal='No',
                 plant_access='No'):
        self.card_num = card_num
        self.first_name = first_name
        self.last_name = last_name
        self.all_doors = 'No' if all_doors == '' else all_doors
        self.office_personal = 'No' if office_personal == '' else office_personal
        self.plant_access = 'No' if plant_access == '' else plant_access

    def __str__(self):
        txt = 'Card Number: {}\nName: {}, {}\nAll doors 24/7 365 Days a Year: {}\nOffice Personal: {}\nPlant 24-7 ' \
              'access: {} '
        return txt.format(self.card_num, self.last_name, self.first_name, self.all_doors, self.office_personal,
                          self.plant_access)
