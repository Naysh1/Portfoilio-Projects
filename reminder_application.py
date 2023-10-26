import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Please Take some rest",
            message = "Taking breaks during the workday can also reduce stress, improve mental health, and maintain a healthy work-life balance. All of these things tie into employee engagement and job satisfaction.",
            app_icon = "C:\\Users\\Asus\\Desktop\\My Projects\\icon.ico",
            timeout = 3,
            ticker = "hey"
        )
        time.sleep(10)