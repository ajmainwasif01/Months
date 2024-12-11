import calendar
import datetime

def display_months():
    print("Months of the Year:")
    for month in range(1, 13):
        month_name = calendar.month_name[month]
        print(f"{month}: {month_name}")

def display_current_date_and_time():
    current_time = datetime.datetime.now()
    print("\nCurrent Date and Time:")
    print(current_time.strftime("%Y-%m-%d %H:%M:%S"))

def display_calendar_for_year(year):
    print(f"\nCalendar for the year {year}:\n")
    print(calendar.TextCalendar().formatyear(year))

if __name__ == "__main__":
    
    display_months()

    
    display_current_date_and_time()


    current_year = datetime.datetime.now().year
    display_calendar_for_year(current_year)
