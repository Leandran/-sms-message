#An SMS Simulation


class SMSMessage():

    def __init__(self,fromNumber,messageText):
        self.fromNumber = fromNumber
        self.messageText = messageText
        self.hasBeenRead = False
        self.SMSStore = []
       
 

    def MarkAsRead(self):
        self.hasBeenRead = True
        

            
        
    def add_sms(self,text,number):
        addsms = SMSMessage(text,number)
        self.SMSStore.append(addsms)
        


    def get_count(self):
        num_messages = len(self.SMSStore)
        print(num_messages)

        

    def get_message(self,index):
        sms = self.SMSStore[index]
        print(sms.messageText)


    def get_unread_messages():
       print([unread for unread in self.SMSStore])


    def remove(self,sms):
        for message in self.SMSStore:
            if message == sms:
                self.SMSStore.remove(message)
                
        


while True:

    menu = """

        1. Send SMS
        2. Read SMS
        3. Delete SMS
        4. Quit

        """
    print(menu)

    userChoice = int(input("Choice: "))

    if userChoice == 1:
        sender_number = input("Sender Number: ")
        message_text = input("Message body: ")
        sms = SMSMessage(sender_number, message_text)
        print("sms sent to", sender_number )
    elif userChoice == 2:
        index = int(input("Enter the message index: "))
    elif userChoice == 3:
        index = int(input("Enter the message index to delete: "))
    elif userChoice == 4:
        break
    else:
        print("Oops - incorrect input")
