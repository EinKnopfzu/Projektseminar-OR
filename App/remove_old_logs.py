import os
import datetime
import logging

def remove_old_logs():
     # Define the maximum age in days
    max_age_in_days = 7  # Change this to your desired maximum age

    # Current date
    current_date = datetime.datetime.now()

    # Iterate through all files in the folder
    for file in os.listdir("logs\\"):
        file_path = os.path.join("logs\\", file)

        # Check if the file is older than the maximum age
        file_info = os.stat(file_path)
        file_created_date = datetime.datetime.fromtimestamp(file_info.st_ctime)
        file_age = current_date - file_created_date

        # Delete the file if it's older than the maximum age
        if file_age.days > max_age_in_days:
            os.remove(file_path)
            logging.info(f"Deleted: {file_path}")
