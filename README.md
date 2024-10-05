# pytest_api

## Overview

`pytest_api` is a Python-based project designed for testing APIs using the **pytest** framework. This project facilitates the automated testing of API endpoints and provides detailed reports of test results.

## Features

- Easy-to-use structure for API testing.
- Support for custom requests and response validation.
- Integration with the **pytest-html** plugin for generating comprehensive HTML reports.

## Prerequisites

- Python 3.6 or higher
- `pip` for installing dependencies

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rubanenkos/pytest_api.git
   cd pytest_api

2. Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

4. Run tests with HTML report: 
    ```bash
    pytest --html=report.html

This will activate the pytest-html plugin and instruct it to generate an HTML report of your test results.