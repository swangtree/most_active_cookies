"""
Most active cookie problem from Quantcast - Samuel Wang
-------------------------------------------------------
-I considered adding error handling for cases with invalid file paths, but I didn't in the interest of efficiency
and because it wasn't mentioned under the assumptions
"""
import argparse
from typing import List
from exception import BadInputException
import regex as re
from datetime import datetime

def parse_input():
    """
    Parses input and returns a parser with file_path and date
    """
    parser = argparse.ArgumentParser(description = "Return the most active cookie for specified day")
    parser.add_argument("file_path", help = "Path to cookie log file")
    parser.add_argument("-d", "--date", help = "Date in YYYY-MM-DD format")
    return parser.parse_args()

def find_most_active_cookies(file_path, given_date) -> List[str]:
    """
    Finds the most active cookie(s) from a file at a given date
    :param file_path: (string) file path
    :param given_date: (string) date to check
    :return: (string list) list of names of most active cookies
    """
    
    # Open file, validate, convert and aggragate value
    cookies = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() == "cookie,timestamp":
                continue
            try:
                cookie, timestamp = line.strip().split(",")
                time = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S+00:00")
                date = time.date()
                # date = timestamp.split("T")[0]
                # With regex
                # data_match = re.search("\d\d\d\d-\d\d-\d\d$", date).group(0)
                # if data_match is None:
                #     raise Exception()
            except BadInputException as e:
                raise e
            except ValueError as e:
                raise ValueError(f"""Time format is not correct, the error msg is :\n{str(e)}""")
            except Exception as e:
                raise e

            if str(date) == str(given_date):
                if cookie not in cookies:
                    cookies[cookie] = 1
                else:
                    cookies[cookie] += 1

    # Process output, find most used cookie
    max_number = max(cookies.values()) if cookies else 0
    most_active_cookies = [cookie for cookie, number in cookies.items() if number == max_number]

    return most_active_cookies

def parse_file(file_path) -> List[str]:
    # Open file, validate, convert and aggragate value
    cookies = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() == "cookie,timestamp":
                continue
            try:
                cookie, timestamp = line.strip().split(",")
                time = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S+00:00")
                date = time.date()
                # date = timestamp.split("T")[0]
                # With regex
                # data_match = re.search("\d\d\d\d-\d\d-\d\d$", date).group(0)
                # if data_match is None:
                #     raise Exception()
                cookies.append((cookie, time))

            except BadInputException as e:
                raise e
            except ValueError as e:
                raise ValueError(f"""Time format is not correct, the error msg is :\n{str(e)}""")
            except Exception as e:
                raise e

            return cookies


def max_cookies_on_day(cookies, given_date):
    cookie_dict = {}

    for cookie, timestamp in cookies:
        if str(timestamp.date()) == str(given_date):
            if cookie not in cookie_dict:
                cookie_dict[cookie] = 1
            else:
                cookie_dict[cookie] += 1
    
    max_number = max(cookie_dict.values()) if cookie_dict else 0
    most_active_cookies = [cookie for cookie, number in cookie_dict.items() if number == max_number]

    return most_active_cookies

def main():
    args = parse_input()
    file_path = args.file_path
    given_date = args.date

    try:
        date = datetime.strptime(given_date, "%Y-%m-%d").date()
        # most_active_cookies = find_most_active_cookies(file_path, given_date)
        cookie_list = parse_file(file_path)
        most_active_cookies = max_cookies_on_day(cookie_list, given_date)

    except ValueError as e:
        raise ValueError(f"Please check input time: {given_date}")
    
    # Returns most active cookies
    for cookie in most_active_cookies:
        print(cookie)

if __name__ == '__main__':
    main()