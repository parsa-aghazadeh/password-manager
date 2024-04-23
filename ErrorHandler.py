class ErrorHandler:
    info_not_found_by_url_and_username = ('No info found for you with given url and username')
    info_not_found_by_url = ('No info found for you with given url')
    mobile_check = ('phone number is incorect Error')
    code_check = ('The code entered does not match the code sent Error')
    def print(self, message):
        print("An Error Found : "+message)
        exit()