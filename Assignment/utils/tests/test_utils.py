import os as _os
from ..utils import ParseExcelWorkBook
import unittest
import xlwt


def create_workbook(workbook, worksheet):
    """ Create a workbook for testing.
    """
    excel_file = xlwt.Workbook()
    sheet = excel_file.add_sheet(worksheet)
    data = {
        'header': ['Roll number', 'Name'],
        'content': [
            (1, 'John'),
            (2, 'David'),
            (3, 'Mark'),
            (4, '')
        ]
    }

    for col, header in enumerate(data.get('header', [])):
        row = 0
        sheet.write(row, col, header)

    for row, contents in enumerate(data.get('content', []), 1):
        for col, content in enumerate(contents):
            sheet.write(row, col, content)

    excel_file.save(workbook)


class TestingUtils(unittest.TestCase):
    def setUp(self):
        """ Setup the resources to test.
        """
        resources = _os.path.abspath(_os.path.dirname(__file__))

        self.workbook = _os.path.join(
            resources, 'ISO10383_MIC.xls'
        )

        self.worksheet = "MICs List by CC"

        self.response = [
            {'Name': 'John', 'Roll number': 1},
            {'Name': 'David', 'Roll number': 2},
            {'Name': 'Mark', 'Roll number': 3},
            {'Name': '', 'Roll number': 4}
        ]

        create_workbook(self.workbook, self.worksheet)

    def test_workbook_parse_returns_list(self):
        """ Test the workbook parse utility returns list of records.
        """
        records = ParseExcelWorkBook.parse_excel_workbook_by_sheets(
            self.workbook, self.worksheet
        )
        self.assertTrue(isinstance(records, list))

    def test_workbook_validate_output(self):
        """ Test the workbook parse utility returns list of records.
        """
        records = ParseExcelWorkBook.parse_excel_workbook_by_sheets(
            self.workbook, self.worksheet
        )
        self.assertEqual(records, self.response)

    def test_workbook_validate_fill_na(self):
        """ Test the workbook parse utility returns list of records.
        """
        records = ParseExcelWorkBook.parse_excel_workbook_by_sheets(
            self.workbook, self.worksheet
        )
        self.assertEqual(records[3], self.response[3])

    def tearDown(self):
        """ Cleanup the resources
        """
        _os.unlink(self.workbook)
