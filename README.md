This software sends a 5-digit code by receiving a mobile number through the sms.ir system. If the user enters the code correctly, the user's image is captured via webcam using the OpenCV library and stored in the "storage" folder, within a subfolder named after the user's mobile number. The database used in this project is MySQL, so enter the necessary connection information in the "database.py" file.
 
To send SMS messages, you must enter the API key and line number received from the sms.ir system in the "Notifier.py" file.

Note that all passwords in the database are stored encrypted, and the encryption key is stored in the "key.key" file. Therefore, after setting up the project, take great care in maintaining and protecting this key.

Also, all activities are stored as events in a file named "activity.log" using the "Logger.py" file.

Additionally, this project utilizes all CRUD operations.

