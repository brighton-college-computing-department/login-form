# login-form
A login form that uses flask and sqlite
## Set Up
You will need the following things installed on your computer:
1. [Python 3](https://www.python.org/downloads/release/python-370/)
2. [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)
3. [DB Browser for SQLite](https://sqlitebrowser.org/)
4. [Brackets](http://brackets.io/)
5. [Git](https://git-scm.com/)

## Instalation
Read the guide below which explains how to create a flask project in pycharm, open the repository on git and run the application:

[Setup Guide](./LoginFormSetupGuide.pdf)
## Guide
Please find a video explainer below:

[![Listner to an explaination of the code here](https://img.youtube.com/vi/cvPnRmOs9io/0.jpg)](https://www.youtube.com/watch?v=cvPnRmOs9io)
## Next Steps
The following next steps need to be taken with this project:
1.  Create a registration.html page that inputs the users name, date of birth and address and then passes this to a register_user function in python that stores this in the database.  You will need to update the structure of the database using DB Browser.
2.  Update the log_the_user_in function so that it uses the user name to retrieve all the users details and displays them on the profile.html page
### Extensions
3.  Add validation to the registration.html page
4.  Add validation to the database schema and use try except to catch these errors in the app.py file
5.  Add a profile picture to the registration page


