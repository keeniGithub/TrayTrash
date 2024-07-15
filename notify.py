from plyer import notification

def notify(msg, title):
    notification.notify(message=msg, app_name='script', title=title)