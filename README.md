# API Testing Project

This project demonstrates API testing using Python, focusing on the Fake Store API (https://fakestoreapi.com/).

## Project Structure
The project has the following structure:

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AlexKomanov/api-demo-python-cursor.git
   cd api-demo-python-cursor
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run all tests:
   ```bash
   pytest
   ```

2. Run specific test file:
   ```bash
   pytest tests/test_products.py
   ```

3. Run tests with detailed output:
   ```bash
   pytest -v
   ```
4. Run tests with self-contained HTML report:
   ```bash
   pytest --html=report.html --self-contained-html
   ```
   This command generates a detailed HTML report of the test results, which includes information about passed, failed, and skipped tests, along with any error messages. The `--self-contained-html` option ensures that all necessary resources are included in a single file, making it easy to share and view the report without external dependencies.


## Test Results
The following is a summary of the test results from the latest run:

- **Total Tests:** 7
- **Passed:** 7
- **Failed:** 0
- **Skipped:** 0
- **Expected Failures:** 0
- **Unexpected Passes:** 0
- **Errors:** 0
- **Duration:** 00:00:02

### Screenshot of Test Report
![Test Report](@2024-11-23_20-14-49.png)



