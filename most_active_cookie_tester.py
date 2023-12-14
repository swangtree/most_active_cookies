from most_active_cookie import *

def parse_input_tester():
    """
    Tests that parse_input returns the correct file_path and date using 'python most_active_cookie_tester.py file_path.csv -d 2023-11-18'
    python most_active_cookie.py cookie_log.csv -d 2018-12-09
    """

    parser = parse_input()

    # Correct file path and date
    assert parser.file_path == "file_path.csv"
    assert parser.date == "2023-11-18"

    # Incorrect file path and date
    assert parser.file_path != "wrong_file_path.csv"
    assert parser.date != "2022-11-18"

    assert ValueError("ValueError: Time format is not correct, the error msg is : time data '2018-12-0909T14:19:00+00:00' does not match format '%Y-%m-%dT%H:%M:%S+00:00'")

    return True

def find_most_active_cookies_tester():
    """
    Tests edge cases and empty files
    """

    # Date not in file
    assert find_most_active_cookies("test1.csv", "2023-11-18") == []

    # Empty file
    assert find_most_active_cookies("test2.csv", "2023-11-18") == []

    # One entry file
    assert find_most_active_cookies("test3.csv", "2018-12-07") == ["fbcn5UAVanZf6UtG"]

    # Boundary cases
    assert find_most_active_cookies("test1.csv", "2018-12-10") == ["FIRSTCOOKIE"]
    assert find_most_active_cookies("test1.csv", "2018-12-06") == ["LASTCOOKIE"]

    # Multiple most active cookies on same date
    assert set(find_most_active_cookies("test1.csv", "2018-12-08")) == {"fbcn5UAVanZf6UtG", "4sMM2LxV07bPJzwf", "SAZuXPGUrfbcn5UA"}
    assert set(find_most_active_cookies("test1.csv", "2018-12-10")) != {"fbcn5UAVanZf6UtG", "4sMM2LxV07bPJzwf", "SAZuXPGUrfbcn5UA"}

    # Duplicate cookies on one timestamp
    assert find_most_active_cookies("test1.csv", "2018-12-07") == ["4sMM2LxV07bPJzwf"]

    return True


def data_processing():
    print("Testing parse_input ... ")
    print("PASS" if parse_input_tester() else "FAIL")

    print("Testing find_most_active_cookies ... ")
    print("PASS" if find_most_active_cookies_tester() else "FAIL")

if __name__ == "__main__":
    data_processing()