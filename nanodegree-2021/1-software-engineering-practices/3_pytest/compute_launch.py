def days_until_launch(current_day, launch_day):
    """"Returns the days left before launch.
    
    current_day (int) - current day in integer
    launch_day (int) - launch day in integer
    """
    #return launch_day - current_day
    return 0 if launch_day < current_day else launch_day - current_day
