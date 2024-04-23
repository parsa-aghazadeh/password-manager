from Logger import Logger
from Notifier import SMS
from random import randrange
from ErrorHandler import ErrorHandler
from database import PasswordManagerDB
from CV import Webcam
MyWebcam = Webcam()
DB = PasswordManagerDB()
SmsNotifier = SMS()


class Menu:
    def Login(self):
        mobile = input('Enter Your Mobile Number: ')
        Logger.add(f'User entered {mobile}')
        if mobile[:2] == '09' and mobile.isnumeric() and len(mobile) == 11:
            Logger.add('entered mobile number is correct')
            random_code = randrange(10000,100000)
            SmsNotifier.send(mobile,'code: '+str(random_code))
            Logger.add(f'sent code:{random_code} to mobile:{mobile}')
            get_code = int(input('Enter code :'))
            Logger.add(f'User entered code : {get_code}')
            if get_code == random_code:
                user_id = DB.get_or_create_user_id_by_mobile(mobile)
                Logger.add('User entered code equal to sent code')
                Logger.add(f'The user with mobile:{mobile} is logged in')
                MyWebcam.capture()
                MyWebcam.saver(mobile)
                return (True,user_id)
        else:
            Logger.add(f'entered mobile number is incorrect')
            raise ValueError(ErrorHandler.mobile_check)
        return (False,None)
    
    def MainMenu(self,user_id):
        selection = int(input('1. Add info \n2. Get info\n3. Edit\n4. Delete\n5. Logout\n6. Exit\n:'))
        Logger.add(f'User entered{selection}')
        if selection == 1:
            self.AddInfo(user_id)
        elif selection == 2:
            self.GetInfo(user_id)
        elif selection == 3:
            self.UpdateInfo(user_id)  
        elif selection == 4:
            self.DeleteInfo(user_id)
        elif selection == 5:
            self.Logout()
        elif selection == 6:
            self.Exit()
        else:
            print('Invalid input')
            self.MainMenu(user_id)
    
    def AddInfo(self,user_id):
        Logger.add(f'User selected option 1(add info) ')
        url = input('Enter url :')
        username = input('Enter username :')
        password = input('Enter password :')
        Logger.add(f'user entered url:{url} and username:{username} and password:*')
        DB.create_info(user_id, url, username, password)
        Logger.add(f'user added info with url:{url} and username:{username} and password:*')
        self.MainMenu(user_id)
        
    def GetInfo(self,user_id):
        Logger.add(f'user selcted option 2(get info)')
        url = input('Enter url :')
        Logger.add(f'user entered url:{url}')
        information_of_user = DB.get_info_by_user_id_and_url(user_id,url)
        print(information_of_user)
        Logger.add(f'get info by user id:{user_id} and url:{url}')
        self.MainMenu(user_id)
        
    def UpdateInfo(self,user_id):
        Logger.add(f'user selcted option 3(update info)')
        url = input('Enter url : ')
        Logger.add(f'user entered url:{url}')
        username = input('Enter username : ')
        Logger.add(f'user entered username:{username}')
        is_exists = DB.check_info_is_exists_by_user_id_url_username(user_id, url, username)
        Logger.add(f'check info is exists by user id:{user_id} and url:{url} and username:{username}')
        if not is_exists:
            Logger.add(f'info NOT is exists by user id:{user_id} and url:{url} and username:{username}')
            raise Exception(ErrorHandler.info_not_found_by_url_and_username)
        else:
            Logger.add(f'info is exists by user id:{user_id} and url:{url} and username:{username}')
            new_username = input('new username :')
            new_password = input('new password :')
            Logger.add(f'user entered new username:{new_username} and mew password:*')
            update_info = DB.update_info_username_and_password(user_id, username, new_username,new_password,url)
            print(update_info)
            Logger.add(f'update info with url:{url} and old username:{username} by new username:{new_username} and new password:*')
        self.MainMenu(user_id)
        
    def DeleteInfo(self,user_id):
        Logger.add(f'user selcted option 3(Delete info)')
        url = input('Enter url : ')
        username = input('Enter username : ')
        Logger.add(f'user entered url:{url} and username:{username}')
        is_exists = DB.check_info_is_exists_by_user_id_url_username(user_id, url, username)
        Logger.add(f'check info is exists by user id:{user_id} and url:{url} and username:{username}')
        if not is_exists:
            Logger.add(f'info NOT is exists by user id:{user_id} and url:{url} and username:{username}')
            raise Exception(ErrorHandler.info_not_found_by_url_and_username)
        else:
            Logger.add(f'info is exists by user id:{user_id} and url:{url} and username:{username}')
            delete_info = DB.delete_info(url,username, user_id)
            print(delete_info)
            Logger.add(f'deleted info by user id:{user_id} and url:{url} and username:{username}')
        self.MainMenu(user_id)
        
    def Logout(self):
        Logger.add('The user logged out')
        is_logged_in,user_id = self.Login()
        if is_logged_in:
            self.MainMenu(user_id)
            
    def Exit(self):
        exit()