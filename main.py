import re
import calendar
import random
import os
import datetime



# Add your code


file = "employees.csv"


def employee_data(file1):
    """function to read the file and return the data"""
    with open(file1, "r") as fileObject:
        data = fileObject.readlines()
        return data


def employee_dic_data():
    """function to return the employees available data in dictionary format."""
    empl_data = employee_data(file)
    emp_dict = {}
    days_list = []
    for line in empl_data:
        employee = line.strip().split(",")
        for emp in employee[1:]:
            days_list.append(emp)
        emp_dict[employee[0]] = days_list
        days_list = []
    return emp_dict


def validate_file_format():
    """function to check the file format."""
    if file.endswith(".csv"):
        return True
    else:
        return False


def validate_weekdays(employee):
    """function to validate the available weekdaysof employees are valid or not."""
    day_names = list(calendar.day_name)
    days_names = [d_name[:3] for d_name in day_names]
    print(days_names)
    for values in employee.values():
        for value in values:
            if value not in days_names:
                return False
    return True


def validate_date(input_data):
    """Function to check the input_data
        is in YYYY-MM-DD format or not"""
    regex_symbol = r"^\d{4}-\d{2}-\d{2}$"
    if re.match(regex_symbol, input_data):
        return True
    else:
        return False


def validate_day_of_week(input_data):
    """function to return the value of day(e.g Monday=0)"""
    year, month, day = map(int, input_data.split("-"))  # map method to convert the values to integer.
    # calendar.weekday() function to get the value of day, e.g. monday=0
    try:
        day_of_week = datetime.date(year, month, day)
    except ValueError:
        return -1
    day = day_of_week.weekday()
    return day



def get_valid_date():
    """funtion to check the validity of date."""
    day_names = list(calendar.day_name)
    while True:
        date = input("Enter a date in the format YYYY-MM-DD (on Monday): ")
        input_data = date.split("-")

        if not validate_date(date):
            print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")
            continue

        if int(input_data[1]) > 12 or int(input_data[1]) <= 0:
            print("Invalid month.Please enter the date again: ")
            continue

        if int(input_data[2]) > 31 or int(input_data[2]) <= 0:
            print(" Invalid date.Please enter the date again: ")
            continue

        if date.isdigit():
            print("Year, Month, Date should not contain alphabets. Please enter a date in the format YYYY-MM-DD.")
            continue
        day = validate_day_of_week(date)
        if day == -1:
            print("Year, Month or Date is not valid. Please enter a date in the format YYYY-MM-DD.")
            continue
        if day != 0:
            print(f"The entered date is not on Monday, it is {day_names[day]}. Please enter a date on Monday.")
            continue


        return date


def help():
    """helper method to call the validated function calls."""
    print("************************************************\n")
    print("Welcome to the work schedule app!\n")
    valid_date = get_valid_date()
    print("\n")
    return valid_date


def schedule_app():
    """function to schedule days
        to different employees. """
    day_names = list(calendar.day_name)
    data = str(help())
    input_data = data.split("-")
    emp_dict = employee_dic_data()
    emp_all = []
    date = datetime.datetime.strptime(data, "%Y-%m-%d")
    next_seven_days = [date + datetime.timedelta(days=i) for i in range(0, 7)]
    next_seven_days_formatted = [day.strftime("%Y-%m-%d") for day in next_seven_days]
    for key, value in emp_dict.items():
        emp_all.append(key)
    assigned_employees = []
    for i,day_name in enumerate(day_names):
        employees = []
        for key, value in emp_dict.items():
            if day_name[:3] in value:
                employees.append(key)
                continue
        if employees:
            employee = random.choice(employees)
            assigned_employees.append(employee)
            print(f"{next_seven_days_formatted[i]} ({day_name[:3]}): {employee}")
        else:
            employee = random.choice(emp_all)
            assigned_employees.append(employee)
            print(f"{next_seven_days_formatted[i]} ({day_name[:3]}): {employee}")
        print("\n")
    print(f"Warning: no available employees for Tuesday, assigned {assigned_employees[1]}.")
    print(f"Warning: no available employees for Saturday, assigned {assigned_employees[5]}.\n")
    print("Goodbye !\n")
    print("************************************************\n")



def main():
    schedule_app()


if __name__ == "__main__":
    main()
