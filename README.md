# fuzzy-carnival

### Requirement:
    - Download the xlsx from - https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.xls
    - Store the xlsx
    - Read the tab titled "MICs List by CC"
    - Create a list of dict containing all rows (except row 1). The values in row 1 would be the keys for in each dict.
    - Store the list from step 4) as a .json file in an AWS S3 bucket
    - The above function should be run as an AWS Lambda


### Assessment criteria:

    Percentage of requirements satisfied
    How clean the code is - In particular simplicity, readability, naming, pep8 validation, test coverage and error handling.

### Code includes
- utils
    + tests
- aws lambda function (parseExcelLambdaFunction)
