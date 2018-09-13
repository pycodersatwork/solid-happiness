""" AWS Lambda handler to upload file to s3 bucket.
"""

import boto3
from utils.utils import ParseExcelWorkBook


def parse_workbook_handler(event, context):
    """ AWS Lambda function to parse an excel workbook.

    Args:
        event (dict)                 : AWS Lambda uses this parameter to pass
                                            in event data to the handler
                                            Expected Keys:
                                                'sheet': SheetName to parse.
                                                'workbook url': WorkBook Url.
        context (LambdaContext type) : AWS Lambda uses this parameter to
                                        provide runtime information to your
                                        handler.
    """
    sheet_name = event.get('sheet')
    work_book = event.get('workbook')

    simple_storage_service = boto3.resource('s3')
    simple_storage_service.create_bucket(Bucket=sheet_name)

    records = ParseExcelWorkBook.parse_excel_workbook_by_sheets(work_book)
    data = ParseExcelWorkBook.get_json_output(records)

    response = simple_storage_service.Object(sheet_name, 'your-key').put(
        Body=(bytes(data).encode('UTF-8')))

    return response
