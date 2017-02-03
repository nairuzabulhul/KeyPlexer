[![key.png](https://s29.postimg.org/u0zdi2e0n/key.png)](https://postimg.org/image/ymvhqezjn/)

### Project Description:
The project explores operating systems vulnerabilities in protecting against common threats of
malware. The project will be a demonstration of how malware type Trojan is created and
executed in the targeted machines.

__Keyplexer__ is a Remote Access Trojan (RAT) written in Python. It combines the
functionalities of Keylogger with remote access abilities. Meaning, that not only the program
records all movements of the user, but also has access to the machine live through the created
backdoor or Trojan.

### Features:
 [x] Logging ALL keystrokes of the user daily and save them in log.txt file

 [ ] Keystrokes are sanitized for accurate output (Ctrl, Alt, Enter)

 [x] Capture the clipboard contents

 [ ] Detects when the user is accessing special important websites such as social media, banks, etc

 [x] Capture ALL active windows on the host machine every 2 min

 [ ]  Conceal and Hide the logs directory with its file on the victim machine

 [x] Detects and saves all open programs in the machine with their paths

 [x] Sends the logs over email at the end every 1h

 [x] Permanently delete the log files after sending them over email to conceal traces

 [x] Capture screenshots of the user machine and send them via email

 [ ] Interact with the program via text and email messages(like checking the status)

 [ ] Files are renamed to unsuspicious names to avoid detection

 [ ] hide the program from Task Manager Menu

 [x] Checks the victim machine for internet connection, if the target computer is not connected to the internet, all logs     and images will be saved locally and once connected it will start sending them all

 [ ] Send email or text when the user shuts down the computer, logs off or disconnects from the internet

 [ ] Added Persistence to the machine, to avoid disconnection on the restart

 [x] Gets the Wifi credentials on the Accessed Point

 [x] Get all the history of browsers (Chrome, Firefox)

 [ ] Get all bookmarks of browsers, cookies, autofill, and saved password

 [x] Keplexer evades all signature based Anti-viruses  

 [ ] Fingerprint the system and get all the information

 [X] IP detection 

 [ ] Geolocation detection

 [ ] Webcam logging

 [ ] Microphone logging

 [x] Revsershell is added as backdoor trojan

 [ ] Download/ upload file using the backdoor shell functionality
 

### Additioal Steps:
 [ ] Trun the script into an executable 

 [ ] Bind the program to a file with an icon


# TO-DO
 [ ] Encrypt traffic accross the network using AES encryption

 [ ] Detect virtual environment 

 [ ] Previlige Escalation

 [ ] Multiple Clients



## Timeline:
The project is divided on 3 level based on the difficulty:

### Level 1 
* Captures logs from active Windows machine
* Captures logs from browsers -- Chrome, Firefox, Internet Explorer including (Incognito mode) 
* Captures all open windows and their paths
* Store the logs locally 
* Display the logs in clear and organized way (sanitized keystrokes i.e Ctrl, Alt, Enter)

### Level 2 
* 	Send logs via email
* 	Use Task Scheduler to run on startup. (related to Persistence)
* 	Hide the logs file, so the target user cannot recognize it.
* 	Rename files into unsuspicious names 
* 	Add date and time to make a new log file each day.
* 	Capture the clipboard contents
* 	Screenshot the host machine
* 	Get the history, cookies, and saved passwords from of the browsers (Chrome, Firefox)
* 	Using threading with timers to repeat the tasks daily

### Level 3 due 
*  Hide the program from the startup menu in the Task Manager
*  Send logs via FTP
*  Add Reverse Shell (RAT) 
*  Detect important websites and log and screen shot them separately i.e. social media accounts, banks, etc. 
*  Microphone Logging
*  Webcam logging
*  Disable anti-virus or anti Keylogger
*  Bypass Antivirus detection
*  Send files by email at specific time of the day and delete traces
*  Add mouse logging 
*  Finger print the operating system
*  IP detection