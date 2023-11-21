import argparse

def parse_input():
    """
    Parses input and returns a parser with file_path and date
    """
    parser = argparse.ArgumentParser(description = "Return the most active cookie for specified day")
    parser.add_argument("file_path", help = "Path to cookie log file")
    parser.add_argument("-d", "--date", help = "Date in YYYY-MM-DD format")
    return parser.parse_args()

def find_most_active_cookies(file_path, given_date):
    """
    Finds the most active cookie(s) from a file at a given date
    :param file_path: (string) file path
    :param given_date: (string) date to check
    :return: (string list) list of names of most active cookies
    """
    cookies = {}
    with open(file_path, 'r') as file:
        # Skip first row
        next(file)

        for line in file:
            cookie, timestamp = line.strip().split(",")
            date = timestamp.split("T")[0]

            if date == given_date:
                if cookie not in cookies:
                    cookies[cookie] = 1
                else:
                    cookies[cookie] += 1

    max_number = max(cookies.values()) if cookies else 0
    most_active_cookies = [cookie for cookie, number in cookies.items() if number == max_number]
    return most_active_cookies

def main():
    args = parse_input()
    file_path = args.file_path
    given_date = args.date

    most_active_cookies = find_most_active_cookies(file_path, given_date)
    
    # Returns most active cookies
    for cookie in most_active_cookies:
        print(cookie)

if __name__ == '__main__':
    main()