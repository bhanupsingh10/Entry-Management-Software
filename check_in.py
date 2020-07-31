import mysql.connector
import smtplib
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
from validate_email import validate_email
from sql_data import *
from home_screen import *
from config_pass import *

# Establishing the connection
mydb = mysql.connector.connect(host="localhost", user=str(username), passwd=str(sql_password), database="details")

# The function that wil work for checking-in
def check_in(vname,vmail,vmob,hname,hmail,hmob):

    vname_info = vname.get()
    vmail_info = vmail.get()
    vmob_info = vmob.get()
    hname_info = hname.get()
    hmail_info = hmail.get()
    hmob_info = hmob.get()

    # Validating non-empty entries
    if(vname_info and vmail_info and vmob_info and hname_info and hmail_info and hmob_info):
        cursor1 = mydb.cursor()
        query = "select * from Office where vis_mail = %s"
        cursor1.execute(query,(vmail_info,))
        fe = cursor1.fetchall()

        temp = 1

        for i in fe:
            nm = i[0]
            em = i[1]
            if(vmail_info==em):
                if not i[4]:
                    temp = 2
                    break
            nm1 = i[5]
            em1 = i[6]
            no1 = i[7]
            cin = i[3]
        # Validating that the user has not checked-in
        if temp == 2:
            tkinter.messagebox.showerror("ERROR!","You have already checked in")
        else:
            # Validating Correct Visitor email-id
            if (validate_email(vmail_info, verify=True)):
                vmob_info = "+91"+vmob_info
                try:
                    # Validating correct visitor mobile number
                    carrier._is_mobile(number_type(phonenumbers.parse(vmob_info)))
                    if (validate_email(hmail_info, verify=True)):
                        hmob_info = "+91"+hmob_info
                        try:
                            # Validating host mobile number
                            carrier._is_mobile(number_type(phonenumbers.parse(hmob_info)))

                            # Sending SMS to the host about the meeting
                            client = Client(account_ID, auth_token)
                            message = client.messages.create(to=hmob_info, from_=twil_num,
                                             body=vname_info + " has a meeting scheduled with you and Visitor's conatact details are\nConact No.:\t" + vmob_info)

                            # Sending E-Mail to the host regarding the meeting
                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.ehlo()
                            server.starttls()
                            server.login(gmailid, password)
                            txt = vname_info + " has a meeting scheduled with you and Visitor's conatact details is:\nConact No.: " + vmob_info
                            server.sendmail(gmailid, hmail_info, txt)

                            # Updating the database when a new cheeck-in is done
                            qry = "insert into Office(vis_name,vis_mail,vis_mob,host_name,host_mail,host_mob)" \
                                    "values (%s,%s,%s,%s,%s,%s)"
                            info = (vname_info, vmail_info, vmob_info, hname_info, hmail_info, hmob_info)
                            cursor1.execute(qry, info)

                            # Saving the changes done to the database
                            mydb.commit()

                            # Showing the Check-In Confirmation
                            tkinter.messagebox.showinfo("SAVED", "Your information has been stored successfully!")

                        # Handling all the Exceptions (Corner Cases)
                        except:
                            tkinter.messagebox.showerror("ERROR!","Please enter correct host number")
                    else:
                        tkinter.messagebox.showerror("ERROR!","Please enter correct Host email")
                except:
                    tkinter.messagebox.showerror("ERROR!","Please enter correct Visitor Number!")
            else:
                tkinter.messagebox.showerror("ERROR!", "Please enter correct Visitor email")
    else:
        tkinter.messagebox.showerror("ERROR!","Please fill all the details")
