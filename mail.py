from googleapiclient.errors import HttpError
from simplegmail import Gmail


class Mail:
    def __init__(self, params):
        self.count_msg = 0
        self.flag = True
        self.params = params

    @property
    def send_message(self):
        # params = {
        #     "to": "krynaann13@gmail.com",
        #     "sender": "capsule.in.future@gmail.com",
        #     # "cc": ["bob@bobsemail.com"],
        #     # "bcc": ["marie@gossip.com", "hidden@whereami.com"],
        #     "subject": "My first email",
        #     "msg_html": "<h1>Woah, my first email!</h1><br />This is an HTML email.",
        #     "msg_plain": "Hi\nThis is a plain text email.",
        #     # "attachments": ["path/to/something/cool.pdf", "path/to/image.jpg", "path/to/script.py"],
        #     "signature": True
        # }

        try:
            if Gmail().send_message(**self.params):
                self.count_msg += 1

            if self.count_msg >= 100:
                messages = Gmail().get_sent_messages()
                [messages[i].trash() for i in range(len(messages))]
                self.count_msg = 0
        except HttpError:
            self.flag = False
        print(self.count_msg)
        return f'self.flag'
