import mysql.connector 
from ErrorHandler import ErrorHandler
from Cryptographer import Cryptographer

class PasswordManagerDB:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
            host = '<db-host>',
            user = '<db-user>',
            password = '<db-pass>',
            auth_plugin='mysql_native_password')
            self.cursor = self.connection.cursor()
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS <db-name>")
            self.cursor.execute('USE <db-name>')
        except Exception as err:
            handler = ErrorHandler()
            handler.print(str(err))

    def boot(self):
        try:
            self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS users (
                            id int(11) primary key auto_increment,
                            mobile varchar(11) NOT NULL UNIQUE
                        )
                        ''')

            self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS info  (
                            id int(11) primary key auto_increment,
                            user_id int(11),
                            url VARCHAR(200),
                            username VARCHAR(200),
                            password varchar(255),
                            FOREIGN KEY (user_id) REFERENCES users(id),
                            UNIQUE(user_id,url,username)
                            )
                            ''')
        except Exception as err:
            handler = ErrorHandler()
            handler.print(str(err))
            
        
    def get_or_create_user_id_by_mobile(self,mobile:str):
        try:
            self.cursor.execute(f'SELECT id FROM users WHERE mobile="{mobile}"')
            found_user = self.cursor.fetchone()
            if found_user!=None and len(found_user)>0:
                user_id = found_user[0]
            else:
                self.cursor.execute(f'INSERT INTO users (mobile) VALUES ("{mobile}")')
                self.connection.commit()
                self.cursor.execute(f'SELECT id FROM users WHERE mobile="{mobile}"')
                user_id = self.cursor.fetchone()[0]
            return user_id
        except Exception as err:
            handler = ErrorHandler()
            handler.print(str(err))

    def create_info(self,user_id, url, username, password):
        password = Cryptographer.encrypt(password)
        try:
            
            self.cursor.execute(f'INSERT INTO info (user_id,url,username,password) VALUES ("{user_id}","{url}","{username}","{password}")')
            self.connection.commit()
        except Exception as err:
            handler = ErrorHandler()
            handler.print(str(err))
            
            
            
    def get_info_by_user_id_and_url(self,user_id:int,url:str):
        try:
            self.cursor.execute(f'SELECT username,password FROM info WHERE url="{url}" AND user_id="{user_id}"')
            result_info = self.cursor.fetchall()
            if result_info!=[] and len(result_info)>0:
                result = []
                for info in result_info:
                    result.append({
                        'username' : info[0],
                        'password' : Cryptographer.decrypt(info[1])
                        })
                return result
            else:
                raise Exception(ErrorHandler.info_not_found_by_url)
        except Exception as err:
            handler = ErrorHandler()
            handler.print(str(err))
        
    def update_info_username_and_password(self,user_id, username, new_username,new_password,url):
        new_password =Cryptographer.encrypt(new_password)
        self.cursor.execute(f"UPDATE info SET username='{new_username}',password='{new_password}' WHERE url='{url}' AND user_id='{user_id}' AND username='{username}'")
        self.connection.commit()
        return 'Updated successfully'
        
    def delete_info(self,url, username,user_id):
        try:
            self.cursor.execute(f"DELETE FROM info WHERE url='{url}' AND user_id='{user_id}' AND username='{username}'")
            self.connection.commit()
            return 'Delete successfully'
        except Exception as err:
            handler = ErrorHandler()
            handler.print(str(err))
        
    def check_info_is_exists_by_user_id_url_username(self, user_id, url, username):
        try:
            self.cursor.execute(f'SELECT id FROM info WHERE url="{url}" AND user_id="{user_id}" AND username="{username}"')
            result = self.cursor.fetchone()
            if result != None:
                return True
            else:
                return False
        except Exception as err:
            handler = ErrorHandler()
            handler.print(str(err))