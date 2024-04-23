from sms_ir import SmsIr
from ErrorHandler import ErrorHandler
class SMS:
    def send(self,receiver_number, message):
        try: 
            test = True
            if not test:
                sms_ir = SmsIr('<api-key>','<line-number>')
                sms_ir.send_sms(receiver_number,message,'<line-number>')
            else:
                print(message)
        except Exception as err:
            handler = ErrorHandler()
            handler.error_print(str(err))