#numerology_table.py
from pyairtable import Table as Airtable

api_key = "patVv6UZF6Nu8osdp.264bcf8203bd14bc9752c35998569bc0d19c262914c61f2eeac26006faa631b2"
base_id = "appxXH2hHvKn4DMLc"
table_name = "numerologytable"

numerologytable = Airtable(api_key, base_id, table_name)

class NumerologyTable:

    @staticmethod
    def create_record(fname, lname, dob, gender, psychic_number, destiny_number, kua_number, loshu_grid):
        # Create string representation of Loshu grid
        grid_representation = "\n".join([
            f"| {loshu_grid[4] or '__'} | {loshu_grid[9] or '__'} | {loshu_grid[2] or '__'} |",
            f"| {loshu_grid[3] or '__'} | {loshu_grid[5] or '__'} | {loshu_grid[7] or '__'} |",
            f"| {loshu_grid[8] or '__'} | {loshu_grid[1] or '__'} | {loshu_grid[6] or '__'} |"
        ])

        record = {
            'FName': fname,
            'LName': lname,
            'DOB': dob.strftime("%Y-%m-%d"),
            'Gender': gender,
            'Psychic': psychic_number,
            'Destiny': destiny_number,
            'Kua': kua_number,
            'Chart': grid_representation
        }

        numerologytable.create(record)

