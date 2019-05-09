import webbrowser
import time


# take time from user
user_time = int(input("Enter time to play a video after minutes: "))

# take url from user
user_url = input("Enter url to play video after what u time set: ")

# take number from user how many time to play video
user_repeatOpenBrowser = int(input("Enter how many time to play a after set the time"))

time_sec = user_time * 60 # convert minute to seconds
current_time = time.ctime()  # get current time

print("start time = " + current_time)  # print current time

i = 0
while (i < user_repeatOpenBrowser):
    time.sleep(time_sec) # pause execution what user set time in seconds "sleep" function works in second
    webbrowser.open(user_url)
    i += 1
