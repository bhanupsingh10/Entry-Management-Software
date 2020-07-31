# Entry-Management-Software

### Prerequisites
All the scripts I have made have been tested on **Windows** with **python version 3.6.0**. The SMS is sent to the user via **Twilio** and the version used is 2010-04-01. The e-mail is sent to the user via **SMTP** which is a Mail Transfer Protocol. The Graphical User Interface was created using **Tkinter**. The images to the software were added using the Python Imaging Library **(PIL)**  of version 6.2.0 . The database of the Visitors is handled by using **MySQL**. Version 5.7 of **MySQL** was used for database management. Contact numbers of Visitor and Host were validated by using a python library, **phonenumbers** of version 8.11.0 .
Email-id of host and visitor were validated by using python library, **validate_email** of version 1.3 .
Please refer **setup.txt**, the instruction guide for stting up the environment and will help in smooth working of the software. Also install all the libraries from **library_install.sh** shell script. 
 Execute the following command for the installation of the **requirements**:
 ```bash
 python -m pip install -r requirements.txt
 ```
### Why Twilio
**Twilio** is an open source cloud communications platform as a service which allows software developers programmatically to make and receive phone calls, send and receive text messages, and perform other communication functions using its web service APIs. **Twilio** uses Amazon Web Services to host telephony infrastructure and provide connectivity between HTTP and the public switched telephone network (PSTN) through its APIs.
**Twilio** uses a simple syntax written in many web languages.It is **completely agentless**. There are no agents/software or additional firewall ports that you need to install on the  client systems or hosts which you want to automate. The user have to register once so as to get their authentic token and account ID. The registration is **free of cost** on **Twilio**.  

### Why Tkinter
**Tkinter** is a Python binding, standard Python interface to the **Tk GUI toolkit**. **Tkinter** is included with standard Linux, Microsoft Windows and Mac OS X installs of Python. 
**Tkinter** provides a graphical interface based on Object Oriented structure to the user.It further reduces the effort required for your team to start automating right away.

### Why SMTP
The **Simple Mail Transfer Protocol (SMTP)** is a communication protocol for electronic mail transmission.SMTP is the Internet standard for sending and receiving emails. Email clients use SMTP to send messages to a mail server for delivery while email servers use it to forward messages to their recipients.
There are no agents/software or additional files that you need to install on the client systems or hosts which you want to automate. You do not have to separately set up a management infrastructure which includes managing your entire systems, network and storage.

### Why MySQL
**MySQL** is a free and open-source relational database management system (RDBMS).  **MySQL** is used by many database-driven web applications, including Drupal, Joomla, phpBB, and WordPress. **MySQL** is also used by many popular websites including Facebook,Flickr,MediaWiki, Twitter and YouTube.It can be used to store anything from a single record of information to an entire inventory of available products.It involves use of **Structured Query Language**.

### Why PIL
**Python Imaging Library** (abbreviated as **PIL**) is a free library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats. It is available for Windows, Mac OS X and Linux.Some of the file formats supported by **PIL** are PPM, PNG, JPEG, GIF, TIFF, and BMP. 

### Why validate_email
**Validate_email** is a package for Python that check if an email is valid, properly formatted and really exists. The main object that the package deals with is an **email-id** .

### Why phonenumbers
**Phonenumbers** is a Python port of Google's libphonenumber library. The main object that the library deals with is a **PhoneNumber** object. You have to specify the country that the phone number is being dialled from (unless the number is in E.164 format, which is globally unique). The **PhoneNumber** object still needs to be validated, to check whether it's a possible number (e.g. it has the right number of digits) or a valid number. 

### How it Works
This Entry Management GUI works by accepting details like Visitor's Name, Phone number, Email Address, Host Name from the
user in the Entry tab and storing them at the backend (by creating a mysql database).
                          The **Home-Screen GUI** Image of Entry Management Software.
                          
![alt text](https://github.com/bhanupsingh10/Entry-Management-Software/blob/master/Images/home_screen.png)



**Database details :**
Visitor Name, Visitor Phone number, Visitor Email ID, Host Name, Host Phone number, Host Email ID, Check-in time, Check-out time.
                                  **How data is stored** in the table in the Database.

![alt text](https://github.com/bhanupsingh10/Entry-Management-Software/blob/master/Images/data_stored.png)
If the host details are there in the database, then they are directly fetched or otherwise a pop-up window opens and ask the user to enter correct details.All the entries are to be properly filled without leaving any of them empty as leaving empty would result in displaying and error message pop-up box which would ask the user to fill the required details.

Once the visitor checks in, an Email is triggered to the Host informing the host about the details of the visitor.
The **e-mail sent to the host** about the contact no. of Visitor.


![alt text](https://github.com/bhanupsingh10/Entry-Management-Software/blob/master/Images/host_email_check-in.png)
An SMS is also sent to the host on his/her mobile no. once the visitor checks-in. The SMS is sent from the number on **Twilio** to the registered number.


![alt text](https://github.com/bhanupsingh10/Entry-Management-Software/blob/master/Images/checkin_host_sms.png)

After the meeting or visit is over, the visitor is supposed to check-out and enter his email id in the check-out window.
The **Check-Out Screen GUI** Image of Entry Management Software.

![alt text](https://github.com/bhanupsingh10/Entry-Management-Software/blob/master/Images/checkout_screen.PNG)

The check-out button inturn triggers an **email to the visitor** after meeting is over and visitor has checked-out stating the details of the meeting(check-in time and check-out time),address of the meeting and Visitor's details like Name,email id and phone number.

![alt text](https://github.com/bhanupsingh10/Entry-Management-Software/blob/master/Images/visitor_email_check-out.png)

The database is updated at every Entry and Exit operation with Entry and Exit time of the Visitor.

### Additional Feature :
As all the entries are compulsary for the user to enter, if the visitor leaves any entry empty
or does not enter a valid email id a warning message is shown on the screen.
The email address and phone number of Visitor and Host are validted.
Here are few of the exceptions handled by the software:

When the user enters the **invalid email-id of host**, a message is shown in the pop-up which asks to enter correct host email-id.

When the user enters the **invalid contact number of host**, a message is shown in the pop-up which asks to enter correct visitor contact    number.

### Limitations :
As messaging service is paid, hence the trial version does not send SMS everytime to the Host.
If the sql server password is wrongly entered, the application has to be restarted.

### Future prospects :
Making a seperate UI for entry of Host data.
Displaying waiting message for a visitor if the host is in a meeting. And sending SMS/Email to the visitor once the Host is free.
Making the host choose his meeting hours. A message - 'Host not available' can be shown on the screen in this case.


