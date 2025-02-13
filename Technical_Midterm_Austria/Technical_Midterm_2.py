def convert_date(date_str):
    month_str, day_str, year_str = date_str.split('/')
    month = int(month_str)
    day = int(day_str)
    year = int(year_str)
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    formatted_date = f"{months[month]} {day}, {year}"
    return formatted_date

date_input = input("Enter the date (mm/dd/yyyy): ")
print(f"Date Output: {convert_date(date_input)}")