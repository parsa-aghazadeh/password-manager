from datetime import datetime
class Logger:
    def add(log_message:str):
        current_dateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('activity.log','a') as log_file:
            log_file.write(f"{current_dateTime} {log_message}\n")