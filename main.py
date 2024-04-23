from database import PasswordManagerDB
from ErrorHandler import ErrorHandler
from Menu import Menu
MyMenu = Menu()
DB = PasswordManagerDB()
DB.boot()
try:
    is_logged_in,user_id = MyMenu.Login()
    if is_logged_in:
        MyMenu.MainMenu(user_id)                    
except Exception as err:
    handler = ErrorHandler()
    handler.print(str(err))