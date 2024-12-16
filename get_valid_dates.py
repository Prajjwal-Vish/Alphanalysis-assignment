from datetime import datetime

# Function to validate start_date and end_date
def get_valid_dates():
    while True:
        try:
            start_date = input("Enter Starting date in YYYY-MM-DD format: ")
            end_date = input("Enter Ending date in YYYY-MM-DD format: ")
            
            start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")
            end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")
            
            # Checking if end_date >= start_date
            if end_date_dt >= start_date_dt:
                return start_date, end_date
            else:
                print("Error: Ending date must be greater than or equal to the starting date. Please try again.")
        except ValueError:
            print("Invalid date format. Please enter dates in YYYY-MM-DD format.")

