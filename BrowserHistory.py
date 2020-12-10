import os
import atexit
import getpass
import datetime
import platform
import sqlite3
import re


d_name = os.environ['COMPUTERNAME']
u_name = getpass.getuser()
d_system = platform.system()
sys_name = os.name
sys_release = platform.release()
full_sys = d_system + " " +  sys_release + " " + sys_name
processor_name = platform.processor() 
sys_drive = os.getenv("SystemDrive")

#LIST OF SOCIAL MEDIA PLATFORMS
s_media = ['https://www.messenger.com', 'https://www.facebook.com', 'https://www.reddit.com', 'https://twitter.com', 'https://www.instagram.com',
           'https://www.tiktok.com', 'https://www.pinterest', 'https://www.linkedin.com', 'https://www.twitch.tv', 'https://www.couchsurfing.com',
           'https://web.whatsapp.com', 'https://www.wechat.com', 'https://www.youtube.com']

#LIST OF TRADING PLATFORMS
t_platforms = ['https://www.amazon.com', 'https://www.ebay.com', 'www.craigslist.org', 'https://www.etsy.com/']

#FIREFOX CATEGORY URL LISTS
s_media_ff = []
t_platforms_ff = []
o_platforms_ff = []

#CHROME CATEGORY URL LISTS
s_media_ch = []
t_platforms_ch = []
o_platforms_ch = []

#RETRIEVING DIRECTORY FOR FIREFOX BROWSERHISTORY
firefox_directory = sys_drive + r'//Users//' + u_name + "//AppData//Roaming//Mozilla//Firefox//Profiles//"
firefox_profiles = os.listdir(firefox_directory)

#RETRIEVING CHROME HISTORY 
def chrome_history():
    id=0
    result=True
    
    try:
        conn=sqlite3.connect(sys_drive + r'//Users//' + u_name + r'//AppData//Local//Google//Chrome//User Data//Default\History')
        c=conn.cursor()
        while result:
            result=False
            ids=[]
            for rows in c.execute("SELECT url FROM urls"):
                id = rows[0]
                for urls in rows:
                    if(list(filter(urls.startswith, s_media)) != []):
                        s_media_ch.append(urls)         
                    elif(list(filter(urls.startswith, t_platforms)) != []):
                        t_platforms_ch.append(urls)
                    else:
                        o_platforms_ch.append(urls)
            conn.commit()
        conn.close()
        return True
    except:
        return False


#RETRIEVING FIREFOX HISTORY 
def firefox_history():
    try:
        for profile in firefox_profiles:
            database_file = firefox_directory + profile + '//places.sqlite'
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(BASE_DIR, database_file)
            db = sqlite3.connect(db_path)
            cursor = db.cursor()
            select_statement = "select moz_places.url, moz_places.visit_count from moz_places;"
            cursor.execute(select_statement)
            results = cursor.fetchall()
            for url, count in results:
                if(list(filter(url.startswith, s_media)) != []):           
                    s_media_ff.append(url) 
                elif(list(filter(url.startswith, t_platforms)) != []):
                    t_platforms_ff.append(url)
                else:
                    o_platforms_ff.append(url)
        return True
    except:
        pass

def print_ff_history(category):
    if category == 'social':
        if len(s_media_ff) != 0:
            for url in s_media_ff:
                print(url)
        else:
            print('There are no social URLs in the firefox history')
    elif category == 'trading':
        if len(t_platforms_ff) != 0:
            for url in t_platforms_ff:
                print(url)
        else:
            print('There are no trading URLs in the firefox history')
    elif category == 'other':
        if len(o_platforms_ff) != 0:
            for url in o_platforms_ff:
                print(url)
        else:
            print('There are no other URLs in the firefox history')
    else:
        print('Enter print_ff_history(social/trading/other) to view the history')
       

def print_ch_history(category):
    if category == 'social':
        if len(s_media_ch) != 0:
            for url in s_media_ch:
                print(url)
        else:
            print('There are no social URLs in the chrome history')
    elif category == 'trading':
        if len(t_platforms_ch) != 0:
            for url in t_platforms_ch:
                print(url)
        else:
            print('There are no trading URLs in the chrome history')
    elif category == 'other':
        if len(o_platforms_ch) != 0:
            for url in o_platforms_ch:
                print(url)
        else:
            print('There are no other URLs in the chrome history')
    else:
        print('Enter print_ch_history(social/trading/other) to view the history')

def print_url_report():
    
    ch_urls = len(s_media_ch) + len(t_platforms_ch) + len(o_platforms_ch)
    if(ch_urls != 0):
        print("============= CHROME BROWSER =============")
        print("Total URLs: \t\t" + str(ch_urls))
        print("Social Media URLs: \t" + str(len(s_media_ch)))
        print("Trading platform URLs: \t" + str(len(t_platforms_ch)))
        print("Other platform URLs: \t" + str(len(o_platforms_ch)))
    else:
        print("No URLs retrieved from Chrome")

    ff_urls = len(s_media_ff) + len(t_platforms_ff) + len(o_platforms_ff)
    if(ff_urls != 0):
        print("============= FIREFOX BROWSER =============")
        print("Total URLs: \t\t" + str(ff_urls))
        print("Social Media URLs: \t" + str(len(s_media_ff)))
        print("Trading platform URLs: \t" + str(len(t_platforms_ff)))
        print("Other platform URLs: \t" + str(len(o_platforms_ff)))
    else:
        print("No URLs retrieved from Firefox")

chrome_history()
firefox_history()




