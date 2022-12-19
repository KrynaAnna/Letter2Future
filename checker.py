from mail import Mail
import pandas as pd
from datetime import datetime
import pytz

date_yesterday = datetime.strptime('2022-11-03', '%Y-%m-%d').date()
date_today = datetime.now(pytz.timezone('Canada/Eastern')).date()

database = pd.read_sql_table('data', 'sqlite:///data.db')

while date_today != date_yesterday:
    for i in range(len(database)):
        if database['date_future'][i].date() == date_today:
            params = {
                "to": database['recipient'][i],
                "sender": "capsule.in.future@gmail.com",
                "subject": f"Hello {database['name'][i]}, this your letter from past {database['date_past'][i].date()}",
                "msg_html": database['body'][i],
                "attachments": [f"static/images/customer/{database['img_url'][i]}"],
                "signature": True
            }

            mail = Mail(params)

    date_yesterday = date_today
