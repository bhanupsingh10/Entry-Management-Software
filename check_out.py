from twilio.rest import Client
import mysql.connector
import smtplib
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
from validate_email import validate_email
from sql_data import *
from checkout_screen import *

# Establishing the connection
mydb = mysql.connector.connect(host="localhost", user=str(username), passwd=str(sql_password), database="details")

# The function that wil work for checking-out
def check_out1(vmail):

    vmail_info = vmail.get()

    # Validating non-empty entries
    if(validate_email(vmail_info,verify = True)):
        cursor3 = mydb.cursor()
        qry = "select * from Office where vis_mail = %s"
        cursor3.execute(qry, (vmail_info,))
        fe = cursor3.fetchall()

        temp = 1

        for i in fe:
            nm = i[0]
            em = i[1]
            no = i[2]
            nm1= i[5]
            em1= i[6]
            no1= i[7]
            cin= i[3]
            cout= i[4]

        # Validating that the user has checked-in
            if em == vmail_info:
                temp = 2
        if(temp==1):
            tkinter.messagebox.showerror("ERROR!","Please check-in first")
        else:
            # Validating that user has not been checked-out
            if cout:
                tkinter.messagebox.showerror("ERROR!","You have already checked out")
            else:
                # Validating Correct Visitor email-id
                if(validate_email(vmail_info,verify = True)):

                    txt = "The details of your last meeting.\n"

                    #Updating the check-out time of the user who has checked out
                    sql1 = "update Office set check_out = NOW() where vis_mail = %s and check_out is NULL"
                    cursor3.execute(sql1,(vmail_info,))

                    #Saving the changes made in the database
                    mydb.commit()

                    # Retrieving details of the user who has checked-out
                    # Name of the visitor
                    qry1 = "select vis_name from Office where vis_mail=%s"
                    cursor3.execute(qry1, (vmail_info,))
                    dis_name = ""
                    for i in cursor3:
                        dis_name = str(i[0])

                    # Contact No. of the Visitor
                    qry2 = "select vis_mob from Office where vis_mail=%s"
                    cursor3.execute(qry2, (vmail_info,))
                    dis_mob = ""
                    for i in cursor3:
                        dis_mob = str(i[0])

                    # Check-in time of the visitor
                    qry3 = "select check_in from Office where vis_mail=%s"
                    cursor3.execute(qry3, (vmail_info,))
                    cin_time = ""
                    for i in cursor3:
                        cin_time = str(i[0])

                    # Check-out time of the visitor
                    qry4 = "select check_out from Office where vis_mail=%s"
                    cursor3.execute(qry4, (vmail_info,))
                    cout_time = ""
                    for i in cursor3:
                        cout_time = str(i[0])

                    # Host name with whom Visiter mate
                    qry5 = "select host_name from Office where vis_mail=%s"
                    cursor3.execute(qry5, (vmail_info,))
                    host_nm = ""
                    for i in cursor3:
                        host_nm = str(i[0])

                    # Host e-mail with whom Visiter mate
                    qry6 = "select host_mail from Office where vis_mail=%s"
                    cursor3.execute(qry6, (vmail_info,))
                    host_ml = ""
                    for i in cursor3:
                        host_ml = str(i[0])

                    # Host contact no. with whom Visiter mate
                    qry7 = "select host_mob from Office where vis_mail=%s"
                    cursor3.execute(qry7, (vmail_info,))
                    host_mb = ""
                    for i in cursor3:
                        host_mb = str(i[0])

                    # Message displayed in the e-mail
                    info = "Name: " + dis_name + "\nPhone No.: " + dis_mob + "\nCheck In time: " + cin_time + "\n" \
                        "Check Out time: " + cout_time + "\nHost Name: " + host_nm + "\nHost E-mail: " + host_ml + "\n" \
                        "Host Mobile No.: " + host_mb + "\nAddress: Innovacer Office"

                    # Sending e-mail to the visitor about the details of the meeting
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login(gmailid, password)
                    txt += info
                    server.sendmail(gmailid, vmail_info, txt)

                    # Showing confirmation of check-out
                    tkinter.messagebox.showinfo("SAVED", "Your have successfully checked-out!")
                # Handling all the exceptions
                else:
                    tkinter.messagebox.showerror("ERROR!","Please enter correct visitor e-mail id")
    else:
        tkinter.messagebox.showerror("ERROR!","Please enter correct visitor email-id")
