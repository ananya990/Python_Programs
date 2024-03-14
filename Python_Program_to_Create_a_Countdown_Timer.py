import time  # Import the time module to work with time-related functions

def countdown(time_sec):
    # Loop until the time_sec becomes 0
    while time_sec:
        # Calculate minutes and seconds from the remaining time
        mins, secs = divmod(time_sec, 60)
        # Format the time as 'MM:SS'
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        # Print the formatted time, overwrite the previous output with '\r' to update the output in place
        print(timeformat, end='\r')
        # Wait for 1 second using time.sleep
        time.sleep(1)
        # Decrease the remaining time by 1 second
        time_sec -= 1

    # After the loop finishes, print 'stop' to indicate the end of countdown
    print("stop")

# Call the countdown function with an initial time of 5 seconds
countdown(5)
