### <a href="http://kryna.pythonanywhere.com/">Use App</a>

# Capsule
Capsule is a web app that allows anyone to write a letter to their future self.

# Description
The main work of the program is based on the Python web framework Flask.

Capsule is a web app that allows anyone to write a letter to their future self. 
This application functions with the help of the Pythonanywhere server, using the open source database - SQLite/MySQL. 
The design was created using HTML/CSS/JS, for developing responsive website used Bootstrap.
The preliminary template of the site was developed on the web platform - Сanva. The graphic elements were drawn by me in the CorelDraw program.

# Logic
The main logic of the application is to send a letter to the future using the simplgmail library. The file main.py starts the server and works on the Flask framework. This allows you to see a web page, fill out a form and send it to the database on the server. The file checker.py is run on the pythonanywhere platform as a task that runs daily at 00:01, it checks the database for emails that are due to be sent today. If there are such letters, it starts the file mail.py. The file mail.py performs the process of sending a letter to the consumer, if the number of sent messages exceeds 100, the messages are deleted to the trash in order not to fill the memory of the mailbox.

# Topics covered
<li>Python</li>

<li>Flask Web Framework, Jinja</li>

<li>HTML, CSS, JavaScript

<li>SQLAlchemy, Pythonanywhere(MySQL)</li>

<li>SimpleGmail</li>

<li>OOP</li>

<li>Functions</li>

# File tree
To use the simplegmail, we need a token to connect to the Gmail API and receive credentials. So below I will provide the complete file tree.
![image](https://user-images.githubusercontent.com/98818064/208489295-341132fe-8d6b-4796-bfd6-240d40fe6546.png)


# Template & graphic elements
![K A P S U L A ](https://user-images.githubusercontent.com/98818064/208470375-70480953-4b5a-48ac-bba9-4564154dccc0.png)
<img src="https://user-images.githubusercontent.com/98818064/208478660-2d570c6a-f844-4259-916c-aff18b7c9ae0.png" width=600px>
