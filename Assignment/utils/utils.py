""" Utilities - To parse excel workbook.
"""

import json
import pandas as pd


class ParseExcelWorkBook:
    @staticmethod
    def parse_excel_workbook_by_sheets(workbook, worksheet=None):
        """ Parse the excel workbook.
        """
        try:
            xls_worksheet = pd.read_excel(workbook, worksheet)
            ParseExcelWorkBook.fill_nan(xls_worksheet, '')
            records_as_list_of_dict = [
                dict(zip(xls_worksheet.keys(), rec))
                for rec in xls_worksheet.values
            ]
            return records_as_list_of_dict
        except Exception as err:
            err_msg = "Failed to open WorkBook: \n Traceback: {0}".format(err)
            raise Exception(err_msg)

    @staticmethod
    def fill_nan(data_frame, substitute, replace=True):
        """ Fill nan by replacement character on dataframe.

        Args:
            dataFrame (DataFrame)   : DataFrame to replace nan.
            replace (str)           : Replacement string.
            apply (bool)            : Apply on dataframe.

        Returns
            (dataFrame)             : DataFrame object with replaced nan.

        """
        if isinstance(data_frame, pd.core.frame.DataFrame):
            if replace:
                data_frame.fillna(substitute, inplace=replace)
            else:
                return data_frame.fillna(substitute)
        else:
            return None

        return data_frame

    @staticmethod
    def get_json_output(data, indent=0):
        """ get JSON string from data

        Args:
            data (object)   : Builtin datatypes.

        Returns:
            (json object)   : Returns json object.
        """
        return json.dumps(data, indent=indent)


if __name__ == "__main__":
    work_book = "https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.xls"
    work_sheet = "MICs List by CC"
    S = ParseExcelWorkBook(work_book, work_sheet)
    R = S.parse_excel_workbook_by_sheets()
    print(ParseExcelWorkBook.get_json_output(R))
