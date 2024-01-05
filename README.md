# DGC_selenium_init

---

# Selenium Test Script Documentation

## Overview

This document provides an overview of a Selenium test script written in Python. The script is designed to perform two main functions: `test_search_in_posts` and `test_pagination_in_post`. These functions involve interacting with a web application, specifically searching for random words in post headers and checking pagination functionality.

### Prerequisites

- Python 3.x
- Selenium WebDriver
- Web browser (Chrome, Firefox, etc.)
- `creds` file with URL, username, and password information

## Script Structure

The script is organized into functions, each serving a specific purpose. The main functions are as follows:

### 1. `test_search_in_posts`

This function searches for random words in the headers of post results. It retrieves the URL, username, and password from the `creds` file and interacts with the web application using Selenium WebDriver.

#### Steps:

1. Read credentials from the `creds` file.
2. Open the web browser and navigate to the specified URL.
3. Log in using the provided username and password.
4. Perform a search using random words from post headers.
5. Verify the search results.

### 2. `test_pagination_in_post`

This function checks the correctness of post results in the posts table when pagination is changed from 10 to 20 and 30.

#### Steps:

1. Read credentials from the `creds` file.
2. Open the web browser and navigate to the specified URL.
3. Log in using the provided username and password.
4. Change pagination settings to 10, 20, and 30.
5. Verify the number of results in the posts table for each pagination setting.

## Future Implementations

1. We can extend the script to give out all possible scenarios added to the testcase sheet at - https://docs.google.com/spreadsheets/d/1fv3eHIIIEs3DMxVaM3a4xN0tzayK6PSS3gQVVHPrS8Y/edit#gid=1766581807
2. We can randomize the scenarios to get different results and check for small issues that are not always put through while manual testing.
3. Once scaled for the website, the script can be run to check the testcases after every deployment without any new changes to be made.

## Usage

1. Ensure that Python and the required dependencies are installed.
2. Create a `creds` file with the following format:

   ```
   https://example.com
   your_username
   your_password
   ```

3. Run the script using the following command:

   ```bash
   python automation_init.py
   ```
