class MailboxSensor: 
    def __init__(self): 
        self.mail_present = False; 
    
    def detect_mail(self): 
        self.mail_present = True; 
    
    def clear_mail(self): 
        self.mail_present = False; 

    def status(self): 
        return self.mail_present; 
